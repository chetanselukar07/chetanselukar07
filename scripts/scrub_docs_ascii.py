from pathlib import Path

p = Path("docs/index.html")
text = p.read_text(encoding="utf-8")
for old, new in {
    "\u00b7": "-",
    "\u2014": "-",
    "\u2013": "-",
    "\u2026": "...",
    "\u2019": "'",
    "\u2018": "'",
    "\u201c": '"',
    "\u201d": '"',
}.items():
    text = text.replace(old, new)
p.write_text(text, encoding="utf-8", newline="\n")
data = p.read_bytes()
print("nonascii", sum(1 for b in data if b > 127))
