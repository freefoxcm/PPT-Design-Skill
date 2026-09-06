"""P6 environmental-reading prototype for the Louvre Abu Dhabi rebuild."""
from pathlib import Path

from pptx_designer import Presentation, svg_chart
from pptx_designer.tools.shapes import rect
from pptx_designer.tools.text import text


ROOT = Path(__file__).resolve().parents[2]
CASE = ROOT / "examples" / "new_examplex" / "louvre_abudhabi"
OUT = Path(__file__).resolve().parent / "louvre_abudhabi_p06_visual_baseline.pptx"
C = {
    "paper": "#F4F3ED", "ink": "#16252D", "muted": "#586A73",
    "silver": "#8EA0A2", "gold": "#B18C58", "line": "#B7C1C2",
}

CLIMATE_FIELD = r'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 560">
  <g fill="none" stroke="#7D9499" stroke-width="1.2">
    <path d="M360 55L540 130L615 280L540 430L360 505L180 430L105 280L180 130Z"/>
    <path d="M360 105L505 165L565 280L505 395L360 455L215 395L155 280L215 165Z"/>
    <path d="M360 55V505M105 280H615"/>
  </g>
  <g fill="none" stroke="#B18C58" stroke-width="1.15"><path d="M360 2V540M64 280H656"/></g>
  <g fill="#B18C58"><circle cx="360" cy="55" r="5"/><circle cx="615" cy="280" r="4"/><circle cx="360" cy="505" r="5"/></g>
  <g fill="#7D9499"><circle cx="105" cy="280" r="4"/><circle cx="360" cy="280" r="4"/><circle cx="505" cy="165" r="3"/></g>
</svg>'''


def tx(slide, x, y, w, h, value, size, color, font="Arial", bold=False, align=None):
    kwargs = dict(font_size=size, color=color, font_name=font, bold=bold, C=C)
    if align:
        kwargs["align"] = align
    return text(slide, x, y, w, h, value, **kwargs)


def main():
    prs = Presentation()
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    rect(slide, 0, 0, 13.333, 7.5, fill=C["paper"], C=C)
    rect(slide, 0.66, 0.60, 0.74, 0.023, fill=C["gold"], C=C)
    tx(slide, 0.66, 0.88, 2.95, 0.14, "05  /  THERMAL FIELD", 7.2, C["muted"], "Arial Narrow", True)
    tx(slide, 0.66, 1.42, 4.10, 1.38, "SHADE\nBECOMES\nINFRASTRUCTURE", 30, C["ink"], "Georgia")
    tx(slide, 0.70, 3.32, 3.70, 0.56, "The canopy filters daylight, reduces heat,\nand protects the public realm below.", 12, C["ink"], "Arial")
    tx(slide, 0.70, 4.22, 3.72, 0.52, "Natural cooling is not an add-on.\nIt is the spatial idea of the project.", 12, C["muted"], "Arial")

    tx(slide, 5.18, 0.86, 6.30, 0.18, "FROM SOLAR LOAD TO PUBLIC COMFORT", 8.0, C["gold"], "Consolas", True)
    svg_chart(slide, CLIMATE_FIELD, x=5.02, y=1.12, w=6.92, h=4.72, C=C)
    tx(slide, 6.24, 5.56, 4.42, 0.16, "OVERLAPPING GEOMETRY  /  FILTERED SKY", 7.1, C["muted"], "Arial Narrow", True, "center")

    rect(slide, 0.70, 5.92, 11.90, 0.018, fill=C["line"], C=C)
    items = [
        (0.70, "01", "SHADE", "block direct solar load"),
        (3.75, "02", "FILTER", "break light into layers"),
        (6.80, "03", "SOFTEN", "make the plaza inhabitable"),
    ]
    for x, num, label, detail in items:
        tx(slide, x, 6.12, 0.56, 0.22, num, 9.5, C["gold"], "Consolas", True)
        tx(slide, x + 0.46, 6.09, 1.40, 0.16, label, 9.2, C["ink"], "Arial Narrow", True)
        tx(slide, x + 0.46, 6.36, 2.22, 0.24, detail, 11.5, C["muted"], "Arial")
    tx(slide, 9.90, 6.12, 1.05, 0.32, "36 M", 23, C["ink"], "Arial")
    tx(slide, 11.02, 6.20, 1.20, 0.14, "ABOVE GROUND", 6.8, C["muted"], "Arial Narrow", True)
    tx(slide, 0.70, 7.05, 4.25, 0.14, "SOURCE  /  LOUVRE ABU DHABI — ARCHITECTURE", 6.4, C["muted"], "Arial Narrow", True)
    tx(slide, 12.02, 6.76, 0.62, 0.48, "06", 21, C["silver"], "Georgia", False, "right")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    prs.save(str(OUT))
    print(OUT)


if __name__ == "__main__":
    main()
