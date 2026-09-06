"""P4 urban-scale content prototype for the Louvre Abu Dhabi rebuild."""
from pathlib import Path

from pptx_designer import Presentation
from pptx_designer.tools.images import cover_image
from pptx_designer.tools.shapes import rect
from pptx_designer.tools.text import text


ROOT = Path(__file__).resolve().parents[2]
CASE = ROOT / "examples" / "new_examplex" / "louvre_abudhabi"
ASSETS = CASE / "assets" / "images"
OUT = Path(__file__).resolve().parent / "louvre_abudhabi_p04_visual_baseline.pptx"
C = {
    "night": "#11242E", "white": "#F6F6F1", "silver": "#B3C1C4",
    "muted": "#6E8187", "gold": "#B18C58", "line": "#49636C",
}


def tx(slide, x, y, w, h, value, size, color, font="Arial", bold=False, align=None):
    kwargs = dict(font_size=size, color=color, font_name=font, bold=bold, C=C)
    if align:
        kwargs["align"] = align
    return text(slide, x, y, w, h, value, **kwargs)


def main():
    image = ASSETS / "louvre_abudhabi_aerial_expedia.jpg"
    if not image.exists():
        raise FileNotFoundError(image)
    prs = Presentation()
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    rect(slide, 0, 0, 13.333, 7.5, fill=C["night"], C=C)
    rect(slide, 0.66, 0.58, 0.74, 0.023, fill=C["gold"], C=C)
    tx(slide, 0.66, 0.86, 2.60, 0.14, "03  /  URBAN FIGURE", 7.2, C["silver"], "Arial Narrow", True)
    tx(slide, 0.66, 1.18, 7.60, 0.52, "A MUSEUM-CITY  /  IN THE SEA", 26, C["white"], "Georgia")
    tx(slide, 10.20, 1.35, 2.35, 0.14, "SAADIYAT ISLAND · ABU DHABI", 6.8, C["silver"], "Arial Narrow", True, "right")
    rect(slide, 0.66, 1.92, 12.01, 0.022, fill=C["gold"], C=C)
    cover_image(slide, 0.66, 2.18, 12.01, 3.80, str(image))
    rect(slide, 0.66, 6.14, 12.01, 0.022, fill=C["gold"], C=C)

    tx(slide, 0.70, 6.39, 2.10, 0.18, "55", 23, C["white"], "Arial")
    tx(slide, 1.45, 6.47, 1.70, 0.14, "BUILDINGS", 7.0, C["gold"], "Arial Narrow", True)
    tx(slide, 4.18, 6.39, 2.10, 0.18, "23", 23, C["white"], "Arial")
    tx(slide, 4.92, 6.47, 1.70, 0.14, "GALLERIES", 7.0, C["gold"], "Arial Narrow", True)
    tx(slide, 7.66, 6.40, 4.20, 0.38, "The dome does not sit on the city;\nit gathers a city beneath it.", 12, C["silver"], "Arial")
    tx(slide, 0.70, 7.08, 4.40, 0.14, "SOURCE  /  LOUVRE ABU DHABI — ARCHITECTURE", 6.4, C["silver"], "Arial Narrow", True)
    tx(slide, 12.02, 6.76, 0.62, 0.48, "04", 21, C["muted"], "Georgia", False, "right")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    prs.save(str(OUT))
    print(OUT)


if __name__ == "__main__":
    main()
