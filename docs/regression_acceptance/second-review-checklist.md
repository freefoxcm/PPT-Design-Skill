# 第二 Reviewer 复核清单

> 说明：Technical Infrastructure Economics 保留为历史审查记录，但其 composition 修订因制作失败被放弃，已排除出正式五案例设计基准、参考集与完成度统计；本页中的相关条目仅用于保留审查证据。

复核对象：2026-09-04 三套回归案例

本清单用于第二 Reviewer 的独立复核。第二 Reviewer 应直接打开 upgraded PPTX 和对应 rendered PNG，不以 baseline 的视觉质量替代案例质量判断，也不只依据 Python 结构检查结果签字。

## 统一复核规则

1. 先看完整 PNG 序列，再看重点页原始 PPTX。
2. 对每个 MUST 条件给出 `PASS`、`NEEDS_REVISION` 或 `BLOCKED`，并写出页面证据。
3. 重点检查：标题/页码、图注与来源、文字是否在演示尺度可读、图表是否被裁切、结论是否超过证据边界、是否存在通用卡片堆叠。
4. 只有所有 MUST 条件通过、低分项已解释、且主 Reviewer 与第二 Reviewer 结论一致，案例才可从 `BLOCKED` 解锁。

## 01 — technical-infrastructure

目标文件：`examples/new_examplex/ai_infrastructure_economics/output/ai_infrastructure_economics.pptx`

Acceptance Record：`docs/regression_acceptance/technical-infrastructure.json`

重点复核页：P01、P02、P05、P06、P08、P09、P10、P11

| 复核项 | 需要确认的事实 | 通过标准 |
|---|---|---|
| P01 首屏 | 标题、报告定位、页码和视觉层级 | 首屏信息层级稳定，无标题/副标题碰撞 |
| P02 依赖栈 | 红色 dependency 箭头是否仍压过主体 | 箭头表达关系但不成为主视觉噪音 |
| P05 瓶颈 | land → energy → network → servers 的顺序 | 阶梯结构可读，慢层约束结论明确 |
| P06 飞轮 | capacity → utilization → revenue → cash 的关系 | 节点、方向和 operating leverage 中心命题一眼可读 |
| P08 价值流 | power/place → compute → platform → application | 连续流结构不能被误读为独立卡片列表 |
| P09 风险矩阵 | lead time × utilization 的二维关系 | 四个区域对应坐标语义，不被误读为装饰色块 |
| P10 选择模型 | buy / rent / build 的比较 | 表格行列对齐，`illustrative` 边界清楚 |
| P11 控制面板 | 五项运营指标是否形成反馈系统 | 指标之间有层级，不能回退为卡片墙 |

主审结论为 `NEEDS_REVISION`；第二 Reviewer 确认预期的 composition 修订因制作失败被放弃，不能按未交付的版本验收。

## 02 — scientific-evidence

目标文件：`examples/new_examplex/car_t_single_cell_paper/output/car_t_single_cell_atlas_blue_editorial.pptx`

Acceptance Record：`docs/regression_acceptance/scientific-evidence.json`

重点复核页：P01、P04、P06、P08、P10、P11、P12

| 复核项 | 需要确认的事实 | 通过标准 |
|---|---|---|
| P01 首屏 | Nature 论文、CAR-T atlas、临床→细胞状态主线 | 概念封面明确标记，不冒充原始论文图 |
| P04 细胞图谱 | 695,819 cells、17 states、Fig. 1b | UMAP 标签和图注在演示尺度可读 |
| P06 type 2 state | transcriptome、secretion、chromatin、perturbation 四层证据 | 四类证据可区分，不能把关联写成单一因果结论 |
| P08 secretome | 345 measurements、30 cytokines、33 patients、days 1–63 | 数字、时间窗、来源图注同时清楚 |
| P10 engineering | IL-4 10/50 ng ml⁻¹、priming、ET2-L/H | 工程策略保留 study/model boundary |
| P11 evidence chain | observed → resolved → proposed → tested | 临床、细胞、机制、临床前四层不能混写 |
| P12 takeaway | paper contribution and boundary | 结论不外推为已证实临床工程方案 |

主审初始结论为 `BLOCKED`；第二 Reviewer 确认页面层级、图注、来源和证据边界可读，论文原生图内部标签不属于 PPT 字号阻塞项，Acceptance Record 已更新为 `PASS`。

## 03 — brand-architecture

目标文件：`examples/new_examplex/louvre_abudhabi/output/louvre_abudhabi_complete.pptx`

Acceptance Record：`docs/regression_acceptance/brand-architecture.json`

重点复核页：P01、P02、P06、P07、P08、P09、P10

| 复核项 | 需要确认的事实 | 通过标准 |
|---|---|---|
| P01 首屏 | Louvre Abu Dhabi、建筑主题、项目定位 | 首屏建立建筑/穹顶/光影语义，不像普通旅游宣传页 |
| P02/P06–P10 页码 | 双位页码 02、06、07、08、09、10 | 数字完整、水平基线一致、无上下拆分 |
| P06–P09 内容 | 几何、光影、结构和参观体验的递进 | 每页有独立空间命题，不能只换标题换配色 |
| P10 收束 | 设计原则与案例结论 | 结尾回收建筑逻辑，并保留来源/素材边界 |

主审已修复双位页码并重新渲染；第二 Reviewer 确认修复没有破坏页脚、边界和最后一页收束，Acceptance Record 已更新为 `PASS`。

## 签字栏

| 案例 | 主 Reviewer | 第二 Reviewer | 最终状态 |
|---|---|---|---|
| technical-infrastructure | 已记录，NEEDS_REVISION | 已复核，制作失败未通过 | BLOCKED |
| scientific-evidence | 已记录，11/12 | 已复核，PASS | PASS |
| brand-architecture | 已记录，修复后待复核 | 已复核，PASS | PASS |

## 第二 Reviewer 结论 — 2026-09-06

### technical-infrastructure

P01、P02、P05、P06、P08、P09、P10、P11 已直接检查。复核发现预期的
composition 替换版本并未成功制作，随后被放弃；因此不能把设计意图或局部
页面草稿当作已交付证据。当前输出仍无法证明已经摆脱重复 dashboard grammar。
结论：`BLOCKED`，composition 保持 0，等待成功生成并渲染的新版本。

### scientific-evidence

P01、P04、P06、P08、P10、P11、P12 已直接检查。封面明确标记 conceptual
visual，证据链清楚区分 observed / resolved / proposed / tested，P10 也保留
model and study design boundary。页面标题、解释文字、图注和来源在 1280×720
下可读。P04、P06、P08、P10 内部的细小标签属于论文原生图像内容，不属于 PPT
原生文字字号规则，也不作为本案例的阻塞项。结论：`PASS`。

### brand-architecture

P01、P02、P06、P07、P08、P09、P10 已直接检查。双位页码完整且基线一致；
照片裁切、几何/光影图、三图序列、材料页和 coda 的建筑叙事成立，来源标签
和素材边界保留。结论：`PASS`。
