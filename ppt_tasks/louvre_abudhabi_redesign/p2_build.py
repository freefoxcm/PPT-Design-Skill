"""P2 content prototype for the Louvre Abu Dhabi visual-baseline rebuild."""
from pathlib import Path

from pptx_designer import Presentation, svg_chart
from pptx_designer.tools.images import cover_image
from pptx_designer.tools.shapes import rect
from pptx_designer.tools.text import text


ROOT = Path(__file__).resolve().parents[2]
CASE = ROOT / "examples" / "new_examplex" / "louvre_abudhabi"
ASSETS = CASE / "assets" / "images"
OUT = Path(__file__).resolve().parent / "louvre_abudhabi_p02_visual_baseline.pptx"
C = {
    "paper": "#F4F3ED",
    "ink": "#15232D",
    "muted": "#596973",
    "pale": "#B7C1C2",
    "gold": "#B18C58",
    "line": "#A3AFB1",
}

LIGHT_TRACE = r'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 180">
  <g fill="none" stroke="#9DA9AB" stroke-width="1.1">
    <path d="M18 24H210M42 50H188M66 76H166M90 102H142"/>
    <path d="M18 24L90 158M210 24L142 158"/>
  </g>
  <g fill="#B18C58"><circle cx="18" cy="24" r="3.4"/><circle cx="210" cy="24" r="3.4"/></g>
  <g fill="#596973"><circle cx="90" cy="158" r="2.7"/><circle cx="142" cy="158" r="2.7"/></g>
</svg>'''


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
    cover_image(slide, 4.20, 0, 9.133, 7.5, str(image))
    rect(slide, 4.13, 0, 0.026, 7.5, fill=C["gold"], C=C)

    tx(slide, 0.66, 0.66, 3.15, 0.14, "01  /  SPATIAL PHENOMENON", 7.2, C["muted"], "Arial Narrow", True)
    rect(slide, 0.66, 1.24, 0.72, 0.023, fill=C["gold"], C=C)
    tx(slide, 0.66, 1.62, 3.20, 1.10, "RAIN\nOF LIGHT", 30, C["ink"], "Georgia")
    tx(slide, 0.68, 3.05, 3.12, 0.60, "BENEATH A POROUS DOME,\nDAYLIGHT BECOMES A\nCULTURAL MEDIUM.", 10.5, C["ink"], "Arial Narrow", True)
    tx(slide, 0.68, 3.88, 3.15, 0.62, "The roof does not simply shelter the museum;\nit filters the sky into a moving field of light.", 12, C["muted"], "Arial")

    rect(slide, 0.68, 4.78, 2.92, 0.018, fill=C["line"], C=C)
    tx(slide, 0.68, 5.02, 0.36, 0.18, "01", 10, C["gold"], "Consolas", True)
    tx(slide, 1.18, 4.98, 2.34, 0.18, "PERFORATED CANOPY", 9.5, C["ink"], "Arial Narrow", True)
    tx(slide, 1.18, 5.25, 2.10, 0.42, "Four steel layers break the\nroof into apertures.", 12, C["muted"], "Arial")
    tx(slide, 0.68, 5.88, 0.36, 0.18, "02", 10, C["gold"], "Consolas", True)
    tx(slide, 1.18, 5.84, 2.34, 0.18, "FILTERED DAYLIGHT", 9.5, C["ink"], "Arial Narrow", True)
    tx(slide, 1.18, 6.12, 2.10, 0.42, "Sunlight becomes a moving\nfield across the floor.", 12, C["muted"], "Arial")

    svg_chart(slide, LIGHT_TRACE, x=2.88, y=5.62, w=1.10, h=0.98, C=C)
    tx(slide, 0.70, 7.05, 2.80, 0.14, "SOURCE  /  LOUVRE ABU DHABI — ARCHITECTURE", 6.4, C["muted"], "Arial Narrow", True)
    tx(slide, 12.02, 6.76, 0.62, 0.48, "02", 21, C["pale"], "Georgia", False, "right")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    prs.save(str(OUT))
    print(OUT)


if __name__ == "__main__":
    main()
