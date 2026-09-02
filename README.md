<div align="center">

# Skills

**一组面向真实工作流持续打磨、可独立安装的 Codex Skills。**

[![Skills](https://img.shields.io/badge/Skills-5-22C55E?style=flat-square&labelColor=111827)](#skills-catalog)
[![Platform](https://img.shields.io/badge/Platform-Codex-4F8FF7?style=flat-square&labelColor=111827&logo=openai&logoColor=white)](#install)
[![Format](https://img.shields.io/badge/Format-SKILL.md-8B5CF6?style=flat-square&labelColor=111827)](#structure)
[![Language](https://img.shields.io/badge/Language-%E4%B8%AD%E6%96%87-F59E0B?style=flat-square&labelColor=111827)](#skills-catalog)

<br>

[仓库简介](#overview) · [Skill 目录](#skills-catalog) · [安装](#install) · [使用](#usage) · [仓库结构](#structure)

</div>

<a id="overview"></a>
## 仓库简介

这里收录我在产品、写作、AI 评测、文档整理和项目交付中持续使用的 Codex Skills。每个 Skill 都有独立的触发范围、工作流程与必要参考资料，可以单独安装，也可以一次选择多个。

当前共收录 **5 个 Skills**。每个目录中的 `SKILL.md` 是能力入口；`agents/`、`references/`、`scripts/` 和 `templates/` 只在该 Skill 确实需要时提供。

<a id="skills-catalog"></a>
## Skill 目录

| Skill | 适合做什么 | 查看 |
|---|---|---|
| `human-writing` | 从选题、观点深挖和公开材料检索，到中文文章、故事、口播与演讲稿的共创和改稿。 | [打开](skills/human-writing) |
| `evaluation-assistant` | 将模糊的模型、Prompt、Agent 或 Skill 评测需求，整理为目标卡、覆盖矩阵、评测集和可执行 Rubric。 | [打开](skills/evaluation-assistant) |
| `feishu-doc-incremental-merge` | 把会议纪要、录音总结或参考资料中的新增信息去重后，按语义位置融合进既有飞书文档。 | [打开](skills/feishu-doc-incremental-merge) |
| `product-analysis` | 从产品截图和操作证据反向整理用户旅程、Agent 契约、System Prompt 与产品全景架构。 | [打开](skills/product-analysis) |
| `readme-plus` | 创建或改造可信、可读、可行动的 GitHub README，并按受众控制徽章、安装、开发信息和产品策略的公开边界。 | [打开](skills/readme-plus) |

<a id="install"></a>
## 安装

交互式选择要安装的 Skill 和目标 Agent：

```bash
npx skills add yuanhao667/Skills
```

只安装指定 Skill 到 Codex：

```bash
npx skills add yuanhao667/Skills --skill readme-plus --agent codex
```

一次安装仓库中的全部 Skills：

```bash
npx skills add yuanhao667/Skills --skill '*' --agent codex
```

安装完成后，新建一个 Codex 会话即可使用。

<a id="usage"></a>
## 使用

可以直接描述任务，让 Codex 根据 Skill 的说明自动匹配；也可以用 `$skill-name` 明确指定：

```text
$readme-plus 帮我把这个仓库的 README 改成清晰的项目主页。

$evaluation-assistant 帮我把这次模型选型整理成可执行评测方案。

$product-analysis 根据这些产品截图梳理用户旅程和 Agent 架构。
```

每个 Skill 的适用范围和边界都写在对应的 `SKILL.md` 中。遇到复杂或条件化流程时，Skill 会按需读取自己的参考文件。

<a id="structure"></a>
## 仓库结构

```text
Skills/
├── README.md
└── skills/
    └── skill-name/
        ├── SKILL.md          # 必需：触发说明与核心工作流
        ├── agents/           # 可选：Codex 展示与调用元数据
        ├── references/       # 可选：按场景读取的详细规则
        ├── scripts/          # 可选：可重复执行的工具脚本
        └── templates/        # 可选：可复用模板
```

仓库只保留 Skill 真正需要的内容。条件化细节进入 `references/`，可重复操作进入 `scripts/`，避免在 `SKILL.md` 中堆叠无关说明。

---

<div align="center">

**Built with ❤️ by [@yuanhao667](https://github.com/yuanhao667)**

[浏览全部 Skills](skills) · [提交问题](https://github.com/yuanhao667/Skills/issues)

</div>
