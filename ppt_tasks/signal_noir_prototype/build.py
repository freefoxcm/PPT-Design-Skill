from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import pptx_designer
from pptx_designer import Presentation, validate_resolved_theme
from pptx_designer.renderer.theme import ThemeComposer
from pptx_designer.tools.images import cover_image
from pptx_designer.tools.shapes import arrow, neon_border, oval, rect, shape, spotlight
from pptx_designer.tools.text import multiline, text


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "output"
OUT.mkdir(exist_ok=True)
ASSET = ROOT / "assets"

# Signal Noir Theme Lock v1.0. These are page-level semantic overrides for the
# original theme thesis; the resolved ThemeComposer object remains authoritative
# for Presentation(theme=..., strict_theme=True).
C = {
    "ink": "#0B111A", "graphite": "#151E29", "fog": "#273341",
    "white": "#F4F7F8", "secondary": "#AAB7C4", "muted": "#718091",
    "cyan": "#55E6E0", "lime": "#D8F36A", "coral": "#FF6B5E",
    "grid": "#344454", "focus": "#8CF4ED",
}

def tx(slide, x, y, w, h, value, size=14, color="white", bold=False,
       font="Aptos", align=None):
    kwargs = dict(font_size=size, color=C[color], bold=bold, font_name=font, C=C)
    if align is not None:
        kwargs["align"] = align
    return text(slide, x, y, w, h, value, **kwargs)


def ml(slide, x, y, w, h, lines, size=12, color="secondary", spacing=1.15):
    return multiline(slide, x, y, w, h, lines, font_size=size, color=C[color], C=C,
                     line_spacing=spacing)


def rule(slide, x, y, w, h=0.018, color="grid"):
    return rect(slide, x, y, w, h, fill=C[color], C=C)


def glow(slide, x, y, radius, color="cyan", alpha=82):
    """Renderer-safe local halo used only at semantic focal points."""
    return spotlight(slide, x, y, radius, alpha=alpha, color=C[color])


def line_seg(slide, x1, y1, x2, y2, color="cyan", thickness=0.018):
    """Thin editable signal segment without arrowhead or filled bounding box."""
    length = math.hypot(x2 - x1, y2 - y1)
    angle = math.degrees(math.atan2(y2 - y1, x2 - x1))
    seg = rect(slide, (x1 + x2) / 2 - length / 2, (y1 + y2) / 2 - thickness / 2,
               length, thickness, fill=C[color], C=C)
    seg.rotation = angle
    return seg


def base(prs, number, label, title, subtitle):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    rect(slide, 0, 0, 13.333, 7.5, fill=C["ink"], C=C)
    # Keep the frame quiet. Grid lines belong only to pages that need a
    # coordinate system; repeating them on every page made v1.0 feel templated.
    tx(slide, 0.72, 0.47, 2.5, 0.16, label, 9, "cyan", True, "Consolas")
    # Editorial title lockup: deliberate line breaks and a serif display face
    # make the system pages feel authored rather than component-generated.
    tx(slide, 0.72, 0.78, 11.4, 0.86, title, 27, "white", True, "Noto Serif SC")
    tx(slide, 0.74, 1.72, 11.4, 0.24, subtitle, 12, "secondary")
    tx(slide, 12.05, 0.47, 0.6, 0.16, f"{number:02d}", 9, "muted", True, "Consolas", "right")
    rule(slide, 0.72, 6.98, 11.9, 0.012, "graphite")
    tx(slide, 0.72, 7.10, 8.2, 0.13, "SIGNAL NOIR / PROTOTYPE / CONCEPTUAL CONTENT", 7.5, "muted", False, "Consolas")
    return slide


def signal_texture(slide):
    # Editable abstract signal field for the cover.
    for i in range(9):
        y = 1.0 + i * 0.65
        rule(slide, 7.0, y, 5.5, 0.008, "grid")
    points = [(7.0, 5.5), (7.75, 4.8), (8.45, 5.0), (9.25, 3.75),
              (10.0, 4.2), (10.75, 2.65), (11.6, 3.0), (12.5, 1.6)]
    for (x1, y1), (x2, y2) in zip(points, points[1:]):
        arrow(slide, x1, y1, x2 - x1, y2 - y1, fill=C["cyan"], C=C)
    for i, (x, y) in enumerate(points):
        oval(slide, x - 0.07, y - 0.07, 0.14, 0.14,
             fill=C["lime"] if i in (3, 7) else C["cyan"],
             line=C["lime"] if i in (3, 7) else C["cyan"], C=C)


def build(theme):
    prs = Presentation(theme=theme, strict_theme=True)

    # P1 — cover / 穿透: image-led art direction v1.1
    s = prs.slides.add_slide(prs.slide_layouts[6])
    cover_image(s, 0, 0, 13.333, 7.5, str(ASSET / "signal_noir_hero_v2.png"))
    # The generated hero already contains a deep left negative space. Keep
    # the cover as one continuous canvas instead of adding a hard split panel.
    # Reintroduce a small editable trace on top of the image, not a competing
    # decoration field.
    # A restrained cyan halo makes the instrument feel emissive instead of
    # merely pasted onto the background. It sits below all editable traces.
    glow(s, 10.95, 3.20, 2.05, "cyan", 84)
    glow(s, 11.35, 3.65, 0.66, "lime", 92)
    arrow(s, 8.0, 5.8, 3.55, -1.9, fill=C["cyan"], C=C)
    oval(s, 11.35, 3.65, 0.18, 0.18, fill=C["lime"], line=C["lime"], C=C)
    rect(s, 0.62, 0, 0.012, 7.5, fill=C["cyan"], C=C)
    tx(s, 0.88, 0.78, 4.6, 0.2, "SIGNAL NOIR / THEME PROTOTYPE", 10, "cyan", True, "Consolas")
    # Renderer-stable display treatment: each line has a very tight
    # chromatic edge and a clean white foreground. The color shift is
    # intentional (cyan for signal, lime for decision) without reading as a
    # large RGB/glitch duplicate.
    tx(s, 0.848, 2.10, 6.3, 0.58, "复杂信息，", 40, "cyan", True, "Noto Serif SC")
    tx(s, 0.860, 2.10, 6.3, 0.58, "复杂信息，", 40, "white", True, "Noto Serif SC")
    tx(s, 0.848, 2.72, 6.3, 0.58, "变成可追踪的信号", 40, "lime", True, "Noto Serif SC")
    tx(s, 0.860, 2.72, 6.3, 0.58, "变成可追踪的信号", 40, "white", True, "Noto Serif SC")
    tx(s, 0.9, 3.85, 4.8, 0.5, "把主题、页面角色与证据\n组织成一条可追踪的叙事。", 16, "secondary")
    rule(s, 0.9, 5.22, 1.35, 0.035, "cyan")
    rule(s, 2.25, 5.22, 1.35, 0.035, "lime")
    tx(s, 0.9, 5.52, 4.8, 0.2, "01 / RESEARCH → DESIGN SYSTEM", 10, "lime", True, "Consolas")
    tx(s, 0.9, 6.78, 4.8, 0.14, "CONCEPTUAL HERO / REPLACEABLE IMAGE / NATIVE TYPE", 7.5, "muted", False, "Consolas")

    # P2 — scale / 放大
    s = base(prs, 2, "02 / SCALE", "成熟系统的尺度，\n不是页数，而是可切换的选择", "研究给出的两个参照：主题系统与页面角色系统。")
    tx(s, 0.88, 2.25, 4.2, 0.18, "RESEARCH SIGNAL / Dashi + PPT Master", 10, "cyan", True, "Consolas")
    tx(s, 0.88, 2.55, 3.8, 0.18, "SYSTEM SCALE / MATERIAL READOUT", 10, "muted", True, "Consolas")
    tx(s, 0.88, 3.12, 5.3, 0.72, "主题决定视觉世界，\n角色决定页面动作。", 24, "white", True, "Noto Serif SC")
    tx(s, 0.88, 4.22, 5.3, 0.35, "同一套 token，不同的阅读动作。", 16, "lime", True)
    rule(s, 0.88, 4.85, 4.4, 0.025, "cyan")
    tx(s, 0.88, 5.08, 4.4, 0.4, "来源：research_report.md / 公开资料综合", 10, "muted", False, "Consolas")
    # right-side material stage: a physical instrument gives the scale a
    # memorable object, while the number remains native and editable.
    tx(s, 7.0, 2.27, 4.8, 0.18, "20 / PAGE ROLES", 10, "cyan", True, "Consolas")
    cover_image(s, 7.0, 2.72, 5.35, 3.25, str(ASSET / "signal_noir_instrument_v1.png"))
    rect(s, 7.0, 2.72, 5.35, 3.25, fill=C["ink"], C=C)
    cover_image(s, 7.06, 2.78, 5.23, 3.13, str(ASSET / "signal_noir_instrument_v1.png"))
    neon_border(s, 7.0, 2.72, 5.35, 3.25, color=C["cyan"], radius=0.08)
    # Make the research numbers part of the instrument readout rather than a
    # detached KPI block. The ticks and labels are editable overlays.
    glow(s, 8.55, 4.15, 0.78, "lime", 74)
    tx(s, 7.52, 3.35, 1.6, 0.72, "12", 56, "white", True, "Consolas")
    tx(s, 8.95, 3.78, 1.95, 0.2, "THEMES / WORLD", 10, "cyan", True, "Consolas")
    for i in range(5):
        rule(s, 9.0 + i * 0.42, 4.25, 0.18, 0.018, "lime" if i == 3 else "grid")
    tx(s, 9.0, 4.48, 2.5, 0.2, "20 / PAGE ROLES", 11, "lime", True, "Consolas")
    tx(s, 9.0, 4.78, 2.5, 0.18, "ROLE = READING ACTION", 9, "secondary", True, "Consolas")
    rect(s, 7.0, 5.97, 5.35, 0.35, fill=C["ink"], C=C)
    tx(s, 7.05, 6.05, 5.0, 0.2, "页面角色让同一主题不断换动作。", 14, "white", True)

    # P3 — mechanism / 推进
    s = base(prs, 3, "03 / MECHANISM", "从主题 token 到页面证据，\n设计是一条转换链", "页面不复制模板，而是根据角色切换主舞台。")
    # v2 is a single continuous black-to-terrain field. It removes the hard
    # seam created when the previous gray-backed image sat on the black slide.
    cover_image(s, 0, 0, 13.333, 7.5, str(ASSET / "signal_noir_atlas_v2.png"))
    # Reassert the editorial frame above the full-bleed image; the image's
    # left negative space is intentionally dark enough to carry native type.
    tx(s, 0.72, 0.47, 2.5, 0.16, "03 / MECHANISM", 9, "cyan", True, "Consolas")
    tx(s, 0.72, 0.78, 11.4, 0.86, "从主题 token 到页面证据，\n设计是一条转换链", 27, "white", True, "Noto Serif SC")
    tx(s, 0.74, 1.72, 11.4, 0.24, "页面不复制模板，而是根据角色切换主舞台。", 12, "secondary")
    tx(s, 12.05, 0.47, 0.6, 0.16, "03", 9, "muted", True, "Consolas", "right")
    tx(s, 0.88, 2.15, 3.5, 0.18, "RESEARCH → THEME → ROLE → EVIDENCE", 10, "cyan", True, "Consolas")
    # Use a segmented signal trace here: unlike ARC, these line primitives do
    # not paint a bounding-box fill over the image, so the trace can genuinely
    # cross the black negative space and enter the terrain stage.
    glow(s, 8.65, 2.75, 0.72, "coral", 78)
    trace = [((1.05, 4.10), (3.0, 4.65)), ((3.0, 4.65), (5.0, 5.0)),
             ((5.0, 5.0), (8.0, 3.0)), ((8.0, 3.0), (11.2, 3.25))]
    for i, ((x1, y1), (x2, y2)) in enumerate(trace):
        line_seg(s, x1, y1, x2, y2, color="cyan" if i < 3 else "lime", thickness=0.022)
    # Anchor the first three stages to the flipped left arc and the last two
    # to the material stage, so the curve reads as a designed trajectory.
    points = [(1.05, 4.10), (3.0, 4.65), (5.0, 5.00), (8.0, 3.0), (11.2, 3.25)]
    labels = [("01", "研究", "observe", "cyan"), ("02", "主题", "compose", "cyan"),
              ("03", "角色", "shift", "lime"), ("04", "证据", "focus", "coral"),
              ("05", "验收", "prove", "lime")]
    for (x, y), (num, title, detail, col) in zip(points, labels):
        oval(s, x - 0.18, y - 0.18, 0.36, 0.36, fill=C[col], line=C[col], C=C)
        tx(s, x - 0.2, y - 0.58, 0.42, 0.14, num, 9, col, True, "Consolas", "center")
        tx(s, x - 0.45, y + 0.3, 0.9, 0.2, title, 13, "white", True, "Aptos", "center")
        tx(s, x - 0.75, y + 0.6, 1.5, 0.15, detail, 8.5, "muted", False, "Consolas", "center")
    # The image stage now carries the language of the final two steps, so it
    # reads as the destination of the chain rather than a decorative picture.
    tx(s, 7.15, 4.92, 2.9, 0.18, "EVIDENCE / MATERIAL TRACE", 9, "cyan", True, "Consolas")
    tx(s, 7.15, 5.22, 3.4, 0.42, "从轨迹，\n进入可验证的判断。", 15, "white", True, "Noto Serif SC")
    rule(s, 0.9, 6.15, 3.1, 0.03, "coral")
    tx(s, 4.3, 6.0, 7.5, 0.28, "页面角色不是装饰，它决定下一步如何被理解。", 15, "coral", True)
    rule(s, 0.72, 6.98, 11.9, 0.012, "graphite")
    tx(s, 0.72, 7.10, 8.2, 0.13, "SIGNAL NOIR / PROTOTYPE / CONCEPTUAL CONTENT", 7.5, "muted", False, "Consolas")

    # P4 — evidence chart / 聚焦
    s = base(prs, 4, "04 / EVIDENCE", "证据不是把内容塞进网格，\n而是让结论先被看见", "研究结论：共享 token，切换页面角色与视觉焦点。")
    # The evidence material becomes the conclusion stage itself. The right
    # side is no longer a detached text column with a decorative strip.
    cover_image(s, 8.25, 2.28, 4.05, 3.45, str(ASSET / "signal_noir_evidence_v1.png"))
    rect(s, 8.25, 2.28, 4.05, 3.45, fill=C["ink"], C=C)
    cover_image(s, 8.33, 2.36, 3.89, 3.29, str(ASSET / "signal_noir_evidence_v1.png"))
    neon_border(s, 8.25, 2.28, 4.05, 3.45, color=C["lime"], radius=0.04)
    tx(s, 0.88, 2.15, 4.4, 0.18, "RESEARCH SYNTHESIS / QUALITATIVE MAP", 10, "cyan", True, "Consolas")
    # chart area and axes
    rule(s, 0.98, 5.65, 7.15, 0.025, "grid")
    rule(s, 0.98, 2.55, 0.025, 3.12, "grid")
    tx(s, 0.82, 2.38, 0.55, 0.16, "强度", 9, "muted", True, "Consolas")
    for i in range(5): rule(s, 1.0, 2.75 + i * 0.65, 7.1, 0.01, "graphite")
    # The evidence page is organized around a semantic threshold, not a
    # generic horizontal benchmark: left is composition, right is decision.
    rule(s, 5.52, 2.58, 0.028, 3.08, "coral")
    glow(s, 5.54, 4.1, 0.62, "coral", 82)
    tx(s, 5.7, 2.62, 1.8, 0.16, "THRESHOLD / 03", 8.5, "coral", True, "Consolas")
    tx(s, 1.02, 6.18, 1.55, 0.16, "COMPOSE", 8.5, "cyan", True, "Consolas")
    tx(s, 5.82, 6.18, 1.55, 0.16, "DECIDE", 8.5, "coral", True, "Consolas")
    # A qualitative evidence map reads better as a continuous trace than as
    # a staircase chart. The stage markers remain discrete and editable.
    evidence_arc = shape(s, "ARC", 1.0, 2.7, 6.35, 2.72, fill=C["ink"], line=C["cyan"], C=C)
    evidence_arc.rotation = 180
    shape(s, "ARC", 1.55, 3.18, 5.15, 1.88, fill=C["ink"], line=C["grid"], C=C)
    data = [(1.25, 3.95), (2.1, 4.45), (2.95, 4.85), (3.8, 5.15), (4.65, 5.25), (5.5, 3.3), (6.35, 3.65), (7.25, 3.9)]
    for i, (x, y) in enumerate(data):
        oval(s, x - 0.065, y - 0.065, 0.13, 0.13, fill=C["lime"] if i in (3, 5, 7) else C["cyan"], line=C["lime"] if i in (3, 5, 7) else C["cyan"], C=C)
    for i, ((x, y), label) in enumerate(zip(data, ("输入", "叠加", "偏移", "放大", "异常", "", "验证", "落点"))):
        if not label:
            continue
        label_y = y - 0.28 if i < 5 else y + 0.16
        tx(s, x + 0.1, label_y, 0.72, 0.16, label, 8.5, "muted", True, "Aptos")
    tx(s, 5.65, 3.0, 2.15, 0.22, "重点标注 / ROLE SHIFT", 11, "lime", True, "Consolas")
    tx(s, 5.65, 3.28, 2.2, 0.35, "角色切换", 15, "white", True)
    rule(s, 8.55, 2.62, 2.55, 0.03, "lime")
    tx(s, 8.55, 2.95, 3.2, 0.6, "固定网格\n无法承载所有角色。", 23, "white", True)
    ml(s, 8.58, 4.05, 2.95, 0.9, ["先声明页面任务，", "再选择视觉结构。"], 12, "secondary")
    tx(s, 8.58, 6.35, 3.2, 0.18, "SOURCE / RESEARCH_REPORT.MD", 9, "muted", True, "Consolas")

    # P5 — transition / 切换
    s = base(prs, 5, "05 / TURN", "下一步：验证页面角色", "从研究结论进入主题原型的方向门槛。")
    cover_image(s, 0, 0, 13.333, 7.5, str(ASSET / "signal_noir_threshold_v1.png"))
    rect(s, 0, 0, 6.9, 7.5, fill=C["ink"], C=C)
    glow(s, 10.65, 3.25, 1.55, "lime", 78)
    neon_border(s, 7.84, 0.98, 4.62, 4.95, color=C["lime"], radius=0.06)
    # The hero is layered after base(); restore the editorial frame on top so
    # the transition page keeps its navigation and source metadata.
    tx(s, 0.72, 0.47, 2.5, 0.16, "05 / TURN", 9, "cyan", True, "Consolas")
    tx(s, 0.72, 0.82, 6.0, 0.52, "下一步：验证页面角色", 27, "white", True)
    tx(s, 0.74, 1.39, 6.0, 0.24, "从研究结论进入主题原型的方向门槛。", 12, "secondary")
    tx(s, 12.05, 0.47, 0.6, 0.16, "05", 9, "muted", True, "Consolas", "right")
    rule(s, 0.72, 6.98, 11.9, 0.012, "graphite")
    tx(s, 0.72, 7.10, 8.2, 0.13, "SIGNAL NOIR / PROTOTYPE / CONCEPTUAL CONTENT", 7.5, "muted", False, "Consolas")
    tx(s, 8.1, 1.25, 4.4, 0.65, "TURN", 56, "lime", True, "Consolas")
    tx(s, 8.15, 2.0, 3.8, 0.18, "A CHANGE IN READING MODE", 10, "secondary", True, "Consolas")
    rule(s, 8.15, 2.42, 3.75, 0.018, "grid")
    tx(s, 0.9, 2.25, 9.8, 1.35, "从“主题是什么”，\n切换到“这一页要让人做什么”。", 34, "white", True, "Noto Serif SC")
    rule(s, 0.92, 4.25, 4.2, 0.045, "lime")
    tx(s, 0.92, 4.65, 5.2, 0.25, "THE ROLE IS NOW THE DECISION", 13, "lime", True, "Consolas")
    arrow(s, 7.55, 5.35, 3.35, -1.9, fill=C["coral"], C=C)
    oval(s, 11.15, 3.2, 0.5, 0.5, fill=C["coral"], line=C["coral"], C=C)
    tx(s, 10.25, 4.0, 2.2, 0.18, "NEXT / CHOICE", 10, "coral", True, "Consolas", "center")
    tx(s, 8.48, 4.5, 2.9, 0.22, "ROLE → DECISION", 12, "lime", True, "Consolas")
    tx(s, 8.48, 4.82, 3.0, 0.36, "读法改变，\n页面才真正开始工作。", 15, "white", True, "Noto Serif SC")
    tx(s, 0.92, 6.2, 5.2, 0.18, "下一阶段：用真实案例内容验证，而不是继续堆装饰。", 11, "secondary")

    return prs


def main():
    theme = ThemeComposer().compose(style="dark-tech", seed=31, query="Signal Noir dark data journalism signal trajectory")
    validate_resolved_theme(theme)
    payload = json.dumps(theme, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    theme_path = ROOT / "resolved-theme-v1.json"
    theme_path.write_text(payload + "\n", encoding="utf-8")
    fingerprint = hashlib.sha256(payload.encode("utf-8")).hexdigest()
    prs = build(theme)
    pptx_path = OUT / "signal_noir_prototype.pptx"
    prs.save(pptx_path)
    meta = {
        "pptx_designer_version": pptx_designer.__version__,
        "pptx_designer_module_path": pptx_designer.__file__,
        "theme_lock_version": "v1.1",
        "resolved_theme_path": str(theme_path),
        "resolved_theme_fingerprint": fingerprint,
        "resolved_theme_seed": 31,
        "output": str(pptx_path),
        "slides": 5,
    }
    (ROOT / "build-metadata.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(meta, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
