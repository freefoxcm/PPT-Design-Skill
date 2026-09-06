"""P7 spatial-sequence prototype for the Louvre Abu Dhabi rebuild."""
from pathlib import Path

from pptx_designer import Presentation
from pptx_designer.tools.images import cover_image
from pptx_designer.tools.shapes import rect
from pptx_designer.tools.text import text


ROOT = Path(__file__).resolve().parents[2]
CASE = ROOT / "examples" / "new_examplex" / "louvre_abudhabi"
ASSETS = CASE / "assets" / "images"
OUT = Path(__file__).resolve().parent / "louvre_abudhabi_p07_visual_baseline.pptx"
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
    images = [
        ASSETS / "louvre_abudhabi_rain_of_light.jpg",
        ASSETS / "louvre_abudhabi_aerial_expedia.jpg",
        ASSETS / "louvre_abudhabi_water_gallery_mediaoffice.jpg",
    ]
    for image in images:
        if not image.exists():
            raise FileNotFoundError(image)
    prs = Presentation()
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    rect(slide, 0, 0, 13.333, 7.5, fill=C["night"], C=C)
    rect(slide, 0.66, 0.58, 0.74, 0.023, fill=C["gold"], C=C)
    tx(slide, 0.66, 0.86, 2.50, 0.14, "06  /  SPATIAL SEQUENCE", 7.2, C["silver"], "Arial Narrow", True)
    tx(slide, 0.66, 1.22, 6.90, 0.50, "WALK  /  PAUSE  /  RETURN", 27, C["white"], "Georgia")
    tx(slide, 10.02, 1.38, 2.52, 0.14, "A MUSEUM DESIGNED AS A JOURNEY", 6.8, C["gold"], "Arial Narrow", True, "right")
    rect(slide, 0.66, 1.88, 12.01, 0.022, fill=C["gold"], C=C)

    xs = [0.66, 4.50, 8.34]
    labels = [("01", "FILTERED DAYLIGHT"), ("02", "CITY + SEA"), ("03", "CIVIC WATER ROOM")]
    for x, image, (num, label) in zip(xs, images, labels):
        cover_image(slide, x, 2.20, 3.60, 3.74, str(image))
        tx(slide, x, 6.20, 3.30, 0.16, f"{num}  /  {label}", 7.0, C["silver"], "Arial Narrow", True)

    tx(slide, 0.70, 6.72, 4.35, 0.18, "ARRIVE THROUGH SHADE", 8.0, C["gold"], "Arial Narrow", True)
    tx(slide, 4.54, 6.72, 4.35, 0.18, "ORIENT FROM ABOVE", 8.0, C["gold"], "Arial Narrow", True)
    tx(slide, 8.38, 6.72, 3.60, 0.18, "RETURN TO WATER", 8.0, C["gold"], "Arial Narrow", True)
    tx(slide, 0.70, 7.08, 4.60, 0.14, "SOURCE  /  LOUVRE ABU DHABI — ARCHITECTURE", 6.4, C["silver"], "Arial Narrow", True)
    tx(slide, 12.02, 6.76, 0.62, 0.48, "07", 21, C["muted"], "Georgia", False, "right")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    prs.save(str(OUT))
    print(OUT)


if __name__ == "__main__":
    main()
