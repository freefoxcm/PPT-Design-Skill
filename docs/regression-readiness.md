# 回归验收就绪度

盘点时间：2026-09-06

## 当前结论

## 项目阶段调整

当前项目进入“阶段一：端到端流程验证”。本阶段的目标是确认新的
`ppt-design-skill` 能否稳定完成 brief → 生成 → 结构检查 → 渲染 → 逐页
Acceptance Record → MUST 检查 → 第二 Reviewer 复核的完整链路，并证明
upgraded 案例相较中性 baseline 具有可观察的设计改善。

两个正式 benchmark 回归案例当前存在的局部视觉问题，不再被视为阶段一的唯一阻塞；Technical Infrastructure 已被排除，不再参与 benchmark；它们会
被记录为阶段二的精修任务。阶段一只有在流程跑通、证据完整、结论不夸大
时才算完成。阶段二再集中优化案例质量、新案例覆盖和设计稳定性。

三套首轮回归目标已经登记，独立 baseline 已生成，文件对与页数审计通过。正式 benchmark 案例已完成主 Reviewer 与第二 Reviewer 的复核；Technical Infrastructure 保留为历史结构控制，不作为视觉 benchmark：

案例是否具备接入新系统参考集的资格，另见 `docs/regression_acceptance/reference-readiness.md`。CAR-T 与 Louvre 已完成第二 Reviewer；Technical Infrastructure 为历史排除案例。

| regression_id | 领域 | upgraded | 阻塞原因 |
|---|---|---|---|
| `technical-infrastructure` | 技术 | `examples/regression_baselines/technical-infrastructure/baseline.pptx` → `ai_infrastructure_economics` | 已由项目决策排除出正式 benchmark/reference set；保留为历史控制记录 |
| `scientific-evidence` | 科研 | `examples/regression_baselines/scientific-evidence/baseline.pptx` → `car_t_single_cell_paper` | 主审与第二 Reviewer 已完成；作为正式参考候选 |
| `brand-architecture` | 品牌/建筑 | `examples/regression_baselines/brand-architecture/baseline.pptx` → `louvre_abudhabi` | 主审与第二 Reviewer 已完成；作为正式参考候选 |

Git 历史审计未在 `origin/master` 或 `origin/main` 找到这三套目标 PPTX 的历史版本，因此不能把当前 upgraded 文件复制或回退后冒充 baseline。当前案例源码是 Visual Grammar / Pack 版本，不能反向推断旧版视觉结果。

## 已确定的补齐方式

三套 baseline 将作为独立生成物重新制作，而不是复制现有 PPTX：

1. 沿用同一案例的 brief、事实、数据、素材、页数和输出尺寸；
2. 使用记录明确的 `pptx-designer` 版本和固定主题参数；
3. 采用中性、未接入 Visual Grammar / Rendering Pack 的基础布局，确保 baseline 与 upgraded 是不同的实际构建结果；
4. 在独立目录保存 baseline 的 `build.py`、PPTX、PDF、PNG 和控制变量记录；
5. 由 `audit_regression_pairs.py` 检查文件独立性和页数，再进行逐页评分。

独立 baseline 已由 `skill/scripts/build_regression_baselines.py` 生成，并保留每套的 `controls.json`、PPTX、PDF 和 PNG。需要特别区分：这些 baseline 是用于回归比较的中性控制组，不是交付级案例 PPTX，不能用其视觉效果代替 upgraded 案例的质量判断。`audit_regression_pairs.py` 已确认三套文件独立且页数一致；主审与第二 Reviewer 记录保存在 `docs/regression_acceptance/`，并已通过相关验收脚本。

## 解阻条件

每套回归必须补齐独立的 baseline PPTX，并记录相同的 brief、内容、素材、模板、seed、`pptx-designer` 版本、页面数量和输出尺寸。完成后运行：

```powershell
python skill/scripts/audit_regression_pairs.py
```

审计通过后，按页生成 Acceptance Record，由主 Reviewer 评分并由第二 Reviewer 独立复核。`render_ready` 只能证明文件与页数闭环，不能替代 baseline、视觉评分或许可证审查。
