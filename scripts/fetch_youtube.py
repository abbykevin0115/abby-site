<!doctype html>
<html lang="zh-Hant">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Abby 的粉紅生活日常</title>
  <style>
    :root {
      --pink: #f8d7e3;
      --cream: #fdf1f6;
      --rose: #f4bcd4;
      --white: #ffffff;
      --brown: #6b4b3c;
      --shadow: 0 18px 40px rgba(244, 188, 212, 0.45);
      --text: #57413a;
      --muted: #8c6f64;
      --transition: 180ms ease;
    }

    * { box-sizing: border-box; }

    body {
      margin: 0;
      font-family: "Noto Sans TC", "PingFang TC", "Microsoft JhengHei", sans-serif;
      color: var(--text);
      background: linear-gradient(180deg, var(--cream), var(--pink));
      scroll-behavior: smooth;
    }

    a { color: inherit; text-decoration: none; }

    header {
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      z-index: 10;
      backdrop-filter: blur(10px);
      background: rgba(255, 255, 255, 0.8);
      border-bottom: 1px solid rgba(244, 188, 212, 0.6);
    }

    .nav {
      max-width: 1080px;
      margin: 0 auto;
      padding: 14px 18px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
    }

    .logo {
      font-weight: 800;
      letter-spacing: 1px;
      font-size: 18px;
      color: var(--brown);
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .logo .dot {
      width: 12px;
      height: 12px;
      border-radius: 50%;
      background: var(--rose);
      display: inline-block;
      box-shadow: 0 0 0 6px rgba(244, 188, 212, 0.25);
    }

    .nav-links { display: flex; gap: 12px; }

    .nav-links a {
      padding: 8px 14px;
      border-radius: 999px;
      background: var(--white);
      border: 1px solid rgba(244, 188, 212, 0.7);
      box-shadow: var(--shadow);
      font-weight: 600;
      font-size: 14px;
      transition: transform var(--transition), box-shadow var(--transition);
    }

    .nav-links a:hover {
      transform: translateY(-2px);
      box-shadow: 0 12px 24px rgba(244, 188, 212, 0.6);
    }

    main {
      max-width: 1080px;
      margin: 0 auto;
      padding: 110px 18px 64px;
      display: flex;
      flex-direction: column;
      gap: 72px;
    }

    section {
      background: var(--white);
      border-radius: 28px;
      padding: 36px 28px;
      box-shadow: var(--shadow);
      border: 1px solid rgba(244, 188, 212, 0.4);
      position: relative;
      overflow: hidden;
    }

    .hero {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      align-items: center;
      gap: 32px;
      background: linear-gradient(145deg, var(--cream), var(--pink));
    }

    h1 {
      margin: 0 0 12px;
      font-size: clamp(28px, 5vw, 42px);
      color: var(--brown);
      letter-spacing: 1px;
    }

    p.lead {
      margin: 0 0 20px;
      color: var(--muted);
      line-height: 1.6;
      font-size: 16px;
    }

    .hero-cta {
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
    }

    .dog-btn {
      position: relative;
      padding: 14px 18px 14px 44px;
      border: none;
      background: var(--white);
      border-radius: 18px;
      cursor: pointer;
      font-weight: 700;
      color: var(--brown);
      box-shadow: var(--shadow);
      transition: transform var(--transition), box-shadow var(--transition), background var(--transition);
      outline: none;
    }

    .dog-btn::before,
    .dog-btn::after {
      content: "";
      position: absolute;
      width: 16px;
      height: 18px;
      background: var(--rose);
      border-radius: 12px 12px 4px 4px;
      top: 6px;
      box-shadow: 0 4px 0 rgba(0, 0, 0, 0.05) inset;
    }

    .dog-btn::before { left: 10px; transform: rotate(-6deg); }
    .dog-btn::after  { left: 26px; transform: rotate( 6deg); }

    .dog-btn span { position: relative; z-index: 1; }

    .dog-btn:hover {
      transform: translateY(-3px);
      box-shadow: 0 16px 30px rgba(244, 188, 212, 0.6);
    }

    .dog-btn.active { background: var(--rose); color: var(--white); }

    .dog-icon-btn {
      display: inline-flex;
      flex-direction: column;
      align-items: center;
      gap: 8px;
      padding: 16px 16px 14px;
      min-width: 132px;
      background: var(--white);
      border: 1px solid rgba(244, 188, 212, 0.7);
      box-shadow: var(--shadow);
      transition: transform 140ms ease, box-shadow var(--transition), background var(--transition), border-color var(--transition);
    }

    .dog-icon-btn svg { width: 74px; height: 74px; }
    .dog-icon-btn::before, .dog-icon-btn::after { display: none; }

    .dog-icon-btn .label {
      font-weight: 700;
      color: var(--brown);
      letter-spacing: 0.3px;
    }

    .dog-icon-btn:hover {
      transform: translateY(-2px) scale(1.02);
      box-shadow: 0 16px 30px rgba(244, 188, 212, 0.6);
    }

    .dog-icon-btn.active {
      background: var(--rose);
      color: var(--white);
      border-color: #e19cbb;
      box-shadow: 0 18px 32px rgba(244, 188, 212, 0.65);
    }

    .dog-icon-btn.active .label { color: var(--white); }

    .dog-icon-btn.active svg path,
    .dog-icon-btn.active svg circle,
    .dog-icon-btn.active svg ellipse {
      stroke: #fef6f9;
      fill: #fce8f0;
    }

    .hero-illustration {
      position: relative;
      width: 100%;
      max-width: 420px;
      margin: 0 auto;
      aspect-ratio: 1 / 1;
    }

    .hero svg { width: 100%; height: 100%; display: block; }

    .tag {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 8px 12px;
      background: var(--white);
      border-radius: 999px;
      font-weight: 600;
      color: var(--muted);
      border: 1px dashed rgba(244, 188, 212, 0.7);
      margin-bottom: 12px;
    }

    .section-title {
      margin: 0 0 10px;
      font-size: 26px;
      color: var(--brown);
      letter-spacing: 0.5px;
    }

    .placeholder {
      margin: 0;
      color: var(--muted);
      line-height: 1.7;
    }

    .work   { background: linear-gradient(160deg, var(--pink), var(--cream)); }
    .family { background: linear-gradient(200deg, var(--cream), var(--white)); }
    .personal{ background: linear-gradient(140deg, var(--white), var(--cream)); }

    .floating-dog {
      position: absolute;
      right: 14px;
      bottom: -12px;
      width: 180px;
      opacity: 0.16;
      pointer-events: none;
    }

    .paw {
      position: absolute;
      width: 48px;
      height: 48px;
      border-radius: 50%;
      background: rgba(244, 188, 212, 0.35);
      filter: blur(2px);
      opacity: 0.6;
    }

    .paw::after,
    .paw::before {
      content: "";
      position: absolute;
      width: 16px;
      height: 16px;
      border-radius: 50%;
      background: rgba(244, 188, 212, 0.35);
    }

    .paw::before { top: -6px; left: 8px; }
    .paw::after  { top:  8px; left: -6px; }

    .toggle-row {
      display: flex;
      gap: 10px;
      flex-wrap: wrap;
      margin: 12px 0 18px;
    }

    .card {
      background: var(--white);
      border-radius: 16px;
      padding: 16px;
      border: 1px solid rgba(244, 188, 212, 0.5);
      box-shadow: var(--shadow);
      margin-top: 6px;
    }

    .card h4 { margin: 0 0 6px; color: var(--brown); }
    .card p  { margin: 0; color: var(--muted); line-height: 1.6; }

    /* === MVP 區塊樣式（新增）=== */
    .mvp-box{
      margin-top: 14px;
      padding: 14px;
      border-radius: 16px;
      border: 2px dashed rgba(244, 188, 212, 0.9);
      background: linear-gradient(180deg, rgba(253, 241, 246, 0.75), rgba(255,255,255,0.9));
    }
    .mvp-title{
      margin: 0 0 10px;
      font-size: 14px;
      font-weight: 800;
      color: var(--brown);
      letter-spacing: 0.2px;
    }
    #store-buttons .dog-btn{
      padding-left: 44px;
    }
    #video-list{
      margin: 0;
      padding-left: 22px;
      color: var(--muted);
      line-height: 1.7;
    }

    @media (max-width: 720px) {
      header { position: sticky; }
      .nav { flex-direction: column; align-items: flex-start; }
      main { padding-top: 96px; gap: 56px; }
      section { padding: 28px 22px; }
      .floating-dog { width: 130px; opacity: 0.22; }
    }
  </style>
</head>
<body>
  <header>
    <div class="nav">
      <div class="logo">
        <span class="dot"></span>
        <span>Abby 的粉紅生活日常</span>
      </div>
      <nav class="nav-links">
        <a href="#work">工作</a>
        <a href="#family">家庭</a>
        <a href="#personal">個人</a>
      </nav>
    </div>
  </header>

  <main>
    <section class="hero" id="hero">
      <div>
        <div class="tag">Pink Chihuahua Mood</div>
        <h1>粉色系 × 插畫風吉娃娃的日常陪伴</h1>
        <p class="lead">柔和的淺粉與奶油色，輕盈的留白，加上一隻愛撒嬌的吉娃娃插畫，陪你從工作到家庭，再到個人生活的小確幸。</p>
        <div class="hero-cta">
          <button class="dog-btn" data-target="#work"><span>工作</span></button>
          <button class="dog-btn" data-target="#family"><span>家庭</span></button>
          <button class="dog-btn" data-target="#personal"><span>個人生活</span></button>
        </div>
      </div>
      <div class="hero-illustration">
        <svg viewBox="0 0 320 320" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
          <defs>
            <linearGradient id="fur" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#fbe3ea"/>
              <stop offset="100%" stop-color="#f7c9d9"/>
            </linearGradient>
          </defs>
          <circle cx="160" cy="160" r="150" fill="#fce8f0"/>
          <g>
            <path d="M70 110 C72 60 120 62 142 96 L126 132 Z" fill="url(#fur)" stroke="#e1a7bc" stroke-width="3" stroke-linejoin="round"/>
            <path d="M250 110 C248 60 200 62 178 96 L194 132 Z" fill="url(#fur)" stroke="#e1a7bc" stroke-width="3" stroke-linejoin="round"/>
            <path d="M110 250 C110 210 110 180 160 180 C210 180 210 210 210 250" fill="#fef6f9" stroke="#e1a7bc" stroke-width="3"/>
            <path d="M110 140 Q160 120 210 140 Q222 190 210 240 Q160 260 110 240 Q98 190 110 140 Z" fill="url(#fur)" stroke="#e1a7bc" stroke-width="3" />
            <ellipse cx="140" cy="168" rx="10" ry="14" fill="#3b2b25"/>
            <ellipse cx="180" cy="168" rx="10" ry="14" fill="#3b2b25"/>
            <circle cx="141" cy="164" r="3" fill="#fff"/>
            <circle cx="181" cy="164" r="3" fill="#fff"/>
            <path d="M158 184 Q160 188 162 184" stroke="#3b2b25" stroke-width="3" stroke-linecap="round"/>
            <path d="M150 196 Q160 206 170 196" fill="none" stroke="#d18c9f" stroke-width="4" stroke-linecap="round"/>
            <path d="M152 206 Q160 214 168 206" fill="#f2b8c7" stroke="#d18c9f" stroke-width="2" stroke-linecap="round"/>
            <circle cx="136" cy="188" r="6" fill="#f4c1d3" opacity="0.9"/>
            <circle cx="184" cy="188" r="6" fill="#f4c1d3" opacity="0.9"/>
            <path d="M130 226 Q160 238 190 226" fill="none" stroke="#e1a7bc" stroke-width="3" stroke-linecap="round"/>
            <path d="M108 118 Q132 108 142 132" fill="#fcecf2" stroke="#e1a7bc" stroke-width="3" stroke-linecap="round"/>
            <path d="M212 118 Q188 108 178 132" fill="#fcecf2" stroke="#e1a7bc" stroke-width="3" stroke-linecap="round"/>
          </g>
        </svg>
      </div>
    </section>

    <section id="work" class="work">
      <div class="paw" style="top:18px; left:18px;"></div>
      <div class="paw" style="bottom:24px; right:32px;"></div>
      <img src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 160 120'%3E%3Cpath d='M24 50 Q40 10 70 26 Q96 10 116 44 L124 80 Q120 104 90 104 L44 96 Q18 84 24 50Z' fill='%23fce8f0' stroke='%23e1a7bc' stroke-width='4' stroke-linejoin='round'/%3E%3Cpath d='M62 64 Q74 70 86 64' stroke='%236b4b3c' stroke-width='5' fill='none' stroke-linecap='round'/%3E%3Cellipse cx='60' cy='56' rx='6' ry='9' fill='%236b4b3c'/%3E%3Cellipse cx='94' cy='56' rx='6' ry='9' fill='%236b4b3c'/%3E%3Ccircle cx='60' cy='52' r='2' fill='%23fff'/%3E%3Ccircle cx='94' cy='52' r='2' fill='%23fff'/%3E%3C/svg%3E" alt="" class="floating-dog">
      <div class="tag">Work Mode</div>
      <h2 class="section-title">工作區</h2>
      <p class="placeholder">預留出版與工作內容，吉娃娃在旁溫柔守護，讓粉色系的靈感陪你完成每個案子。</p>
    </section>

    <section id="family" class="family">
      <div class="paw" style="top:14px; right:18px;"></div>
      <div class="paw" style="bottom:18px; left:32px;"></div>
      <div class="tag">Home Sweet Pink</div>
      <h2 class="section-title">家庭區</h2>
      <p class="placeholder">預留家庭記事與粉粉日常，吉娃娃腳印點綴，輕盈留白讓每段故事都有呼吸感。</p>
    </section>

    <section id="personal" class="personal">
      <div class="tag">Personal Picks</div>
      <h2 class="section-title">個人生活：新品開箱 × 超商必買</h2>

      <div class="toggle-row">
        <button class="dog-btn dog-icon-btn active" data-panel="unbox">
          <svg viewBox="0 0 120 120" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
            <path d="M26 42 Q30 14 52 22 Q70 14 86 34 L92 62 Q90 84 70 90 L48 88 Q28 84 26 64 Z" fill="#fce8f0" stroke="#e1a7bc" stroke-width="4" stroke-linejoin="round"/>
            <ellipse cx="48" cy="58" rx="7" ry="10" fill="#6b4b3c"/>
            <ellipse cx="72" cy="58" rx="7" ry="10" fill="#6b4b3c"/>
            <circle cx="48" cy="54" r="2.5" fill="#fff"/>
            <circle cx="72" cy="54" r="2.5" fill="#fff"/>
            <path d="M54 68 Q60 74 66 68" stroke="#d18c9f" stroke-width="4" fill="none" stroke-linecap="round"/>
            <path d="M52 74 Q60 80 68 74" fill="#f2b8c7" stroke="#d18c9f" stroke-width="2" stroke-linecap="round"/>
            <circle cx="44" cy="70" r="5" fill="#f4c1d3" opacity="0.9"/>
            <circle cx="76" cy="70" r="5" fill="#f4c1d3" opacity="0.9"/>
          </svg>
          <span class="label">新品開箱</span>
        </button>

        <button class="dog-btn dog-icon-btn" data-panel="conbini">
          <svg viewBox="0 0 120 120" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
            <path d="M28 44 Q32 18 56 24 Q74 16 90 38 L94 62 Q92 86 70 92 L46 90 Q24 86 28 64 Z" fill="#fce8f0" stroke="#e1a7bc" stroke-width="4" stroke-linejoin="round"/>
            <ellipse cx="52" cy="60" rx="6.5" ry="9" fill="#6b4b3c"/>
            <ellipse cx="76" cy="60" rx="6.5" ry="9" fill="#6b4b3c"/>
            <circle cx="52" cy="56" r="2.4" fill="#fff"/>
            <circle cx="76" cy="56" r="2.4" fill="#fff"/>
            <path d="M56 68 Q64 74 72 68" stroke="#d18c9f" stroke-width="4" fill="none" stroke-linecap="round"/>
            <path d="M54 74 Q64 80 74 74" fill="#f2b8c7" stroke="#d18c9f" stroke-width="2" stroke-linecap="round"/>
            <path d="M40 46 Q46 40 54 48" fill="#fcecf2" stroke="#e1a7bc" stroke-width="3" stroke-linecap="round"/>
            <path d="M84 46 Q78 40 70 48" fill="#fcecf2" stroke="#e1a7bc" stroke-width="3" stroke-linecap="round"/>
            <circle cx="44" cy="70" r="5" fill="#f4c1d3" opacity="0.9"/>
            <circle cx="84" cy="70" r="5" fill="#f4c1d3" opacity="0.9"/>
          </svg>
          <span class="label">超商必買</span>
        </button>
      </div>

      <div class="card" data-panel-content="unbox">
        <h4>新品開箱</h4>
        <p>預設顯示新品開箱心得，粉嫩色調搭配吉娃娃插畫，分享每件療癒小物的第一印象與使用感。</p>
      </div>

      <div class="card" data-panel-content="conbini" style="display: none;">
        <h4>超商必買</h4>
        <p>切換後可看到超商必買清單：粉系甜點、暖心飲品、療癒文具，與吉娃娃一起尋找小確幸。</p>

        <!-- ✅ MVP 區塊（新增） -->
        <div class="mvp-box">
          <div class="mvp-title">YouTube 本月熱門影片（MVP）</div>

          <!-- ✅ 超商按鈕（新增，下一步接 JS） -->
          <div class="toggle-row" id="store-buttons">
            <button class="dog-btn" data-store="7-11"><span>7-11</span></button>
            <button class="dog-btn" data-store="全家"><span>全家</span></button>
            <button class="dog-btn" data-store="萊爾富"><span>萊爾富</span></button>
          </div>

          <!-- ✅ 影片清單容器（新增） -->
          <ol id="video-list">
            <li>（這裡會顯示影片清單）</li>
          </ol>
        </div>
      </div>
    </section>
  </main>

  <script>
    const heroButtons = document.querySelectorAll('.hero-cta .dog-btn');
    heroButtons.forEach(btn => {
      btn.addEventListener('click', () => {
        const target = document.querySelector(btn.dataset.target);
        if (target) {
          heroButtons.forEach(b => b.classList.remove('active'));
          btn.classList.add('active');
          target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
      });
    });

    const toggleButtons = document.querySelectorAll('[data-panel]');
    const toggleCards = document.querySelectorAll('[data-panel-content]');

    toggleButtons.forEach(btn => {
      btn.addEventListener('click', () => {
        const panel = btn.dataset.panel;
        toggleButtons.forEach(b => b.classList.toggle('active', b === btn));
        toggleCards.forEach(card => {
          card.style.display = card.dataset.panelContent === panel ? 'block' : 'none';
        });
      });
    });
  </script>
</body>
</html>
