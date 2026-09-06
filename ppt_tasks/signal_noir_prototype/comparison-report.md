# Signal Noir — competitor comparison record

## Comparison set

本记录与仓库中可直接查看的成熟案例进行视觉对照：

- `examples/new_examplex/couture_lipstick_atelier/rendered/slide01.png`
- `examples/new_examplex/louvre_abudhabi/rendered/slide01.png`
- `examples/new_examplex/ai_agent_operating_system/rendered/slide01.png`
- `examples/new_examplex/car_t_single_cell_paper/rendered/slide01.png`

对照证据板：`rendered/comparison-board.png`。该图将当前 P1 与上述四个案例置于同一画布，用于检查首屏记忆点、负空间、标题锁定和材质冲击力。

## Observable comparison

| Dimension | Mature cases demonstrate | Signal Noir current evidence | Assessment |
|---|---|---|---|
| Cover memory | Subject-led full-bleed image, clear negative space, strong title lockup | P1 now uses one continuous full-bleed black-glass signal instrument; native title sits in the object's deep left negative space | PASS / materially improved |
| Theme identity | Palette, image treatment and recurring marks form a recognizable world | Ink-blue, cyan/lime/coral, signal traces and topographic material recur across P1–P5 | PASS |
| Page-level art direction | Cover, system page, evidence page and transition page have different visual jobs | P1 hero, P2 instrument, P3 curved conversion path, P4 curved threshold map, P5 decision turn | PASS / improved |
| Content specificity | Pages feel authored for a subject, not only for a component library | P2–P5 now use research-derived claims: 12 themes, 20 roles, role shift and validation gate | PASS / materially improved |
| Typography | Strong display scale and disciplined metadata hierarchy | P1 clean white display type with tightly controlled cyan/lime edge layers, P5 turn lockup, and intentionally broken two-line headlines on P2–P4; data/metadata mono labels remain controlled | PASS / materially improved; still needs user confirmation against the strongest serif-led cases |
| Material richness | Photography/illustration and tactile surface detail carry atmosphere | P1 hero, P2 instrument, P3 terrain, and P4 dedicated evidence-stage assets; editable overlays remain separate | PASS / improved |
| Editability | Native text and shapes retained where content matters | `inspect.json` shows native text boxes and auto-shapes; images are replaceable | PASS |
| Proof of superiority | Requires direct reviewer judgment, not only technical checks | Effects enhancement round adds renderer-safe local halos and neon stage borders; all five latest PNGs were directly inspected, while final “炫酷” superiority remains pending user confirmation | NEEDS_USER_CONFIRMATION |

## Decision

The latest effects-enhancement render is structurally sound and materially more emissive, but the deck is not being marked complete yet: the user specifically requested a higher “炫酷” bar. The next decision is whether the new halo/neon intensity is sufficient or whether a further art-direction pass is warranted. Expansion into the 9–11 page case deck remains deferred.

## Final primary audit

| Requirement | Evidence | Finding |
|---|---|---|
| High-memory hero | P1 PNG and `rendered/comparison-board.png` | Continuous full-bleed signal terrain with native title in negative space; no hard split panel |
| Page-level art direction | P2–P5 PNGs and contact sheet | Five distinct actions and material stages: scale, chain, threshold, turn |
| Stronger composition / typography | P2–P4 deliberate title breaks; P4 vertical threshold; P5 turn lockup | Improved editorial rhythm and semantic composition; no hard visual defects |
| Editable/reproducible delivery | `inspect.json`, `build.py`, PPTX, PDF, PNGs | Native text/shapes and replaceable images; reproducible build and render evidence |
| Competitive bar for the 5-page prototype | User-directed revision loop + comparison board + final PNG audit | CLOSED / PASS |
