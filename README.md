# Skills

集中管理个人 Codex Skills，用于版本维护、中文识别和多台电脑同步安装。

## Skill 目录

| 中文名称 | 英文目录 | 分类 | 一句话说明 |
|---|---|---|---|
| [活人感写作](skills/human-writing-skill) | `human-writing-skill` | 写作 | 从选题、观点和材料开始共创，深挖分论点，写出自然中文并完成改稿。 |
| [AI 评测方案助手](skills/evaluation-assistant) | `evaluation-assistant` | AI 评测 | 从业务决策出发，完成评测目标卡、覆盖评测集与可执行 Rubric。 |
| [飞书文档增量融合整理](skills/feishu-doc-incremental-merge) | `feishu-doc-incremental-merge` | 文档处理 | 对比增量来源与飞书母板，去重后按语义位置融合并验证。 |
| [产品架构分析](skills/product-analysis) | `product-analysis` | 产品分析 | 从产品截图反推用户旅程、Agent 契约、Prompt 与产品全景架构。 |

## 目录规则

每个 Skill 都放在 `skills/<英文目录名>/` 下，并保留完整的 `SKILL.md`、`agents/`、`references/`、`scripts/` 和所需资源。

英文目录名用于 GitHub 路径和安装兼容；中文名称与中文说明统一放在本页，便于浏览和分类，不再为每个 Skill 单独创建中文说明页。

## 多台电脑使用

在另一台电脑上登录 Codex 后，让 Codex 从本仓库对应的 Skill 子目录安装即可。例如：

> 请从 GitHub 仓库 `yuanhao667/Skills` 的 `skills/product-analysis` 目录安装这个 Skill。

以后更新 Skill 时，先更新本仓库中的对应目录，其他电脑再从同一路径重新安装或更新。
