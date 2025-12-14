from __future__ import annotations
import argparse
import datetime as dt
import yaml
import re
from collections import Counter
from pathlib import Path
from docx import Document

# -----------------------
# 讀取模板（任務規格）
# -----------------------
def load_template(template_path: Path) -> dict:
    with template_path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)

# -----------------------
# 讀取來源文字（30 天文章）
# -----------------------
def read_source_text(source_path: Path) -> str:
    if source_path.suffix.lower() == ".txt":
        return source_path.read_text(encoding="utf-8")
    elif source_path.suffix.lower() == ".docx":
        doc = Document(str(source_path))
        return "\n".join(p.text for p in doc.paragraphs if p.text.strip())
    else:
        raise ValueError(f"不支援的來源格式：{source_path.suffix}")

# -----------------------
# 通用版：從來源文抽出「技術名詞候選」
# -----------------------
def extract_internal_notes(text: str) -> dict:
    """
    通用抽取規則（不靠 LLM）：
    - 抓看起來像技術名詞的字串（英文、含數字或符號）
    - 用頻率排序，取得本書可能的重要技術詞
    """

    # 1) 粗抓候選
    raw_candidates = re.findall(r"[A-Za-z][A-Za-z0-9_\-\.]{1,}", text)

    # 2) 移除常見停用字
    stop = {
        "the","and","with","from","into","that","this","your","you","are","for","to","in","of","on","as",
        "is","be","by","an","or","at","it","we","our","can","will","not","use","using"
    }

    candidates = []
    for w in raw_candidates:
        lw = w.lower()
        if lw in stop:
            continue
        if len(w) < 2:
            continue
        candidates.append(w)

    # 3) 計算出現頻率
    freq = Counter(candidates)

    # 4) 取前 12 個作為候選池
    top_terms = [t for t, _ in freq.most_common(12)]

    # 5) 預覽用（未來可擴充）
    preview = "\n".join([line.strip() for line in text.splitlines() if line.strip()][:8])

    return {
        "observed_terms": top_terms,
        "preview": preview,
        "core_theme_hint": "把書的核心技術與流程，用白話故事說清楚"
    }

# -----------------------
# 生成任務一故事（依輸入而變）
# -----------------------
def generate_task01_story(template: dict, notes: dict) -> list[str]:
    rule = template["structure"].get("required_terms_rule", {})
    min_terms = int(rule.get("min_terms", 3))
    max_terms = int(rule.get("max_terms", 8))

    terms = notes.get("observed_terms", [])
    picked = terms[:max_terms]

    if len(picked) < min_terms:
        picked = picked + ["（核心技術）"] * (min_terms - len(picked))

    pocket = "、".join(picked)

    p1 = (
        "拿到一本完全陌生的技術書時，第一件事不是理解所有細節，"
        "而是先搞清楚：這本書到底要帶你完成什麼。"
        "任務一的目的，就是先用白話把整個主題翻譯給你聽。"
    )

    p2 = (
        f"從這本書的內容中，可以先抓出一些反覆出現的技術關鍵詞：{pocket}。"
        "你現在不需要精通它們，只要把它們當成故事裡的重要角色，"
        "等一下就會看到它們是怎麼一起把事情推進的。"
    )

    p3 = (
        "接下來的故事，會描述一條把想法變成可驗證成果的路線："
        "先有目標與方法，再透過某些工具或框架把事情拆解，"
        "最後產出一個你能實際檢查的結果。"
        "這條路線會成為後續所有任務的共同基礎。"
    )

    snapshot_starter = template["structure"]["required_section_starter"]["snapshot"]
    p4 = (
        f"{snapshot_starter}：你腦中只要留下這張快照——"
        f"這本書會以 {picked[0]} 為核心概念，搭配 {picked[1]}、{picked[2]} 等方法或工具，"
        "一步一步把事情做出來，最後留下可以被你檢查與判斷的成果。"
    )

    return [p1, p2, p3, p4]

# -----------------------
# 檢核是否符合任務規格
# -----------------------
def validate_story(template: dict, paragraphs: list[str]) -> None:
    if len(paragraphs) != template["structure"]["paragraphs"]:
        raise ValueError("段落數不符合模板要求")

    joined = "\n".join(paragraphs)

    # 快照句檢核
    snapshot = template["structure"]["required_section_starter"]["snapshot"]
    if snapshot not in joined:
        raise ValueError("缺少快照收斂段落的固定開頭")

    # 技術名詞數量檢核（通用規則）
    rule = template["structure"].get("required_terms_rule")
    if rule:
        min_terms = int(rule.get("min_terms", 3))
        max_terms = int(rule.get("max_terms", 8))
        observed = template.get("_runtime_observed_terms", [])
        if observed:
            hit = [t for t in observed[:max_terms] if t in joined]
            if len(hit) < min_terms:
                raise ValueError(
                    f"技術名詞出現不足：需要至少 {min_terms} 個，實際只有 {len(hit)} 個"
                )

# -----------------------
# 輸出 Word
# -----------------------
def write_docx(title: str, paragraphs: list[str], output_path: Path) -> None:
    doc = Document()
    doc.add_heading(title, level=1)
    for p in paragraphs:
        doc.add_paragraph(p)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    doc.save(str(output_path))

# -----------------------
# 主程式
# -----------------------
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--template", required=True)
    ap.add_argument("--source", required=True)
    ap.add_argument("--author", required=True)
    ap.add_argument("--book", required=True)
    ap.add_argument("--outdir", default="outputs")
    args = ap.parse_args()

    template = load_template(Path(args.template))
    text = read_source_text(Path(args.source))
    notes = extract_internal_notes(text)

    # runtime only：讓 validate_story 用
    template["_runtime_observed_terms"] = notes.get("observed_terms", [])

    paragraphs = generate_task01_story(template, notes)
    validate_story(template, paragraphs)

    today = dt.datetime.now().strftime("%Y%m%d")
    filename = template["output"]["filename_pattern"].format(
        book=args.book, author=args.author, date=today
    )
    out_path = Path(args.outdir) / filename

    title = template.get("name", "任務一｜主題白話理解")
    write_docx(title, paragraphs, out_path)

    print(f"OK: {out_path}")

if __name__ == "__main__":
    main()
