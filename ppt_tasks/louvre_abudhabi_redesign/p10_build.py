"""P10 closing-coda prototype for the Louvre Abu Dhabi rebuild."""
from pathlib import Path

from pptx_designer import Presentation, svg_chart
from pptx_designer.tools.images import cover_image
from pptx_designer.tools.shapes import rect
from pptx_designer.tools.text import text


ROOT = Path(__file__).resolve().parents[2]
CASE = ROOT / "examples" / "new_examplex" / "louvre_abudhabi"
ASSETS = CASE / "assets" / "images"
OUT = Path(__file__).resolve().parent / "louvre_abudhabi_p10_visual_baseline.pptx"
C = {
    "night": "#11242E", "white": "#F6F6F1", "silver": "#B3C1C4",
    "muted": "#6E8187", "gold": "#B18C58", "line": "#49636C",
}

LIGHT_ROUTE = r'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 230">
  <g fill="none" stroke="#6D858D" stroke-width="1.15">
    <path d="M20 28H740M110 102H650M200 176H560"/>
  </g>
  <g fill="none" stroke="#B18C58" stroke-width="1.1"><path d="M20 28L200 214M740 28L560 214"/></g>
  <g fill="#B18C58"><circle cx="20" cy="28" r="4"/><circle cx="740" cy="28" r="4"/></g>
  <g fill="#6D858D"><circle cx="200" cy="214" r="3"/><circle cx="560" cy="214" r="3"/></g>
</svg>'''


def tx(slide, x, y, w, h, value, size, color, font="Arial", bold=False, align=None):
    kwargs = dict(font_size=size, color=color, font_name=font, bold=bold, C=C)
    if align:
        kwargs["align"] = align
    return text(slide, x, y, w, h, value, **kwargs)


def main():
    image = ASSETS / "louvre_abudhabi_night_metalocus.jpg"
    if not image.exists():
        raise FileNotFoundError(image)
    prs = Presentation()
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    rect(slide, 0, 0, 13.333, 7.5, fill=C["night"], C=C)
    rect(slide, 0.66, 0.60, 0.74, 0.023, fill=C["gold"], C=C)
    tx(slide, 0.66, 0.88, 2.50, 0.14, "09  /  CODA", 7.2, C["silver"], "Arial Narrow", True)
    cover_image(slide, 0.66, 1.48, 7.42, 4.18, str(image))
    rect(slide, 0.66, 5.98, 7.42, 0.022, fill=C["gold"], C=C)
    tx(slide, 0.70, 6.25, 3.50, 0.14, "LOUVRE ABU DHABI  /  SAADIYAT ISLAND", 6.8, C["silver"], "Arial Narrow", True)

    tx(slide, 8.72, 1.56, 3.70, 1.50, "LIGHT.\nWATER.\nCITY.", 35, C["white"], "Georgia")
    tx(slide, 8.76, 3.78, 3.34, 0.54, "A common sky turns architecture\ninto a public cultural landscape.", 12, C["silver"], "Arial")
    rect(slide, 8.76, 4.76, 3.52, 0.018, fill=C["line"], C=C)
    tx(slide, 8.76, 5.02, 3.30, 0.22, "THE CASE CLOSES ON A RELATIONSHIP", 8.0, C["gold"], "Consolas", True)
    tx(slide, 8.76, 5.42, 3.22, 0.48, "A landmark becomes civic when its\nlight, water and paths remain shared.", 12, C["white"], "Arial")
    svg_chart(slide, LIGHT_ROUTE, x=8.68, y=6.02, w=3.52, h=0.86, C=C)
    tx(slide, 0.70, 7.05, 4.25, 0.14, "SOURCE  /  LOUVRE ABU DHABI — ARCHITECTURE", 6.4, C["silver"], "Arial Narrow", True)
    tx(slide, 12.02, 6.76, 0.62, 0.48, "10", 21, C["muted"], "Georgia", False, "right")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    prs.save(str(OUT))
    print(OUT)


if __name__ == "__main__":
    main()
