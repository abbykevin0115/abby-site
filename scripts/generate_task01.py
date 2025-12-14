from __future__ import annotations
import argparse
import datetime as dt
import yaml
from pathlib import Path
from docx import Document

# -----------------------
# 讀取模板（版本化規格）
# -----------------------
def load_template(template_path: Path) -> dict:
    with template_path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)

# -----------------------
# 讀取來源文章（txt / docx）
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
# 內部筆記（不輸出）
# -----------------------
def extract_internal_notes(text: str) -> dict:
    terms = []
    for t in ["Cursor", "GitHub", "Pages", "GitHub Pages", "Action", "commit", "deploy"]:
        if t.lower() in text.lower():
            terms.append(t)

    return {
        "core_theme": "把『想法→版本管理→呈現驗證』變成可重複流程",
        "observed_terms": terms,
        "workflow_hint": "Cursor 生成 → GitHub 記版本 → 網頁呈現驗證 → 回頭修"
    }

# -----------------------
# 生成四段故事（形狀固定）
# -----------------------
def generate_task01_story(template: dict, notes: dict) -> list[str]:
    p1 = (
        "一開始桌上什麼都沒有，只有一句模糊的想法。這本書要做的，是把這個模糊想法，"
        "一步一步帶到『可以被看見、被驗證』的狀態。"
    )

    p2 = (
        "第一個角色是 Cursor。你可以把它想成一個能用自然語言對話的寫作與程式助理，"
        "先陪你把骨幹長出來，再陪你慢慢把內容補齊。"
    )

    p3 = (
        "第二個角色是 GitHub，第三個角色是網頁呈現。流程像接力賽："
        "在 Cursor 裡完成一段，就交給 GitHub 記住版本；"
        "再把成果放到網頁上，看它實際跑起來的樣子。"
    )

    snapshot_starter = template["structure"]["required_section_starter"]["snapshot"]
    p4 = (
        f"{snapshot_starter}：你把想法丟給 Cursor 生成與陪寫；"
        "GitHub 負責把每一次修改記住；"
        "網頁負責把成果攤在你眼前，讓你決定要不要再修。"
    )

    return [p1, p2, p3, p4]

# -----------------------
# 檢核（模板即規格）
# -----------------------
def validate_story(template: dict, paragraphs: list[str]) -> None:
    if len(paragraphs) != template["structure"]["paragraphs"]:
        raise ValueError("段落數不符合模板要求")

    joined = "\n".join(paragraphs)
    for term in template["structure"]["required_terms"]:
        if term not in joined:
            raise ValueError(f"缺少必備名詞：{term}")

    starter = template["structure"]["required_section_starter"]["snapshot"]
    if starter not in joined:
        raise ValueError("缺少快照收斂段落的固定開頭")

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

    paragraphs = generate_task01_story(template, notes)
    validate_story(template, paragraphs)

    today = dt.datetime.now().strftime("%Y%m%d")
    filename = template["output"]["filename_pattern"].format(
        book=args.book, author=args.author, date=today
    )
    out_path = Path(args.outdir) / filename

    title = template["name"]
    write_docx(title, paragraphs, out_path)
    print(f"OK: {out_path}")

if __name__ == "__main__":
    main()
