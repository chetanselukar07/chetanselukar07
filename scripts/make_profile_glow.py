from PIL import Image, ImageDraw, ImageFilter
from pathlib import Path

src = Image.open("assets/images/profile.png").convert("RGBA")
w, h = src.size
side = min(w, h)
left = (w - side) // 2
top = max(0, (h - side) // 5)
if top + side > h:
    top = h - side
face = src.crop((left, top, left + side, top + side)).resize((520, 520), Image.Resampling.LANCZOS)

mask = Image.new("L", (520, 520), 0)
ImageDraw.Draw(mask).ellipse((0, 0, 519, 519), fill=255)
face_c = Image.new("RGBA", (520, 520), (0, 0, 0, 0))
face_c.paste(face, (0, 0))
face_c.putalpha(mask)

pad = 56
size = 520 + pad * 2
canvas = Image.new("RGBA", (size, size), (10, 14, 23, 255))
cx = cy = size // 2

glow = Image.new("RGBA", (size, size), (0, 0, 0, 0))
gd = ImageDraw.Draw(glow)
for i, a in [(48, 40), (40, 70), (32, 100)]:
    gd.ellipse((cx - 260 - i, cy - 260 - i, cx + 260 + i, cy + 260 + i), outline=(0, 240, 255, a), width=6)
for i, a in [(20, 90), (12, 120)]:
    gd.ellipse((cx - 260 - i, cy - 260 - i, cx + 260 + i, cy + 260 + i), outline=(57, 255, 20, a), width=4)
glow = glow.filter(ImageFilter.GaussianBlur(10))
canvas = Image.alpha_composite(canvas, glow)

d = ImageDraw.Draw(canvas)
d.ellipse((cx - 268, cy - 268, cx + 268, cy + 268), outline=(0, 240, 255, 220), width=3)
d.ellipse((cx - 258, cy - 258, cx + 258, cy + 258), outline=(57, 255, 20, 200), width=2)
d.ellipse((cx - 248, cy - 248, cx + 248, cy + 248), outline=(0, 240, 255, 120), width=1)

tick = 28
col = (57, 255, 20, 230)
for ox, oy, sx, sy in [
    (cx - 280, cy - 280, 1, 1),
    (cx + 280, cy - 280, -1, 1),
    (cx - 280, cy + 280, 1, -1),
    (cx + 280, cy + 280, -1, -1),
]:
    d.line([(ox, oy + sy * tick), (ox, oy), (ox + sx * tick, oy)], fill=col, width=3)

canvas.paste(face_c, (pad, pad), face_c)
out = Path("assets/images/profile-glow.png")
canvas.convert("RGB").save(out, "PNG", optimize=True)
print("saved", out, canvas.size, out.stat().st_size)
