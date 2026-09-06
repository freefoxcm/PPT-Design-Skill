"""P1 cover prototype for the Louvre Abu Dhabi visual-baseline rebuild."""
from pathlib import Path

from pptx_designer import Presentation, svg_chart
from pptx_designer.tools.images import cover_image
from pptx_designer.tools.shapes import rect
from pptx_designer.tools.text import text


ROOT = Path(__file__).resolve().parents[2]
CASE = ROOT / "examples" / "new_examplex" / "louvre_abudhabi"
ASSETS = CASE / "assets" / "images"
OUT = Path(__file__).resolve().parent / "louvre_abudhabi_p01_visual_baseline.pptx"
C = {
    "night": "#11242E",
    "white": "#F6F6F1",
    "silver": "#AEBCC0",
    "gold": "#B18C58",
    "faint": "#49636C",
}

STAR_FIELD = r'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 780 420">
  <g fill="none" stroke="#49636C" stroke-width="1.2">
    <path d="M380 24L535 88L600 240L535 392L380 456L225 392L160 240L225 88Z"/>
    <path d="M380 78L498 127L547 240L498 353L380 402L262 353L213 240L262 127Z"/>
    <path d="M380 24V456M160 240H600"/>
  </g>
  <g fill="none" stroke="#756545" stroke-width="1">
    <path d="M380 0V480M110 240H650"/>
  </g>
  <g fill="#B18C58"><circle cx="380" cy="24" r="4"/><circle cx="600" cy="240" r="3.5"/><circle cx="380" cy="456" r="4"/></g>
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
    cover_image(slide, 0, 2.42, 13.333, 4.18, str(image))

    rect(slide, 0.66, 0.56, 0.72, 0.024, fill=C["gold"], C=C)
    tx(slide, 0.66, 0.84, 4.0, 0.14, "CASE 04  /  ARCHITECTURAL DOSSIER", 7.2, C["silver"], "Arial Narrow", True)
    tx(slide, 0.66, 1.12, 5.60, 1.15, "LOUVRE\nABU DHABI", 40, C["white"], "Georgia")
    tx(slide, 5.12, 2.12, 2.45, 0.14, "JEAN NOUVEL  /  2017", 7.0, C["silver"], "Arial Narrow", True)
    svg_chart(slide, STAR_FIELD, x=8.22, y=0.28, w=4.12, h=1.92, C=C)
    rect(slide, 0.66, 6.83, 12.01, 0.022, fill=C["gold"], C=C)
    tx(slide, 0.70, 7.05, 4.20, 0.14, "SAADIYAT ISLAND  /  ABU DHABI, UAE", 6.8, C["silver"], "Arial Narrow", True)
    tx(slide, 8.15, 7.05, 3.55, 0.14, "MUSEUM-CITY  /  LIGHT  /  WATER", 6.5, C["silver"], "Arial Narrow", True, "right")
    tx(slide, 11.98, 6.94, 0.55, 0.32, "01", 20, C["silver"], "Georgia", False, "right")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    prs.save(str(OUT))
    print(OUT)


if __name__ == "__main__":
    main()
