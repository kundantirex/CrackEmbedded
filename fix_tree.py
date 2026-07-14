import os
import shutil
from pathlib import Path

base_dir = Path("/home/tirex/Downloads/Embedded_Learn/new/CrackEmbedded")
protocols_dir = base_dir / "protocols"
nested_protocols = protocols_dir / "protocols"

# Move directories to root
dirs_to_move = ["raspberry-pi", "rtos", "stm32", "yocto"]
for d in dirs_to_move:
    src = protocols_dir / d
    dst = base_dir / d
    if src.exists():
        shutil.move(str(src), str(dst))
        print(f"Moved {d} to root")

# Move files from nested protocols
if nested_protocols.exists():
    for item in nested_protocols.iterdir():
        dst = protocols_dir / item.name
        # If dst already exists, delete it first to allow move
        if dst.exists():
            dst.unlink()
        shutil.move(str(item), str(dst))
    
    # Try to remove nested protocols dir
    try:
        nested_protocols.rmdir()
        print("Removed nested protocols dir")
    except Exception as e:
        print(f"Could not remove nested protocols dir: {e}")

# Delete about.html if it exists
about_file = protocols_dir / "about.html"
if about_file.exists():
    about_file.unlink()
    print("Removed about.html")

# Boilerplate logic
def format_title(name):
    if name == "index":
        return "Overview"
    name = name.replace("-", " ")
    if name.lower() == "cpp":
        return "C++"
    if name.lower() == "rtos":
        return "RTOS"
    if name.lower() == "yocto":
        return "Yocto"
    if name.lower() == "mcq":
        return "MCQ"
    return name.title()

boilerplate = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} — Embedded Learning Hub</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg: #0B1120; --panel: #131C2E; --panel-2: #0F1726; --line: #1F2B41;
            --text: #E6EDF6; --muted: #8595AD; --ch1: #22D3EE; --ch2: #F5B841;
            --ch3: #4ADE80; --ch4: #A78BFA; --display: 'Space Grotesk', sans-serif;
            --mono: 'JetBrains Mono', monospace; --body: 'Inter', sans-serif;
        }}
        * {{ box-sizing: border-box; margin: 0; padding: 0 }}
        html {{ scroll-behavior: smooth }}
        body {{ background: var(--bg); color: var(--text); font-family: var(--body); line-height: 1.6; -webkit-font-smoothing: antialiased; overflow-x: hidden }}
        a {{ color: inherit; text-decoration: none }}
        .wrap {{ max-width: 1120px; margin: 0 auto; padding: 0 24px }}
        .banner {{ background: linear-gradient(120deg, #0B1120 0%, #13314A 55%, #1B4D63 100%); border-bottom: 1px solid var(--line); text-align: center; padding: 38px 24px 30px }}
        .banner h1 {{ font-family: var(--display); font-weight: 700; font-size: clamp(30px, 4.6vw, 46px); letter-spacing: -.5px }}
        .banner .tag {{ margin-top: 8px; font-family: var(--mono); font-size: clamp(12px, 1.6vw, 15px); color: #AFC6D6; letter-spacing: .5px }}
        .topnav {{ position: sticky; top: 0; z-index: 50; background: rgba(15, 24, 40, .94); backdrop-filter: blur(10px); border-bottom: 1px solid var(--line) }}
        .topnav .wrap {{ display: flex; flex-wrap: wrap; justify-content: center; gap: 2px; padding-top: 0; padding-bottom: 0 }}
        .topnav a {{ font-family: var(--mono); font-size: 14px; color: #C4D2E4; padding: 15px 18px; position: relative; transition: color .15s }}
        .topnav a:hover, .topnav a:focus-visible {{ color: #fff }}
        .sec {{ padding: 56px 0 }}
        .sec-head {{ display: flex; align-items: baseline; gap: 14px; margin-bottom: 30px }}
        .sec-head h2 {{ font-family: var(--display); font-size: 28px; font-weight: 600; letter-spacing: -.5px }}
        .sec-head .rule {{ flex: 1; height: 1px; background: var(--line) }}
        .content-box {{ background: var(--panel); border: 1px solid var(--line); border-radius: 12px; padding: 32px; min-height: 400px; display: flex; align-items: center; justify-content: center; flex-direction: column; text-align: center; }}
        .content-box h3 {{ font-family: var(--display); font-size: 24px; color: var(--ch1); margin-bottom: 12px; }}
        .content-box p {{ color: var(--muted); max-width: 500px; }}
        footer {{ border-top: 1px solid var(--line); padding: 36px 0; margin-top: 30px; font-family: var(--mono); font-size: 13px; color: var(--muted) }}
        .foot {{ display: flex; justify-content: space-between; flex-wrap: wrap; gap: 16px }}
        footer a:hover {{ color: var(--ch1) }}
    </style>
</head>
<body>
    <div class="banner">
        <h1>{title}</h1>
        <div class="tag">{category} Module</div>
    </div>
    <nav class="topnav">
        <div class="wrap">
            <a href="{prefix}index.html">Home</a>
            <a href="{prefix}c/index.html">C</a>
            <a href="{prefix}embedded-c/index.html">Embedded C</a>
            <a href="{prefix}cpp/index.html">C++</a>
            <a href="{prefix}protocols.html">Protocols</a>
            <a href="{prefix}linux/index.html">Linux</a>
            <a href="{prefix}rtos/index.html">RTOS</a>
            <a href="{prefix}mcq/embedded-c.html">MCQs</a>
            <a href="{prefix}interview/embedded.html">Interview</a>
        </div>
    </nav>
    <section class="sec wrap">
        <div class="sec-head">
            <h2>{title} Overview</h2><span class="rule"></span>
        </div>
        <div class="content-box">
            <h3>Coming Soon</h3>
            <p>Detailed tutorials, code snippets, and interview questions for <strong>{title}</strong> will be added here shortly.</p>
        </div>
    </section>
    <footer class="wrap">
        <div class="foot">
            <span>© 2026 CrackEmbedded · Open Source Learning Platform</span>
            <span><a href="https://github.com/kundantirex" target="_blank" rel="noopener">github.com/kundantirex</a></span>
        </div>
    </footer>
</body>
</html>
"""

count = 0
for path in base_dir.rglob("*.html"):
    if "Coming Soon" in path.read_text(errors='ignore'):
        rel_path = path.relative_to(base_dir)
        
        # Calculate prefix to root
        depth = len(rel_path.parts) - 1
        prefix = "../" * depth
        
        file_name = path.stem
        title = format_title(file_name)
        
        if depth > 0:
            category = format_title(rel_path.parts[0])
        else:
            category = "General"
            
        if file_name == "index" and depth > 0:
            title = category
            
        content = boilerplate.format(title=title, category=category, prefix=prefix)
        
        path.write_text(content)
        count += 1

print(f"Successfully fixed file tree and repopulated {count} HTML files.")
