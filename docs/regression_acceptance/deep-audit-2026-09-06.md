# 深度审查：master → main 合并前评估

审查日期：2026-09-06  
审查分支：`codex/visual-capability-implementation` / `master`  目标：`main`

## 结论

初始结论为 **NO-GO：暂不合并 master 到 main**。本轮清理后，文件与自动化
门禁已恢复；最终合并仍需等待视觉复核 Gate 完成。

原因不是流程没有价值，而是合并前的质量门禁仍未闭环：当前 master 比 main
多 3 个提交且可以快进，但仓库本身仍有测试失败、案例输出不唯一、Prototype
预览路径失效，以及第二 Reviewer 尚未完成签字等问题。

## 已确认的正向结果

| 领域 | 结论 | 证据 |
|---|---|---|
| 安装与运行时 | PASS | `check_runtime.py` 与 `installer/install.py --check` 通过；pptx-designer、PowerPoint 结构库、Pillow、LibreOffice、Poppler 均可用 |
| baseline 配对 | PASS | `audit_regression_pairs.py` 对技术、科研、建筑三组均通过，页数分别为 12/12、12/12、10/10 |
| 五个 benchmark 案例资产 | PASS | 五个正式 benchmark 案例均有 build.py、brief/page-plan、visual review、prototype recipe/object map；Technical Infrastructure 单独保留为历史排除案例 |
| 设计表现 | 明显提升 | 五个正式 benchmark 案例已形成可识别的领域视觉语言；图片、编辑型排版、原生图形和叙事页角色明显优于中性 baseline |
| 流程能力 | 已具备 | brief → build → inspect → render → visual review → acceptance record 的主要链路已存在 |

## 初始合并阻塞项与清理结果

### 1. 自动化测试不是绿灯

清理前 `pytest` 结果为 **21 passed, 4 failed**。失败集中在：

- `validate_visual_pack.py`：Prototype index 中 COUTURE 的
  `rendered/slide01.png` 预览路径无法通过校验；
- `audit_prototype_provenance.py`：Prototype provenance 总体为
  `UNVERIFIED`；
- `audit_visual_review_records.py`：CAR-T 与 Louvre 的 `output/` 中存在多个
  PPTX，无法确定唯一 canonical output；
- `audit_case_outputs.py`：案例输出闭环失败。

这些失败已通过本轮清理与预览恢复解决，不能作为合并后的已知无害告警处理。

### 2. 案例输出目录没有单一事实源

当前扫描结果：

| 案例 | PPTX 数量 | 渲染 PNG | 状态 |
|---|---:|---:|---|
| AI Agent Operating System | 1 | 12 | render-ready |
| AI Infrastructure Economics | 1 | 12 | render-ready |
| CAR-T Single-Cell Paper | 15 | 12 | BLOCKED |
| COUTURE COLOR | 1 | 0（当前工作区） | BLOCKED |
| Louvre Abu Dhabi | 2 | 10 | BLOCKED |
| Vertical City Retrofit | 1 | 14 | render-ready |

临时版本已移出 `output/`，归档于 `examples/_archive/2026-09-06/`；当前每个案例
只保留一个由 `build.py` 指向的 canonical PPTX。

## 清理后验证

| 检查 | 结果 |
|---|---|
| `validate_visual_pack.py` | PASS |
| `audit_case_outputs.py` | PASS；6/6 案例 `render_ready` |
| `audit_visual_review_records.py` | PASS；6/6 案例通过结构/记录一致性审计 |
| `audit_prototype_provenance.py` | PASS；canonical provenance 可解析 |
| `pytest -q` | PASS；25 passed |

本轮保留的 canonical 版本：

- CAR-T：`output/car_t_single_cell_atlas_blue_editorial.pptx`
- Louvre：`output/louvre_abudhabi_complete.pptx`
- COUTURE：`output/couture_color_objects_of_desire.pptx`

旧 baseline、单页实验 PPTX、临时渲染目录和额外裁切目录均保留在归档目录，
没有直接删除。

### 3. 第二 Reviewer 尚未完成

现有回归记录仍然显示：

- Technical Infrastructure：`NEEDS_REVISION`，composition 低分；
- Scientific Evidence：第二 Reviewer 已确认页面标题、图注、来源和证据边界可读；论文原生图内部标签不作为 PPT 字号阻塞项，状态已更新为 `PASS`；
- Brand Architecture：主审修复完成，但第二 Reviewer 仍为 `PENDING`。

因此目前只能证明“流程跑通并发现了问题”，还不能证明“升级后的系统已经
稳定提升最终交付质量”。

## 设计效果评估

### 已经有效提升的部分

- 从单一模板思路转向 domain-aware page grammar；
- 封面、章节节奏、图片裁切、留白与信息层级显著增强；
- 原生 PowerPoint 对象承担色板、产品结构、时间线、建筑/科研图示，编辑性更好；
- Visual Direction、Theme Lock、Acceptance Contract 让设计判断开始可复用；
- 三组独立 baseline/upgraded 对照已经证明“升级不是只换颜色或字体”。

### 尚不能宣称已经解决的部分

- Technical Infrastructure 的 composition 修订制作失败，已从 benchmark/reference set 排除；
- 科研案例的图版在演示尺度下仍有可读性风险；
- 五个正式 benchmark 案例不再以 Technical Infrastructure 的未完成修订作为完成度证据；
- 当前没有覆盖用户从安装、选方向、生成、修订到交付的真实体验测试；
- 自动化系统能发现结构和文件问题，但还不能自动判断“是否足够高级、是否
  真的像 editorial 而不是模板”。

## 用户体验评估

当前体验属于 **可用但偏专家向**：

- 对熟悉仓库和脚本的设计/工程人员，流程已经可重复；
- 对普通用户，文件数量、任务目录、rendered/output 的关系、第二 Reviewer
  的职责仍不够直观；
- 输出目录中保留多个版本会造成严重的选择困难；
- 渲染链在 PowerPoint COM 卡住时虽有后备方案，但用户侧缺少清晰的状态与
  恢复提示；
- `render_ready`、`PASS`、`NEEDS_REVISION`、`BLOCKED` 的区别需要在用户指南
  中用一个简短状态表解释。

## 合并前必须完成的 Gate

1. 清理 CAR-T 与 Louvre 的 `output/`，每个案例只保留一个 canonical PPTX，
   并更新 provenance/hash 记录；
2. 恢复 COUTURE 的完整 PNG 预览集，并修正 prototype index 的路径校验；
3. 让 `pytest -q` 全部通过；
4. 让 `validate_visual_pack.py`、`audit_visual_review_records.py`、
   `audit_case_outputs.py` 全部返回 0；
5. 完成正式 benchmark 案例的第二 Reviewer 独立签字；Technical Infrastructure
   已被排除，不再作为合并或设计效果证据；
6. 在用户指南加入 canonical output、状态语义和渲染失败恢复说明；
7. 完成一次从新用户视角的最小体验演练：安装 → 创建任务 → 生成 → 查看 PNG
   → 修改 → 交付。

## 建议的合并策略

不要直接把整个脏工作区合并到 main。建议先在 master 上形成一个小的
`release-readiness` 修复提交，完成上述 Gate 后重新跑完整审计；只有所有自动
化门禁为绿灯、三组第二 Reviewer 签字完成后，再将 master fast-forward 到 main。

当前更准确的阶段判断是：**流程升级完成，案例重构基本完成，发布合并尚未完成**。
