"""P1 cover prototype for the Vertical City Retrofit visual-baseline rebuild."""
from pathlib import Path

from pptx_designer import Presentation
from pptx_designer.tools.images import cover_image
from pptx_designer.tools.shapes import rect
from pptx_designer.tools.text import text


ROOT = Path(__file__).resolve().parents[2]
CASE = ROOT / "examples" / "new_examplex" / "vertical_city_retrofit"
OUT = Path(__file__).resolve().parent / "vertical_city_retrofit_p01_visual_baseline.pptx"
C = {
    "paper": "#F1EEE8", "graphite": "#20272B", "blue": "#1F6F8B",
    "muted": "#667278", "brick": "#B85C42",
}


def tx(slide, x, y, w, h, value, size, color, font="Arial", bold=False, align=None):
    kwargs = dict(font_size=size, color=color, font_name=font, bold=bold, C=C)
    if align:
        kwargs["align"] = align
    return text(slide, x, y, w, h, value, **kwargs)


def main():
    image = CASE / "assets" / "vertical_city_cover.png"
    if not image.exists():
        raise FileNotFoundError(image)
    prs = Presentation()
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    cover_image(slide, 0, 0, 13.333, 7.5, str(image))
    rect(slide, 0.66, 0.78, 2.95, 0.035, fill=C["blue"], C=C)
    tx(slide, 0.72, 1.12, 3.30, 0.16, "URBAN SYSTEMS  /  CASE 07", 8.0, C["blue"], "Consolas", True)
    tx(slide, 0.72, 1.70, 4.65, 1.24, "VERTICAL CITY\nRETROFIT", 30, C["graphite"], "Arial", True)
    tx(slide, 0.76, 3.34, 4.12, 0.56, "The next city is not built from scratch.\nIt is upgraded in place.", 13.5, C["graphite"], "Arial", True)
    tx(slide, 0.76, 4.26, 3.75, 0.44, "A connected strategy for aging high-rise housing:\nenvelope · energy · shared space · care", 12, C["muted"], "Arial")
    tx(slide, 0.76, 6.26, 3.50, 0.16, "CONCEPTUAL HERO VISUAL  /  NOT A REAL PROJECT", 7.0, C["blue"], "Consolas", True)
    tx(slide, 0.76, 6.76, 3.50, 0.14, "VERTICAL CITY RETROFIT  ·  2026", 7.0, C["muted"], "Consolas", True)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    prs.save(str(OUT))
    print(OUT)


if __name__ == "__main__":
    main()
