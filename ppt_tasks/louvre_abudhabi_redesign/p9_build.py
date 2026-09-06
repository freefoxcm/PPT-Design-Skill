"""P9 architectural-position prototype for the Louvre Abu Dhabi rebuild."""
from pathlib import Path

from pptx_designer import Presentation, svg_chart
from pptx_designer.tools.shapes import rect
from pptx_designer.tools.text import text


ROOT = Path(__file__).resolve().parents[2]
CASE = ROOT / "examples" / "new_examplex" / "louvre_abudhabi"
OUT = Path(__file__).resolve().parent / "louvre_abudhabi_p09_visual_baseline.pptx"
C = {
    "night": "#11242E", "white": "#F6F6F1", "silver": "#B3C1C4",
    "muted": "#6E8187", "gold": "#B18C58", "line": "#49636C",
}

STAR_FIELD = r'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 560">
  <g fill="none" stroke="#38535D" stroke-width="1">
    <path d="M300 28L445 88L505 230L445 372L300 432L155 372L95 230L155 88Z"/>
    <path d="M720 128L840 178L890 298L840 418L720 468L600 418L550 298L600 178Z"/>
    <path d="M300 28V432M95 230H505M720 128V468M550 298H890"/>
  </g>
  <g fill="#536D75"><circle cx="400" cy="28" r="3"/><circle cx="605" cy="230" r="3"/><circle cx="680" cy="128" r="3"/><circle cx="850" cy="298" r="3"/></g>
</svg>'''


def tx(slide, x, y, w, h, value, size, color, font="Arial", bold=False, align=None):
    kwargs = dict(font_size=size, color=color, font_name=font, bold=bold, C=C)
    if align:
        kwargs["align"] = align
    return text(slide, x, y, w, h, value, **kwargs)


def main():
    prs = Presentation()
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    rect(slide, 0, 0, 13.333, 7.5, fill=C["night"], C=C)
    svg_chart(slide, STAR_FIELD, x=5.28, y=0.54, w=7.28, h=4.36, C=C)
    rect(slide, 0.66, 0.60, 0.74, 0.023, fill=C["gold"], C=C)
    tx(slide, 0.66, 0.88, 3.10, 0.14, "08  /  ARCHITECTURAL POSITION", 7.2, C["silver"], "Arial Narrow", True)
    tx(slide, 0.66, 1.46, 5.40, 1.78, "A WELCOMING WORLD\nOF LIGHT, SHADOW,\nREFLECTION AND CALM.", 29, C["white"], "Georgia")
    tx(slide, 0.70, 3.76, 4.42, 0.62, "A museum-city that belongs to its geography\nwithout becoming a literal interpretation of it.", 12, C["silver"], "Arial")
    rect(slide, 0.70, 5.04, 4.18, 0.018, fill=C["line"], C=C)

    terms = [
        ("01", "LIGHT", "reveals movement"),
        ("02", "SHADOW", "makes room for pause"),
        ("03", "REFLECTION", "joins land and sea"),
    ]
    for i, (num, label, detail) in enumerate(terms):
        y = 5.30 + i * 0.48
        tx(slide, 0.70, y, 0.44, 0.18, num, 9.5, C["gold"], "Consolas", True)
        tx(slide, 1.28, y - 0.02, 1.50, 0.18, label, 9.5, C["white"], "Arial Narrow", True)
        tx(slide, 2.90, y - 0.02, 1.80, 0.18, detail, 11.5, C["silver"], "Arial")

    tx(slide, 0.70, 7.05, 4.35, 0.14, "SOURCE  /  LOUVRE ABU DHABI — ARCHITECTURE", 6.4, C["silver"], "Arial Narrow", True)
    tx(slide, 12.02, 6.76, 0.62, 0.48, "09", 21, C["muted"], "Georgia", False, "right")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    prs.save(str(OUT))
    print(OUT)


if __name__ == "__main__":
    main()
