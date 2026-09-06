# 案例参考资格矩阵

用途：判断正式 benchmark 回归案例是否已经达到“可作为新系统参考样本”的程度。

这里的“参考样本”指经过视觉和内容验收、可以用于新系统回归比较的 upgraded 案例；`regression_baselines` 目录中的中性 baseline 只用于技术对照，不属于交付级参考样本。

| 案例 | 当前资格 | 已完成 | 仍需完成 | 接入建议 |
|---|---|---|---|---|
| CAR-T Single-Cell Atlas | 内容基本可靠，暂缓最终接入 | 12 页主审、论文事实对照、逐页评分已完成 | 第二 Reviewer 确认 P04/P06/P08/P10 的演示尺度可读性 | 可作为科研叙事候选样本，签字后接入 |
| Louvre Abu Dhabi | 主审修复完成，待最终确认 | 修复 P02/P06/P07/P08/P09/P10 双位页码并重新渲染 | 第二 Reviewer 确认页脚、来源和整体建筑叙事未受影响 | 最接近可接入状态，签字后接入 |

AI Infrastructure Economics 已被项目决策排除出正式 benchmark/reference set。它的
文件和修订记录保留在案例目录中，但不再参与 benchmark 评分或完成度统计。

## 接入门槛

案例只有在以下条件全部满足后，才能进入新系统的正式参考集：

- upgraded PPTX 结构检查通过，页数和尺寸正确；
- PPTX → PDF → PNG 重新渲染成功；
- 每一页都有主 Reviewer 的评分和证据；
- 所有 MUST 条件都有可见证据；
- 第二 Reviewer 完成独立复核；
- `Acceptance Record.status` 不再是 `BLOCKED` 或 `NEEDS_REVISION`；
- baseline 与 upgraded 的来源、素材、页数和控制变量可追溯。

## 当前结论

截至本次复核，CAR-T 与 Louvre 已完成第二 Reviewer 复核并可作为正式参考样本；AI Infrastructure Economics 被明确排除，不计入正式参考集。
