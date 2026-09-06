# Visual direction

## Status

- DRAFT / LOCKED
- Confirmed by:
- Confirmed at:

## Visual thesis

## Theme Lock

- Version:
- Status: DRAFT / ACTIVE / SUPERSEDED
- User-confirmed at:
- Forbidden patterns:

## Resolved theme record

- Source: `ThemeComposer.compose(...)`
- Resolved-theme file:
- Seed:
- `pptx-designer` version:
- Imported module path:

## Design system

- Mood and audience fit:
- Colors:
- Typography and fallback:
- Grid, margins, and spacing:
- Image treatment:
- Chart / diagram language:
- Variance / motion / density:

## Page anchors and whitespace purpose

## Forbidden patterns

-

# Visual Direction — Signal Noir v1.1

## 视觉目标

第一眼识别为深色连续画布与青黄信号色，并由一个具有主体、光影和负空间的概念主视觉建立世界观；缩略图中五页应显示不同页面动作，而不是同一模板的换内容版本。

## Token

### 颜色

| Token | Value | Role |
|---|---|---|
| bg.ink | #0B111A | 主背景 |
| bg.graphite | #151E29 | 次级面板 |
| bg.fog | #273341 | 辅助背景/弱数据 |
| text.primary | #F4F7F8 | 主标题、关键文字 |
| text.secondary | #AAB7C4 | 正文解释 |
| text.muted | #718091 | 来源、页码、弱标签 |
| signal.cyan | #55E6E0 | 主数据、路径、强调 |
| signal.lime | #D8F36A | 第二重点、增长 |
| signal.coral | #FF6B5E | 风险、异常、反例 |
| line.grid | #344454 | 网格、坐标、弱分隔 |
| line.focus | #8CF4ED | 关键轨迹和焦点线 |

比例建议：70% 深色背景、20% 中性文字/面板、8% 青色、2% 黄绿或珊瑚异常标记；单页最多三种强调色。

### 字体与尺寸

几何无衬线粗体用于 display，中性无衬线用于 body，等宽字体仅用于 data 标签、数字、编号和时间戳。字号体系：56 / 40 / 30 / 24 / 18 / 14 / 11 pt。

### 网格与形态

16:9，13.333 × 7.5 in；安全边距左/右 0.62 in、上 0.42 in、下 0.38 in；12 列网格，间距 0.12 in，基础间距 0.08 in。默认无阴影，圆角 0.06–0.10 in，仅在线框面板中使用。

## v1.1 升级决策

- P1 采用右重心的概念英雄图，左侧保留原生中文标题负空间。
- 图片只承担氛围和世界观，不承载数据、标签或关键文字。
- 原生轨迹元素只做局部叠合，不再铺满整页作为主要视觉资产。
- P2–P5 减少“UI 组件感”，以页面级构图、比例变化和内容主舞台制造差异。

## 页面语言

轨迹线表达方向，节点表达事件，异常点使用珊瑚；图表去掉默认坐标轴、图例框和厚网格；图片使用冷色、低饱和处理，并保持负空间。

## 参考方法的可见证据

P1 全幅主视觉；P2 超大数字；P3 轨迹流程；P4 单一主图表；P5 强留白转折。五页共享 token，但不共享网格构图。
