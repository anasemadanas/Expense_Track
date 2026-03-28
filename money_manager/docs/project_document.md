<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Money Manager — Project Documentation</title>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600&family=Outfit:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<style>
  :root {
    --bg-primary: #0a0e17;
    --bg-secondary: #111827;
    --bg-card: #151d2e;
    --bg-card-alt: #182036;
    --bg-code: #0d1321;
    --border: #1e2d4a;
    --border-glow: #2563eb33;
    --text-primary: #e8edf5;
    --text-secondary: #8896b3;
    --text-muted: #5a6a8a;
    --accent-blue: #3b82f6;
    --accent-cyan: #06b6d4;
    --accent-emerald: #10b981;
    --accent-amber: #f59e0b;
    --accent-rose: #f43f5e;
    --accent-violet: #8b5cf6;
    --accent-blue-glow: #3b82f620;
    --gradient-hero: linear-gradient(135deg, #3b82f6 0%, #06b6d4 50%, #10b981 100%);
    --gradient-subtle: linear-gradient(135deg, #1e3a5f 0%, #1a1e2e 100%);
  }

  * { margin: 0; padding: 0; box-sizing: border-box; }

  html { scroll-behavior: smooth; }

  body {
    font-family: 'Outfit', sans-serif;
    background: var(--bg-primary);
    color: var(--text-primary);
    line-height: 1.7;
    -webkit-font-smoothing: antialiased;
  }

  /* ── Scrollbar ── */
  ::-webkit-scrollbar { width: 6px; }
  ::-webkit-scrollbar-track { background: var(--bg-primary); }
  ::-webkit-scrollbar-thumb { background: var(--border); border-radius: 3px; }
  ::-webkit-scrollbar-thumb:hover { background: var(--accent-blue); }

  /* ── Container ── */
  .container { max-width: 960px; margin: 0 auto; padding: 0 2rem; }

  /* ── Hero ── */
  .hero {
    position: relative;
    padding: 5rem 0 4rem;
    overflow: hidden;
  }

  .hero::before {
    content: '';
    position: absolute;
    top: -200px; right: -200px;
    width: 600px; height: 600px;
    background: radial-gradient(circle, #3b82f60d 0%, transparent 70%);
    pointer-events: none;
  }

  .hero::after {
    content: '';
    position: absolute;
    bottom: -100px; left: -100px;
    width: 400px; height: 400px;
    background: radial-gradient(circle, #06b6d40a 0%, transparent 70%);
    pointer-events: none;
  }

  .hero-icon {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 56px; height: 56px;
    background: var(--gradient-hero);
    border-radius: 14px;
    font-size: 1.6rem;
    margin-bottom: 1.5rem;
    box-shadow: 0 8px 32px #3b82f630;
  }

  .hero h1 {
    font-size: 3rem;
    font-weight: 800;
    letter-spacing: -0.03em;
    line-height: 1.1;
    margin-bottom: 1rem;
    background: linear-gradient(135deg, #e8edf5 30%, #8896b3 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }

  .hero-tagline {
    font-size: 1.15rem;
    color: var(--text-secondary);
    max-width: 620px;
    margin-bottom: 2rem;
    font-weight: 300;
  }

  .badges { display: flex; flex-wrap: wrap; gap: 0.5rem; margin-bottom: 2rem; }

  .badge {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    padding: 0.35rem 0.85rem;
    font-size: 0.78rem;
    font-weight: 500;
    border-radius: 100px;
    border: 1px solid var(--border);
    background: var(--bg-card);
    color: var(--text-secondary);
    letter-spacing: 0.02em;
  }

  .badge .dot {
    width: 7px; height: 7px;
    border-radius: 50%;
    display: inline-block;
  }

  .badge .dot.blue { background: var(--accent-blue); }
  .badge .dot.green { background: var(--accent-emerald); }
  .badge .dot.amber { background: var(--accent-amber); }
  .badge .dot.violet { background: var(--accent-violet); }
  .badge .dot.cyan { background: var(--accent-cyan); }

  .meta-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
    gap: 1rem;
    margin-top: 1.5rem;
  }

  .meta-item {
    padding: 1rem 1.25rem;
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 10px;
  }

  .meta-item .label {
    font-size: 0.7rem;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: var(--text-muted);
    margin-bottom: 0.25rem;
    font-weight: 600;
  }

  .meta-item .value {
    font-size: 0.95rem;
    font-weight: 600;
    color: var(--text-primary);
  }

  /* ── Table of Contents ── */
  .toc {
    margin: 2rem 0 3rem;
    padding: 2rem;
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 12px;
  }

  .toc h2 {
    font-size: 0.8rem;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: var(--text-muted);
    margin-bottom: 1.2rem;
    font-weight: 600;
  }

  .toc-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
    gap: 0.4rem;
  }

  .toc a {
    display: flex;
    align-items: center;
    gap: 0.6rem;
    padding: 0.5rem 0.7rem;
    color: var(--text-secondary);
    text-decoration: none;
    font-size: 0.88rem;
    font-weight: 400;
    border-radius: 6px;
    transition: all 0.2s;
  }

  .toc a:hover {
    background: var(--bg-card-alt);
    color: var(--accent-blue);
  }

  .toc a .num {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem;
    color: var(--text-muted);
    min-width: 1.6rem;
  }

  /* ── Sections ── */
  .section {
    margin-bottom: 4rem;
    animation: fadeIn 0.6s ease-out;
  }

  @keyframes fadeIn {
    from { opacity: 0; transform: translateY(12px); }
    to { opacity: 1; transform: translateY(0); }
  }

  .section-header {
    display: flex;
    align-items: center;
    gap: 0.8rem;
    margin-bottom: 1.5rem;
    padding-bottom: 1rem;
    border-bottom: 1px solid var(--border);
  }

  .section-num {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 32px; height: 32px;
    background: var(--accent-blue);
    color: white;
    font-size: 0.82rem;
    font-weight: 700;
    border-radius: 8px;
    flex-shrink: 0;
  }

  .section-header h2 {
    font-size: 1.6rem;
    font-weight: 700;
    letter-spacing: -0.02em;
  }

  .section p {
    color: var(--text-secondary);
    font-size: 0.95rem;
    margin-bottom: 1rem;
    max-width: 720px;
  }

  /* ── Cards ── */
  .card-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 1rem;
  }

  .card {
    padding: 1.5rem;
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 12px;
    transition: border-color 0.25s, box-shadow 0.25s;
  }

  .card:hover {
    border-color: var(--accent-blue);
    box-shadow: 0 4px 24px var(--accent-blue-glow);
  }

  .card-icon {
    font-size: 1.3rem;
    margin-bottom: 0.75rem;
  }

  .card h3 {
    font-size: 1rem;
    font-weight: 600;
    margin-bottom: 0.5rem;
  }

  .card p {
    font-size: 0.85rem;
    color: var(--text-secondary);
    line-height: 1.5;
  }

  /* ── Architecture ── */
  .arch-layer {
    padding: 1.25rem 1.5rem;
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 10px;
    margin-bottom: 0.75rem;
    position: relative;
  }

  .arch-layer.gui { border-left: 3px solid var(--accent-blue); }
  .arch-layer.service { border-left: 3px solid var(--accent-emerald); }
  .arch-layer.data { border-left: 3px solid var(--accent-violet); }

  .arch-layer h3 {
    font-size: 0.95rem;
    font-weight: 600;
    margin-bottom: 0.3rem;
  }

  .arch-layer .arch-sub {
    font-size: 0.82rem;
    color: var(--text-muted);
    font-family: 'JetBrains Mono', monospace;
  }

  .arch-layer ul {
    margin-top: 0.6rem;
    padding-left: 1.2rem;
  }

  .arch-layer li {
    font-size: 0.85rem;
    color: var(--text-secondary);
    margin-bottom: 0.25rem;
  }

  .arch-connector {
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 0.3rem 0;
    color: var(--text-muted);
    font-size: 0.75rem;
    font-family: 'JetBrains Mono', monospace;
    gap: 0.4rem;
  }

  .arch-connector .arrow {
    font-size: 1.1rem;
    color: var(--accent-cyan);
  }

  /* ── SOLID ── */
  .solid-grid {
    display: grid;
    gap: 0.75rem;
  }

  .solid-item {
    display: flex;
    gap: 1rem;
    padding: 1.25rem 1.5rem;
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 10px;
    align-items: flex-start;
  }

  .solid-letter {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 38px; height: 38px;
    border-radius: 10px;
    font-weight: 700;
    font-size: 1.1rem;
    flex-shrink: 0;
  }

  .solid-letter.s { background: #3b82f620; color: var(--accent-blue); }
  .solid-letter.o { background: #10b98120; color: var(--accent-emerald); }
  .solid-letter.l { background: #f59e0b20; color: var(--accent-amber); }
  .solid-letter.i { background: #8b5cf620; color: var(--accent-violet); }
  .solid-letter.d { background: #06b6d420; color: var(--accent-cyan); }

  .solid-content h4 {
    font-size: 0.9rem;
    font-weight: 600;
    margin-bottom: 0.2rem;
  }

  .solid-content p {
    font-size: 0.83rem;
    color: var(--text-secondary);
    margin: 0;
  }

  .solid-content code {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.78rem;
    background: var(--bg-code);
    padding: 0.15rem 0.4rem;
    border-radius: 4px;
    color: var(--accent-cyan);
  }

  /* ── Code Block ── */
  .code-block {
    background: var(--bg-code);
    border: 1px solid var(--border);
    border-radius: 10px;
    overflow: hidden;
    margin: 1rem 0;
  }

  .code-header {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.7rem 1.2rem;
    background: var(--bg-card);
    border-bottom: 1px solid var(--border);
    font-size: 0.78rem;
    color: var(--text-muted);
    font-family: 'JetBrains Mono', monospace;
  }

  .code-header .dots {
    display: flex;
    gap: 5px;
  }

  .code-header .dots span {
    width: 10px; height: 10px;
    border-radius: 50%;
  }

  .code-header .dots span:nth-child(1) { background: #f43f5e; }
  .code-header .dots span:nth-child(2) { background: #f59e0b; }
  .code-header .dots span:nth-child(3) { background: #10b981; }

  .code-body {
    padding: 1.25rem 1.5rem;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.8rem;
    line-height: 1.65;
    color: var(--text-secondary);
    overflow-x: auto;
    white-space: pre;
  }

  .code-body .comment { color: var(--text-muted); }
  .code-body .folder { color: var(--accent-blue); }
  .code-body .file { color: var(--text-secondary); }

  /* ── Tables ── */
  .table-wrap {
    overflow-x: auto;
    border: 1px solid var(--border);
    border-radius: 10px;
    margin: 1rem 0;
  }

  table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.88rem;
  }

  thead th {
    text-align: left;
    padding: 0.85rem 1.2rem;
    background: var(--bg-card);
    color: var(--text-muted);
    font-weight: 600;
    font-size: 0.75rem;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    border-bottom: 1px solid var(--border);
  }

  tbody td {
    padding: 0.75rem 1.2rem;
    border-bottom: 1px solid var(--border);
    color: var(--text-secondary);
  }

  tbody tr:last-child td { border-bottom: none; }

  tbody tr:hover { background: var(--bg-card-alt); }

  tbody td:first-child { font-weight: 500; color: var(--text-primary); }

  /* ── DB Schema ── */
  .db-table-group {
    display: grid;
    gap: 1rem;
    margin: 1.5rem 0;
  }

  .db-table {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 10px;
    overflow: hidden;
  }

  .db-table-name {
    padding: 0.8rem 1.2rem;
    background: var(--bg-card-alt);
    border-bottom: 1px solid var(--border);
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.85rem;
    font-weight: 600;
    color: var(--accent-cyan);
  }

  .db-columns {
    padding: 0.75rem 1.2rem;
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
  }

  .db-col {
    padding: 0.3rem 0.7rem;
    background: var(--bg-code);
    border: 1px solid var(--border);
    border-radius: 6px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.76rem;
    color: var(--text-secondary);
  }

  .db-col.pk { border-color: var(--accent-amber); color: var(--accent-amber); }
  .db-col.fk { border-color: var(--accent-violet); color: var(--accent-violet); }

  /* ── FR Cards ── */
  .fr-group { margin-bottom: 1.5rem; }

  .fr-header {
    display: flex;
    align-items: center;
    gap: 0.6rem;
    margin-bottom: 0.75rem;
  }

  .fr-id {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem;
    padding: 0.2rem 0.5rem;
    background: var(--accent-blue-glow);
    color: var(--accent-blue);
    border-radius: 4px;
    font-weight: 600;
  }

  .fr-header h3 {
    font-size: 1.05rem;
    font-weight: 600;
  }

  .fr-list {
    padding-left: 1.2rem;
    list-style: none;
  }

  .fr-list li {
    position: relative;
    padding: 0.35rem 0 0.35rem 1.2rem;
    font-size: 0.88rem;
    color: var(--text-secondary);
  }

  .fr-list li::before {
    content: '';
    position: absolute;
    left: 0;
    top: 0.75rem;
    width: 6px; height: 6px;
    border-radius: 50%;
    background: var(--accent-blue);
  }

  /* ── Steps ── */
  .steps { counter-reset: step; margin: 1.5rem 0; }

  .step {
    display: flex;
    gap: 1rem;
    margin-bottom: 1.5rem;
    align-items: flex-start;
  }

  .step-num {
    counter-increment: step;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 36px; height: 36px;
    background: var(--accent-blue);
    color: white;
    font-weight: 700;
    font-size: 0.9rem;
    border-radius: 50%;
    flex-shrink: 0;
  }

  .step-content h4 {
    font-size: 0.95rem;
    font-weight: 600;
    margin-bottom: 0.3rem;
  }

  .step-content .cmd {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.82rem;
    background: var(--bg-code);
    padding: 0.6rem 1rem;
    border-radius: 8px;
    border: 1px solid var(--border);
    color: var(--accent-emerald);
    margin-top: 0.4rem;
    display: block;
  }

  /* ── Future ── */
  .future-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 1rem;
  }

  .future-card {
    padding: 1.25rem 1.5rem;
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 10px;
    transition: transform 0.2s, box-shadow 0.2s;
  }

  .future-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(0,0,0,0.3);
  }

  .future-card h4 {
    font-size: 0.95rem;
    font-weight: 600;
    margin-bottom: 0.35rem;
  }

  .future-card p {
    font-size: 0.83rem;
    color: var(--text-secondary);
    margin: 0;
  }

  /* ── Constraints ── */
  .split-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1.5rem;
  }

  @media (max-width: 640px) {
    .split-grid { grid-template-columns: 1fr; }
  }

  .split-grid h3 {
    font-size: 1rem;
    font-weight: 600;
    margin-bottom: 0.8rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
  }

  .constraint-list {
    list-style: none;
    padding: 0;
  }

  .constraint-list li {
    position: relative;
    padding: 0.4rem 0 0.4rem 1.2rem;
    font-size: 0.85rem;
    color: var(--text-secondary);
  }

  .constraint-list li::before {
    content: '›';
    position: absolute;
    left: 0;
    color: var(--accent-blue);
    font-weight: 700;
    font-size: 1.1rem;
    line-height: 1.5;
  }

  /* ── Contributing ── */
  .contrib-steps {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 0.75rem;
    margin: 1rem 0;
  }

  .contrib-step {
    display: flex;
    align-items: center;
    gap: 0.6rem;
    padding: 0.85rem 1rem;
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 8px;
    font-size: 0.85rem;
    color: var(--text-secondary);
  }

  .contrib-step .cs-num {
    width: 24px; height: 24px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: var(--accent-blue-glow);
    color: var(--accent-blue);
    font-weight: 700;
    font-size: 0.75rem;
    border-radius: 6px;
    flex-shrink: 0;
  }

  /* ── Footer ── */
  .footer {
    padding: 3rem 0;
    text-align: center;
    border-top: 1px solid var(--border);
    margin-top: 2rem;
  }

  .footer p {
    font-size: 0.82rem;
    color: var(--text-muted);
  }

  /* ── ER Diagram ── */
  .er-diagram {
    display: flex;
    align-items: flex-start;
    gap: 2rem;
    margin: 1.5rem 0;
    flex-wrap: wrap;
    justify-content: center;
  }

  .er-entity {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 10px;
    overflow: hidden;
    min-width: 140px;
  }

  .er-entity.central {
    border-color: var(--accent-blue);
    box-shadow: 0 0 20px var(--accent-blue-glow);
  }

  .er-entity-name {
    padding: 0.5rem 1rem;
    background: var(--bg-card-alt);
    border-bottom: 1px solid var(--border);
    font-weight: 600;
    font-size: 0.85rem;
    text-align: center;
  }

  .er-entity.central .er-entity-name {
    background: var(--accent-blue);
    color: white;
  }

  .er-fields {
    padding: 0.6rem 1rem;
  }

  .er-field {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem;
    color: var(--text-secondary);
    padding: 0.15rem 0;
  }

  .er-field.key { color: var(--accent-amber); }

  .er-relations {
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 0.6rem;
    align-self: center;
  }

  .er-rel {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem;
    color: var(--text-muted);
    display: flex;
    align-items: center;
    gap: 0.4rem;
  }

  .er-rel .arrow-line { color: var(--accent-cyan); }

  /* ── Responsive ── */
  @media (max-width: 768px) {
    .hero h1 { font-size: 2rem; }
    .container { padding: 0 1.25rem; }
    .card-grid, .future-grid { grid-template-columns: 1fr; }
    .toc-grid { grid-template-columns: 1fr; }
    .meta-grid { grid-template-columns: repeat(2, 1fr); }
    .er-diagram { flex-direction: column; align-items: center; }
  }

  /* ── Divider ── */
  .divider {
    height: 1px;
    background: var(--border);
    margin: 3rem 0;
  }
</style>
</head>
<body>

<!-- ═══ HERO ═══ -->
<header class="hero">
  <div class="container">
    <div class="hero-icon">💰</div>
    <h1>Money Manager App</h1>
    <p class="hero-tagline">A Python desktop application for managing personal finances — track expenses, income, budgets, notes, and financial goals efficiently.</p>

    <div class="badges">
      <span class="badge"><span class="dot blue"></span> Python 3.10+</span>
      <span class="badge"><span class="dot green"></span> 3-Tier Architecture</span>
      <span class="badge"><span class="dot violet"></span> SOLID Principles</span>
      <span class="badge"><span class="dot amber"></span> MIT License</span>
      <span class="badge"><span class="dot cyan"></span> In Development</span>
    </div>

    <div class="meta-grid">
      <div class="meta-item">
        <div class="label">Version</div>
        <div class="value">1.0</div>
      </div>
      <div class="meta-item">
        <div class="label">Author</div>
        <div class="value">Your Name</div>
      </div>
      <div class="meta-item">
        <div class="label">Language</div>
        <div class="value">Python</div>
      </div>
      <div class="meta-item">
        <div class="label">Architecture</div>
        <div class="value">3-Tier + SOLID</div>
      </div>
      <div class="meta-item">
        <div class="label">Future Platforms</div>
        <div class="value">Desktop, Android, Web</div>
      </div>
    </div>
  </div>
</header>

<main class="container">

  <!-- ═══ TABLE OF CONTENTS ═══ -->
  <nav class="toc">
    <h2>Table of Contents</h2>
    <div class="toc-grid">
      <a href="#introduction"><span class="num">01</span> Introduction</a>
      <a href="#objectives"><span class="num">02</span> Project Objectives</a>
      <a href="#features"><span class="num">03</span> Features</a>
      <a href="#architecture"><span class="num">04</span> System Architecture</a>
      <a href="#solid"><span class="num">05</span> SOLID Principles</a>
      <a href="#structure"><span class="num">06</span> Folder Structure</a>
      <a href="#database"><span class="num">07</span> Database Design</a>
      <a href="#functional"><span class="num">08</span> Functional Requirements</a>
      <a href="#nonfunctional"><span class="num">09</span> Non-Functional Requirements</a>
      <a href="#howtorun"><span class="num">10</span> How to Run</a>
      <a href="#future"><span class="num">11</span> Future Enhancements</a>
      <a href="#constraints"><span class="num">12</span> Constraints &amp; Assumptions</a>
      <a href="#contributing"><span class="num">13</span> Contributing</a>
      <a href="#license"><span class="num">14</span> License</a>
    </div>
  </nav>

  <!-- ═══ 1. INTRODUCTION ═══ -->
  <section class="section" id="introduction">
    <div class="section-header">
      <span class="section-num">1</span>
      <h2>Introduction</h2>
    </div>
    <div class="meta-grid" style="margin-bottom:1.5rem">
      <div class="meta-item">
        <div class="label">Project Name</div>
        <div class="value">Money Manager App</div>
      </div>
      <div class="meta-item">
        <div class="label">Objective</div>
        <div class="value">Manage finances efficiently</div>
      </div>
      <div class="meta-item">
        <div class="label">Programming Language</div>
        <div class="value">Python</div>
      </div>
      <div class="meta-item">
        <div class="label">Future Plans</div>
        <div class="value">Android &amp; Web versions</div>
      </div>
    </div>
    <p>The Money Manager Application is a standalone desktop personal finance tool that enables individuals to track income and expenses, categorize transactions, manage monthly budgets, set personal financial goals, write notes, and view visual reports from an intuitive desktop GUI. The system is built in Python using a strict 3-Tier + SOLID architecture to ensure maintainability and future extensibility to Android and Web platforms.</p>
  </section>

  <div class="divider"></div>

  <!-- ═══ 2. OBJECTIVES ═══ -->
  <section class="section" id="objectives">
    <div class="section-header">
      <span class="section-num">2</span>
      <h2>Project Objectives</h2>
    </div>
    <ul class="fr-list">
      <li>Track expenses and income</li>
      <li>Categorize transactions</li>
      <li>Manage monthly budgets</li>
      <li>Dashboard with charts for financial reports</li>
      <li>Notes &amp; Goals system for reminders and objectives</li>
      <li>Flexible architecture for future expansion (Android, Web)</li>
    </ul>
  </section>

  <div class="divider"></div>

  <!-- ═══ 3. FEATURES ═══ -->
  <section class="section" id="features">
    <div class="section-header">
      <span class="section-num">3</span>
      <h2>Features</h2>
    </div>
    <div class="card-grid">
      <div class="card">
        <div class="card-icon">📊</div>
        <h3>Expenses &amp; Income Tracking</h3>
        <p>Record, edit, and delete financial transactions with full categorization support.</p>
      </div>
      <div class="card">
        <div class="card-icon">💳</div>
        <h3>Budget Management</h3>
        <p>Define per-category monthly budgets with real-time over-limit alerting.</p>
      </div>
      <div class="card">
        <div class="card-icon">🎯</div>
        <h3>Notes &amp; Goals System</h3>
        <p>Attach notes to entries and track progress toward savings goals with deadlines.</p>
      </div>
      <div class="card">
        <div class="card-icon">📈</div>
        <h3>Dashboard with Charts</h3>
        <p>Visual summary of financial health with trend lines, pie charts, and KPI cards.</p>
      </div>
      <div class="card">
        <div class="card-icon">🔄</div>
        <h3>CRUD Operations</h3>
        <p>Full create, read, update, and delete for all data entities in the system.</p>
      </div>
      <div class="card">
        <div class="card-icon">📄</div>
        <h3>Reports Export</h3>
        <p>Generate PDF and Excel reports filtered by date range or category.</p>
      </div>
      <div class="card">
        <div class="card-icon">💱</div>
        <h3>Multi-currency Support</h3>
        <p>User-configurable display currency with ISO 4217 code validation.</p>
      </div>
      <div class="card">
        <div class="card-icon">🖥️</div>
        <h3>Easy-to-use GUI</h3>
        <p>Built with PyQt5 or Tkinter for a clean, intuitive desktop experience.</p>
      </div>
    </div>
  </section>

  <div class="divider"></div>

  <!-- ═══ 4. ARCHITECTURE ═══ -->
  <section class="section" id="architecture">
    <div class="section-header">
      <span class="section-num">4</span>
      <h2>System Architecture</h2>
    </div>
    <p>The application follows a strict 3-Tier Architecture, enforcing clear separation of concerns. Each tier communicates exclusively with the adjacent tier through well-defined interfaces.</p>

    <div style="margin-top:1.5rem">
      <div class="arch-layer gui">
        <h3>A. Presentation Layer (GUI Layer)</h3>
        <div class="arch-sub">PyQt5 / Tkinter &bull; Views &bull; Event Handlers</div>
        <ul>
          <li>Responsible for the graphical user interface (PyQt or Tkinter)</li>
          <li>Does <strong>not</strong> contain business logic</li>
          <li>Interacts only with the Business Layer</li>
        </ul>
      </div>

      <div class="arch-connector"><span class="arrow">↓</span> calls</div>

      <div class="arch-layer service">
        <h3>B. Business Logic Layer (Service Layer)</h3>
        <div class="arch-sub">TransactionService &bull; BudgetService &bull; GoalService &bull; Validators</div>
        <ul>
          <li>Contains all domain logic, calculations, and validations</li>
          <li>Handles budget validation and transaction rules</li>
          <li>Independent of UI and database</li>
        </ul>
      </div>

      <div class="arch-connector"><span class="arrow">↓</span> calls</div>

      <div class="arch-layer data">
        <h3>C. Data Layer (Repository Layer)</h3>
        <div class="arch-sub">SQLiteRepo &bull; ITransactionRepo &bull; IBudgetRepo &bull; INotesRepo</div>
        <ul>
          <li>Responsible for data storage (SQLite, JSON, or API)</li>
          <li>Contains Repositories and Interfaces</li>
          <li>Allows changing the storage implementation without modifying the Business Layer</li>
        </ul>
      </div>

      <div class="arch-connector"><span class="arrow">↓</span></div>

      <div style="text-align:center; padding:0.8rem; background:var(--bg-card); border:1px solid var(--border); border-radius:10px; border-left:3px solid var(--accent-amber);">
        <span style="font-family:'JetBrains Mono',monospace; font-size:0.85rem; color:var(--accent-amber);">SQLite Database</span>
      </div>
    </div>
  </section>

  <div class="divider"></div>

  <!-- ═══ 5. SOLID ═══ -->
  <section class="section" id="solid">
    <div class="section-header">
      <span class="section-num">5</span>
      <h2>SOLID Principles</h2>
    </div>
    <p>All components are designed in strict adherence to SOLID object-oriented design principles to maximize maintainability and extensibility.</p>

    <div class="solid-grid" style="margin-top:1.25rem">
      <div class="solid-item">
        <div class="solid-letter s">S</div>
        <div class="solid-content">
          <h4>Single Responsibility</h4>
          <p>Each class has one responsibility (e.g., <code>TransactionService</code>, <code>BudgetRepo</code>)</p>
        </div>
      </div>
      <div class="solid-item">
        <div class="solid-letter o">O</div>
        <div class="solid-content">
          <h4>Open / Closed</h4>
          <p>Extend features without modifying existing classes. New report types or backends are added via new classes.</p>
        </div>
      </div>
      <div class="solid-item">
        <div class="solid-letter l">L</div>
        <div class="solid-content">
          <h4>Liskov Substitution</h4>
          <p>Any repository can be replaced without breaking services (e.g., SQLite → REST API).</p>
        </div>
      </div>
      <div class="solid-item">
        <div class="solid-letter i">I</div>
        <div class="solid-content">
          <h4>Interface Segregation</h4>
          <p>Small, focused interfaces like <code>IBudgetRepo</code>, <code>ITransactionRepo</code></p>
        </div>
      </div>
      <div class="solid-item">
        <div class="solid-letter d">D</div>
        <div class="solid-content">
          <h4>Dependency Inversion</h4>
          <p>Upper layers depend on interfaces, not concrete classes. Dependencies injected at runtime.</p>
        </div>
      </div>
    </div>
  </section>

  <div class="divider"></div>

  <!-- ═══ 6. FOLDER STRUCTURE ═══ -->
  <section class="section" id="structure">
    <div class="section-header">
      <span class="section-num">6</span>
      <h2>Folder Structure</h2>
    </div>

    <div class="code-block">
      <div class="code-header">
        <div class="dots"><span></span><span></span><span></span></div>
        project-structure
      </div>
      <div class="code-body"><span class="folder">Expense_Track/</span>
│
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
│
└── <span class="folder">money_manager/</span>
    ├── __init__.py
    ├── main.py
    ├── <span class="folder">src/</span>
    │   ├── <span class="folder">presentation/</span>              <span class="comment"># GUI Layer</span>
    │   │   ├── __init__.py
    │   │   ├── <span class="folder">views/</span>
    │   │   │   ├── __init__.py
    │   │   │   ├── dashboard_view.py
    │   │   │   ├── add_transaction_view.py
    │   │   │   └── budget_view.py
    │   │   └── <span class="folder">controllers/</span>
    │   │       ├── __init__.py
    │   │       └── transaction_controller.py
    │   │
    │   ├── <span class="folder">business/</span>                  <span class="comment"># Service Layer</span>
    │   │   ├── __init__.py
    │   │   ├── <span class="folder">services/</span>
    │   │   │   ├── __init__.py
    │   │   │   ├── transaction_service.py
    │   │   │   └── budget_service.py
    │   │   └── <span class="folder">models/</span>
    │   │       ├── __init__.py
    │   │       ├── transaction.py
    │   │       └── budget.py
    │   │
    │   ├── <span class="folder">data/</span>                      <span class="comment"># Repository Layer</span>
    │   │   ├── __init__.py
    │   │   ├── database.py
    │   │   ├── <span class="folder">repositories/</span>
    │   │   │   ├── __init__.py
    │   │   │   ├── transaction_repo.py
    │   │   │   └── budget_repo.py
    │   │   └── <span class="folder">interfaces/</span>
    │   │       ├── __init__.py
    │   │       ├── ITransactionRepo.py
    │   │       └── IBudgetRepo.py
    │   │
    │   └── <span class="folder">shared/</span>
    │       ├── __init__.py
    │       ├── util.py
    │       └── constants.py
    │
    └── <span class="folder">tests/</span>
        ├── __init__.py
        ├── test_transaction_service.py
        ├── test_budget_service.py
        └── test_repo.py</div>
    </div>
  </section>

  <div class="divider"></div>

  <!-- ═══ 7. DATABASE ═══ -->
  <section class="section" id="database">
    <div class="section-header">
      <span class="section-num">7</span>
      <h2>Database Design</h2>
    </div>
    <p>The application uses SQLite for local data persistence. All entities are linked to the User entity, enforcing data isolation per user account.</p>

    <!-- ER Diagram -->
    <div class="er-diagram">
      <div class="er-entity central">
        <div class="er-entity-name">User</div>
        <div class="er-fields">
          <div class="er-field key">id (PK)</div>
          <div class="er-field">username</div>
          <div class="er-field">email</div>
          <div class="er-field">password_hash</div>
          <div class="er-field">currency</div>
          <div class="er-field">theme</div>
        </div>
      </div>

      <div class="er-relations">
        <div class="er-rel"><span class="arrow-line">——1:N——▶</span> Transaction</div>
        <div class="er-rel"><span class="arrow-line">——1:N——▶</span> Budget</div>
        <div class="er-rel"><span class="arrow-line">——1:N——▶</span> Note</div>
        <div class="er-rel"><span class="arrow-line">——1:N——▶</span> Goal</div>
      </div>

      <div style="display:flex; flex-direction:column; gap:0.75rem;">
        <div class="er-entity">
          <div class="er-entity-name">Transaction</div>
          <div class="er-fields">
            <div class="er-field key">id (PK)</div>
            <div class="er-field">user_id (FK)</div>
            <div class="er-field">name, amount</div>
            <div class="er-field">category, date, type</div>
          </div>
        </div>
        <div class="er-entity">
          <div class="er-entity-name">Budget</div>
          <div class="er-fields">
            <div class="er-field key">id (PK)</div>
            <div class="er-field">user_id (FK)</div>
            <div class="er-field">name, amount, period</div>
          </div>
        </div>
        <div class="er-entity">
          <div class="er-entity-name">Note</div>
          <div class="er-fields">
            <div class="er-field key">id (PK)</div>
            <div class="er-field">user_id (FK)</div>
            <div class="er-field">title, content, date, tag</div>
          </div>
        </div>
        <div class="er-entity">
          <div class="er-entity-name">Goal</div>
          <div class="er-fields">
            <div class="er-field key">id (PK)</div>
            <div class="er-field">user_id (FK)</div>
            <div class="er-field">title, target, saved</div>
            <div class="er-field">deadline</div>
          </div>
        </div>
      </div>
    </div>

    <!-- DB Tables -->
    <div class="db-table-group">
      <div class="db-table">
        <div class="db-table-name">users</div>
        <div class="db-columns">
          <span class="db-col pk">id PK</span>
          <span class="db-col">username</span>
          <span class="db-col">email</span>
          <span class="db-col">password_hash</span>
          <span class="db-col">currency</span>
          <span class="db-col">theme</span>
        </div>
      </div>
      <div class="db-table">
        <div class="db-table-name">transactions</div>
        <div class="db-columns">
          <span class="db-col pk">id PK</span>
          <span class="db-col fk">user_id FK</span>
          <span class="db-col">name</span>
          <span class="db-col">amount</span>
          <span class="db-col">category</span>
          <span class="db-col">date</span>
          <span class="db-col">type</span>
        </div>
      </div>
      <div class="db-table">
        <div class="db-table-name">budgets</div>
        <div class="db-columns">
          <span class="db-col pk">id PK</span>
          <span class="db-col fk">user_id FK</span>
          <span class="db-col">name</span>
          <span class="db-col">amount</span>
          <span class="db-col">period</span>
        </div>
      </div>
      <div class="db-table">
        <div class="db-table-name">notes</div>
        <div class="db-columns">
          <span class="db-col pk">id PK</span>
          <span class="db-col fk">user_id FK</span>
          <span class="db-col">title</span>
          <span class="db-col">content</span>
          <span class="db-col">date</span>
          <span class="db-col">tag</span>
        </div>
      </div>
      <div class="db-table">
        <div class="db-table-name">goals</div>
        <div class="db-columns">
          <span class="db-col pk">id PK</span>
          <span class="db-col fk">user_id FK</span>
          <span class="db-col">title</span>
          <span class="db-col">target_amount</span>
          <span class="db-col">saved_amount</span>
          <span class="db-col">deadline</span>
        </div>
      </div>
    </div>
  </section>

  <div class="divider"></div>

  <!-- ═══ 8. FUNCTIONAL REQUIREMENTS ═══ -->
  <section class="section" id="functional">
    <div class="section-header">
      <span class="section-num">8</span>
      <h2>Functional Requirements</h2>
    </div>

    <div class="fr-group">
      <div class="fr-header">
        <span class="fr-id">FR-01</span>
        <h3>Transaction Management</h3>
      </div>
      <ul class="fr-list">
        <li>Add new transactions with name, amount, type (income/expense), category, and date</li>
        <li>View all transactions with filtering by date range, category, and type</li>
        <li>Edit any field of an existing transaction</li>
        <li>Delete a transaction with confirmation prompt</li>
        <li>Auto-categorize transactions based on configurable keyword rules</li>
      </ul>
    </div>

    <div class="fr-group">
      <div class="fr-header">
        <span class="fr-id">FR-02</span>
        <h3>Budget Management</h3>
      </div>
      <ul class="fr-list">
        <li>Define a monthly budget per category with a monetary cap</li>
        <li>Display current spending vs budget limit in real time</li>
        <li>Trigger visual alert when spending reaches 80% of a budget limit</li>
        <li>Full CRUD on budget entries</li>
      </ul>
    </div>

    <div class="fr-group">
      <div class="fr-header">
        <span class="fr-id">FR-03</span>
        <h3>Dashboard &amp; Reports</h3>
      </div>
      <ul class="fr-list">
        <li>Display total income, total expenses, and net balance for the current month</li>
        <li>Pie chart of spending by category</li>
        <li>Bar/line chart showing monthly spending trends</li>
        <li>Export financial reports to PDF or Excel format</li>
      </ul>
    </div>

    <div class="fr-group">
      <div class="fr-header">
        <span class="fr-id">FR-04</span>
        <h3>Notes &amp; Goals</h3>
      </div>
      <ul class="fr-list">
        <li>Create notes with title, content, date, and optional tags</li>
        <li>Define savings goals with target amount and deadline</li>
        <li>Calculate and display percentage completion of each goal</li>
        <li>In-app reminders for approaching goal deadlines</li>
      </ul>
    </div>
  </section>

  <div class="divider"></div>

  <!-- ═══ 9. NON-FUNCTIONAL ═══ -->
  <section class="section" id="nonfunctional">
    <div class="section-header">
      <span class="section-num">9</span>
      <h2>Non-Functional Requirements</h2>
    </div>

    <div class="table-wrap">
      <table>
        <thead>
          <tr><th>ID</th><th>Category</th><th>Requirement</th></tr>
        </thead>
        <tbody>
          <tr><td>NFR-01</td><td>Performance</td><td>Launch in under 3 seconds; GUI responses under 200ms</td></tr>
          <tr><td>NFR-02</td><td>Reliability</td><td>No data loss or corruption; atomic writes via DB transactions</td></tr>
          <tr><td>NFR-03</td><td>Usability</td><td>Core tasks completable within 5 minutes without documentation</td></tr>
          <tr><td>NFR-04</td><td>Security</td><td>Passwords hashed with bcrypt; no plaintext credentials</td></tr>
          <tr><td>NFR-05</td><td>Maintainability</td><td>Unit test coverage &gt; 80%; docstrings on all public methods</td></tr>
          <tr><td>NFR-06</td><td>Portability</td><td>Runs on Windows 10+, macOS 12+, Ubuntu 20.04+</td></tr>
          <tr><td>NFR-07</td><td>Scalability</td><td>Repository layer swappable with zero service-layer changes</td></tr>
          <tr><td>NFR-08</td><td>Data Integrity</td><td>Foreign key constraints enforced; cascading deletes configured</td></tr>
        </tbody>
      </table>
    </div>
  </section>

  <div class="divider"></div>

  <!-- ═══ 10. HOW TO RUN ═══ -->
  <section class="section" id="howtorun">
    <div class="section-header">
      <span class="section-num">10</span>
      <h2>How to Run</h2>
    </div>
    <p>Prerequisites: Python 3.10+ and pip package manager.</p>

    <div class="steps">
      <div class="step">
        <div class="step-num">1</div>
        <div class="step-content">
          <h4>Clone the repository</h4>
          <code class="cmd">git clone https://github.com/anasemadanas/Expense_Track.git
cd Expense_Track</code>
        </div>
      </div>
      <div class="step">
        <div class="step-num">2</div>
        <div class="step-content">
          <h4>Install dependencies</h4>
          <code class="cmd">pip install -r requirements.txt</code>
        </div>
      </div>
      <div class="step">
        <div class="step-num">3</div>
        <div class="step-content">
          <h4>Run the application</h4>
          <code class="cmd">python money_manager/main.py</code>
        </div>
      </div>
    </div>
  </section>

  <div class="divider"></div>

  <!-- ═══ 11. FUTURE ═══ -->
  <section class="section" id="future">
    <div class="section-header">
      <span class="section-num">11</span>
      <h2>Future Enhancements</h2>
    </div>
    <div class="future-grid">
      <div class="future-card">
        <h4>📱 Android App</h4>
        <p>Kivy or Flutter with shared Python backend</p>
      </div>
      <div class="future-card">
        <h4>🌐 Web App</h4>
        <p>FastAPI + React</p>
      </div>
      <div class="future-card">
        <h4>☁️ Cloud Sync</h4>
        <p>Firebase / Supabase</p>
      </div>
      <div class="future-card">
        <h4>📑 PDF/Excel Reports</h4>
        <p>Scheduled report generation with embedded charts</p>
      </div>
      <div class="future-card">
        <h4>🤖 AI-based Insights</h4>
        <p>Automatic transaction classification and spending suggestions</p>
      </div>
      <div class="future-card">
        <h4>👨‍👩‍👧‍👦 Multi-User / Family Mode</h4>
        <p>Role-based access (admin/viewer) for household budgets</p>
      </div>
    </div>
  </section>

  <div class="divider"></div>

  <!-- ═══ 12. CONSTRAINTS ═══ -->
  <section class="section" id="constraints">
    <div class="section-header">
      <span class="section-num">12</span>
      <h2>Constraints &amp; Assumptions</h2>
    </div>
    <div class="split-grid">
      <div>
        <h3>🔒 Constraints</h3>
        <ul class="constraint-list">
          <li>v1.0 supports a single local user; multi-user deferred to v2.0</li>
          <li>GUI built with Python-native libraries (PyQt5 or Tkinter) only</li>
          <li>Data stored locally in SQLite; cloud backup is optional</li>
          <li>No internet connectivity required for core functionality</li>
          <li>Distributed as a self-contained executable via PyInstaller</li>
        </ul>
      </div>
      <div>
        <h3>💡 Assumptions</h3>
        <ul class="constraint-list">
          <li>Users have basic familiarity with personal finance concepts</li>
          <li>Development environment uses Python 3.10+ with pip</li>
          <li>SQLite bundled with Python is sufficient for single-user workload</li>
          <li>Monetary values stored as REAL with 2-decimal precision at the app layer</li>
          <li>Dates stored as ISO 8601 strings (YYYY-MM-DD)</li>
        </ul>
      </div>
    </div>
  </section>

  <div class="divider"></div>

  <!-- ═══ 13. CONTRIBUTING ═══ -->
  <section class="section" id="contributing">
    <div class="section-header">
      <span class="section-num">13</span>
      <h2>Contributing</h2>
    </div>
    <p>Contributions are welcome! Please ensure your code follows the SOLID principles and the 3-Tier architecture outlined above.</p>
    <div class="contrib-steps">
      <div class="contrib-step"><span class="cs-num">1</span> Fork the repository</div>
      <div class="contrib-step"><span class="cs-num">2</span> Create feature branch</div>
      <div class="contrib-step"><span class="cs-num">3</span> Commit your changes</div>
      <div class="contrib-step"><span class="cs-num">4</span> Push to branch</div>
      <div class="contrib-step"><span class="cs-num">5</span> Open a Pull Request</div>
    </div>
  </section>

  <div class="divider"></div>

  <!-- ═══ 14. LICENSE ═══ -->
  <section class="section" id="license">
    <div class="section-header">
      <span class="section-num">14</span>
      <h2>License</h2>
    </div>
    <p>This project is licensed under the MIT License — see the <a href="LICENSE" style="color:var(--accent-blue);text-decoration:none;border-bottom:1px solid var(--accent-blue)">LICENSE</a> file for details.</p>
  </section>

</main>

<!-- ═══ FOOTER ═══ -->
<footer class="footer">
  <div class="container">
    <p>Built with ❤️ using Python &bull; Designed with SOLID principles in mind</p>
  </div>
</footer>

</body>
</html>
