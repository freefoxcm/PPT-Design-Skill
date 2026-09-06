"""P3 technical content prototype for the Louvre Abu Dhabi rebuild."""
from pathlib import Path

from pptx_designer import Presentation, svg_chart
from pptx_designer.tools.shapes import rect
from pptx_designer.tools.text import text


ROOT = Path(__file__).resolve().parents[2]
CASE = ROOT / "examples" / "new_examplex" / "louvre_abudhabi"
OUT = Path(__file__).resolve().parent / "louvre_abudhabi_p03_visual_baseline.pptx"
C = {
    "night": "#10212B", "night2": "#17303B", "white": "#F6F6F1",
    "silver": "#AEBCC0", "muted": "#6E8187", "gold": "#B18C58",
}

DOME = r'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 540">
  <g fill="none" stroke="#6F8991" stroke-width="1.4">
    <path d="M360 42L520 108L586 270L520 432L360 498L200 432L134 270L200 108Z"/>
    <path d="M360 92L484 144L534 270L484 396L360 448L236 396L186 270L236 144Z"/>
    <path d="M360 42V498M134 270H586M200 108L520 432M520 108L200 432"/>
  </g>
  <g fill="none" stroke="#B18C58" stroke-width="1">
    <path d="M360 12V528M104 270H616"/>
  </g>
  <g fill="#B18C58"><circle cx="360" cy="42" r="5"/><circle cx="520" cy="108" r="4"/><circle cx="360" cy="498" r="5"/></g>
  <g fill="#AEBCC0"><circle cx="134" cy="270" r="4"/><circle cx="200" cy="432" r="4"/><circle cx="360" cy="270" r="4"/></g>
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
    rect(slide, 0.66, 0.60, 0.74, 0.023, fill=C["gold"], C=C)
    tx(slide, 0.66, 0.88, 3.30, 0.14, "02  /  ENVIRONMENTAL INSTRUMENT", 7.2, C["silver"], "Arial Narrow", True)
    tx(slide, 0.66, 1.48, 4.55, 0.90, "THE DOME\nAS INSTRUMENT", 29, C["white"], "Georgia")
    tx(slide, 0.70, 2.78, 3.80, 0.38, "FOUR OUTER LAYERS OF STAINLESS STEEL\nMEET FOUR INNER LAYERS OF ALUMINIUM.", 10.5, C["white"], "Arial Narrow", True)
    tx(slide, 0.70, 3.55, 3.70, 0.58, "The geometry filters daylight, shades the plaza,\nand turns the roof into a climate device.", 12, C["silver"], "Arial")

    svg_chart(slide, DOME, x=6.25, y=0.58, w=5.45, h=4.12, C=C)
    tx(slide, 7.05, 4.82, 4.20, 0.16, "LAYERED GEOMETRY  /  POROSITY AS PERFORMANCE", 7.1, C["gold"], "Consolas", True)
    rect(slide, 0.70, 5.30, 11.88, 0.018, fill=C["muted"], C=C)

    metrics = [
        (0.70, "7,850", "STARS IN THE PATTERN", "repeated apertures"),
        (4.45, "8", "OVERLAPPING LAYERS", "steel + aluminium"),
        (8.20, "180 M", "DOME DIAMETER", "museum-city scale"),
    ]
    for x, value, label, detail in metrics:
        tx(slide, x, 5.64, 2.60, 0.48, value, 26, C["white"], "Arial")
        tx(slide, x, 6.16, 2.60, 0.16, label, 7.0, C["gold"], "Arial Narrow", True)
        tx(slide, x, 6.44, 2.60, 0.20, detail, 11.5, C["silver"], "Arial")

    tx(slide, 0.70, 7.04, 4.30, 0.14, "SOURCE  /  LOUVRE ABU DHABI — ARCHITECTURE", 6.4, C["silver"], "Arial Narrow", True)
    tx(slide, 12.02, 6.76, 0.62, 0.48, "03", 21, C["muted"], "Georgia", False, "right")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    prs.save(str(OUT))
    print(OUT)


if __name__ == "__main__":
    main()
