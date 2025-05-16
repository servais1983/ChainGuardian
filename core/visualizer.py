def generate_html_timeline(events):
    filename = "timeline.html"
    with open(filename, "w") as f:
        f.write("<html><head><title>Incident Timeline</title></head><body><h1>ChainGuardian Timeline</h1><ul>")
        for e in events:
            f.write(f"<li><strong>{e['time']}</strong> — {e['desc']}<br><code>{str(e['log'])[:200]}</code></li>")
        f.write("</ul></body></html>")
    return filename