"""P5 civic-space content prototype for the Louvre Abu Dhabi rebuild."""
from pathlib import Path

from pptx_designer import Presentation, svg_chart
from pptx_designer.tools.images import cover_image
from pptx_designer.tools.shapes import rect
from pptx_designer.tools.text import text


ROOT = Path(__file__).resolve().parents[2]
CASE = ROOT / "examples" / "new_examplex" / "louvre_abudhabi"
ASSETS = CASE / "assets" / "images"
OUT = Path(__file__).resolve().parent / "louvre_abudhabi_p05_visual_baseline.pptx"
C = {
    "paper": "#F4F3ED", "ink": "#15232D", "muted": "#596973",
    "pale": "#B7C1C2", "gold": "#B18C58", "line": "#A3AFB1",
}

WATER_TRACE = r'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 180">
  <g fill="none" stroke="#AEBCC0" stroke-width="1.1">
    <path d="M18 26H482M72 74H428M128 122H372"/>
  </g>
  <g fill="none" stroke="#B18C58" stroke-width="1.1">
    <path d="M18 26L128 164M482 26L372 164"/>
  </g>
  <g fill="#B18C58"><circle cx="18" cy="26" r="4"/><circle cx="482" cy="26" r="4"/></g>
  <g fill="#596973"><circle cx="128" cy="164" r="3"/><circle cx="372" cy="164" r="3"/></g>
</svg>'''


def tx(slide, x, y, w, h, value, size, color, font="Arial", bold=False, align=None):
    kwargs = dict(font_size=size, color=color, font_name=font, bold=bold, C=C)
    if align:
        kwargs["align"] = align
    return text(slide, x, y, w, h, value, **kwargs)


def main():
    image = ASSETS / "louvre_abudhabi_water_gallery_mediaoffice.jpg"
    if not image.exists():
        raise FileNotFoundError(image)
    prs = Presentation()
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    rect(slide, 0, 0, 13.333, 7.5, fill=C["paper"], C=C)
    cover_image(slide, 0.66, 0.56, 4.42, 6.38, str(image))
    rect(slide, 5.34, 0.56, 0.024, 6.38, fill=C["gold"], C=C)

    tx(slide, 5.82, 0.70, 2.30, 0.14, "04  /  CIVIC INTERIOR", 7.2, C["muted"], "Arial Narrow", True)
    rect(slide, 5.82, 1.15, 0.72, 0.023, fill=C["gold"], C=C)
    tx(slide, 5.82, 1.48, 5.80, 1.06, "WATER\nAS PUBLIC ROOM", 31, C["ink"], "Georgia")
    tx(slide, 5.86, 2.92, 5.55, 0.58, "Paths cross the water beneath the dome,\nturning the museum into a walkable urban room.", 12, C["ink"], "Arial")
    tx(slide, 5.86, 3.78, 5.32, 0.52, "The visitor does not move around a single object.\nThe visitor moves through a sequence of thresholds.", 12, C["muted"], "Arial")

    rect(slide, 5.86, 4.68, 5.72, 0.018, fill=C["line"], C=C)
    tx(slide, 5.86, 4.94, 0.42, 0.18, "01", 10, C["gold"], "Consolas", True)
    tx(slide, 6.42, 4.91, 2.20, 0.18, "ARRIVAL", 9.5, C["ink"], "Arial Narrow", True)
    tx(slide, 6.42, 5.20, 2.08, 0.26, "land → water → threshold", 11.5, C["muted"], "Arial")
    tx(slide, 8.86, 4.94, 0.42, 0.18, "02", 10, C["gold"], "Consolas", True)
    tx(slide, 9.42, 4.91, 2.20, 0.18, "PAUSE", 9.5, C["ink"], "Arial Narrow", True)
    tx(slide, 9.42, 5.20, 2.08, 0.26, "shade → water → room", 11.5, C["muted"], "Arial")
    svg_chart(slide, WATER_TRACE, x=6.02, y=5.72, w=5.20, h=1.06, C=C)
    tx(slide, 5.86, 6.96, 3.80, 0.14, "SOURCE  /  LOUVRE ABU DHABI — ARCHITECTURE", 6.4, C["muted"], "Arial Narrow", True)
    tx(slide, 11.98, 6.70, 0.64, 0.48, "05", 21, C["pale"], "Georgia", False, "right")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    prs.save(str(OUT))
    print(OUT)


if __name__ == "__main__":
    main()
