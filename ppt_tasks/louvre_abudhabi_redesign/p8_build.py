"""P8 material-logic prototype for the Louvre Abu Dhabi rebuild."""
from pathlib import Path

from pptx_designer import Presentation
from pptx_designer.tools.images import cover_image
from pptx_designer.tools.shapes import rect
from pptx_designer.tools.text import text


ROOT = Path(__file__).resolve().parents[2]
CASE = ROOT / "examples" / "new_examplex" / "louvre_abudhabi"
ASSETS = CASE / "assets" / "images"
OUT = Path(__file__).resolve().parent / "louvre_abudhabi_p08_visual_baseline.pptx"
C = {
    "paper": "#F4F3ED", "ink": "#16252D", "muted": "#586A73",
    "gold": "#B18C58", "line": "#A3AFB1", "silver": "#B7C1C2",
}


def tx(slide, x, y, w, h, value, size, color, font="Arial", bold=False, align=None):
    kwargs = dict(font_size=size, color=color, font_name=font, bold=bold, C=C)
    if align:
        kwargs["align"] = align
    return text(slide, x, y, w, h, value, **kwargs)


def main():
    image = ASSETS / "louvre_abudhabi_rain_of_light.jpg"
    if not image.exists():
        raise FileNotFoundError(image)
    prs = Presentation()
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    rect(slide, 0, 0, 13.333, 7.5, fill=C["paper"], C=C)
    rect(slide, 0.66, 0.54, 0.74, 0.023, fill=C["gold"], C=C)
    tx(slide, 0.66, 0.82, 2.70, 0.14, "07  /  MATERIAL LOGIC", 7.2, C["muted"], "Arial Narrow", True)
    tx(slide, 10.05, 0.84, 2.50, 0.14, "SKY  /  STEEL  /  GROUND", 6.8, C["gold"], "Arial Narrow", True, "right")
    cover_image(slide, 0.66, 1.18, 12.01, 3.58, str(image))
    rect(slide, 0.66, 4.76, 12.01, 0.022, fill=C["gold"], C=C)

    tx(slide, 0.70, 5.10, 5.20, 0.54, "MATERIAL IS A FILTER", 28, C["ink"], "Georgia")
    tx(slide, 0.70, 5.86, 5.30, 0.48, "Steel, aluminium and patterned voids work as a single\noptical instrument between sky and ground.", 12, C["ink"], "Arial")

    rect(slide, 7.22, 5.06, 0.024, 1.55, fill=C["gold"], C=C)
    tx(slide, 7.54, 5.04, 2.55, 0.30, "8 LAYERS", 22, C["ink"], "Arial")
    tx(slide, 7.58, 5.43, 4.36, 0.18, "4 STAINLESS STEEL  /  4 ALUMINIUM", 7.0, C["muted"], "Arial Narrow", True)
    tx(slide, 7.54, 5.86, 4.65, 0.48, "Structure becomes atmosphere:\nopenings admit light without losing shade.", 12, C["muted"], "Arial")
    tx(slide, 0.70, 6.98, 4.30, 0.14, "SOURCE  /  LOUVRE ABU DHABI — ARCHITECTURE", 6.4, C["muted"], "Arial Narrow", True)
    tx(slide, 12.02, 6.76, 0.62, 0.48, "08", 21, C["silver"], "Georgia", False, "right")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    prs.save(str(OUT))
    print(OUT)


if __name__ == "__main__":
    main()
