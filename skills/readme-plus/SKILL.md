---
name: readme-plus
description: 为 GitHub 项目创建或改造清晰、可信、具有项目主页质感的 README.md。适用于 README 新建、美化、首屏与 Hero 重构、Shields.io 黑色加彩色徽章、章节导航、安装与运行说明、GitHub Releases 下载入口、macOS DMG 首次打开说明、License、页脚，以及 Repository Description 和 Topics 更新。先读取仓库与 Release 的真实信息，再按产品主页、文档优先或作品展示模式交付；不把内部开发验收内容默认写进公开 README。
---

# readme-plus

把 README 做成可信、可读、可行动的项目入口。读者应快速知道：这是什么、为什么值得继续看、从哪里体验或下载安装。

## 基本原则

1. 事实优先。不要编造 Demo、下载包、状态、版本、兼容性、指标、技术栈或许可证。
2. 先判断受众。产品用户、开发者和贡献者需要的 README 不同。
3. 首屏克制。项目身份、简短定位、少量事实徽章、必要导航和一张主视觉通常已经足够。
4. 行动入口必须真实。链接应直接到可用页面、文档或安装包。
5. README 是公开入口，不是内部交付记录。测试命令、开发验证和手工验收清单只在贡献者文档或用户明确要求时加入。

## 选择交付模式

| 模式 | 适用场景 | 默认交付 |
|---|---|---|
| `project-home` | App、Web 产品、设计项目、Agent Skill、可下载安装的工具 | 居中身份、2–5 个事实徽章、章节导航、单张 Hero、产品说明、安装／体验、简短页脚 |
| `clean-doc` | SDK、库、CLI、后端、基础设施 | 简洁标题、必要状态徽章、快速安装、最小示例、API／文档入口；Hero 和导航均可省略 |
| `showcase` | 用户明确强调作品展示、品牌传播或视觉呈现 | 在 `project-home` 基础上强化 Hero 和产品截图；仍避免重复视觉 |

没有明确理由时，面向最终用户的 App 与 Web 项目使用 `project-home`；库、SDK 和基础设施使用 `clean-doc`。不要强迫所有仓库使用同一套首屏。

## 工作流程

### 1. 读取仓库与线上事实

先读取现有项目，不从仓库名猜功能：

```bash
pwd
rg --files -g '!*build*' -g '!*.xcuserstate' | head -120
```

优先检查：

- 现有 `README.md`、`LICENSE`、项目清单和主要入口。
- `package.json`、`pyproject.toml`、`go.mod`、`Cargo.toml`、`.xcodeproj` 等真实技术信息。
- `docs/`、截图、App 图标、品牌素材、Demo 和公开链接。
- GitHub Actions、部署配置、Issues 地址、作者主页。
- GitHub Releases 及其 assets。安装包未提交到仓库，不代表 Release 里没有。

升级现有 README 时，先列出必须保留的事实、命令、链接和独特内容，再重排。若用户要求直接修改仓库，则修改并验证；仅要求建议时不要擅自变更 GitHub 元信息或 Release。

### 2. 建立事实卡

至少确认以下字段：

| 字段 | 内容 |
|---|---|
| `project_name` | 正式项目名 |
| `tagline` | 一句话定位 |
| `audience` | 最主要的读者 |
| `primary_action` | 体验、下载、安装、阅读文档或快速开始 |
| `primary_url` | 对应的真实链接 |
| `license` | 实际许可证及文件路径 |
| `status` | 真实发布、构建或版本状态 |
| `stack` | 2–3 个有辨识度的技术信息 |
| `hero_source` | 真实截图、已有宣传图或待制作 Hero |
| `download_assets` | Release 中可公开下载的安装包 |
| `install_notes` | 平台安装与首次启动注意事项 |
| `author_url` | 作者或团队主页 |

缺失事实时优先从仓库、GitHub API 和公开页面查证。不能查证就省略，不用占位符伪装完整。

### 3. 设计首屏

制作首屏前读取 [references/design-system.md](references/design-system.md)。`project-home` 推荐顺序：

1. 项目图标或名称。
2. 一句话定位。
3. 2–5 个黑色标签加彩色值的事实徽章。
4. 可选的主 CTA。只有当单一动作明显比其他入口重要时才使用大徽章。
5. 一行简短章节导航，链接到 README 内真实存在的主要章节。
6. 一张可点击的 16:9 Hero。

章节导航与大 CTA 不必同时出现。面向内容浏览的项目通常优先导航；有明确在线体验或直接下载动作的项目可以保留 CTA。

图标默认直接使用项目正常提供的文件。把 README 渲染出来后再检查；只有实际出现黑角、异常底色、裁切或清晰度问题时，才人工修图、改用 README 专用版本或请用户确认替换。

### 4. 准备 Hero

素材优先级：

1. 能准确代表产品的现有截图或宣传图。
2. 项目已有品牌资产组合出的 Hero。
3. 根据真实产品特征制作的新 Hero。
4. HTML／CSS 或 SVG 排版渲染兜底。

要求：

- 推荐 16:9，清晰且文件大小合理；PNG、WebP 或 SVG 服从项目实际需要。
- 默认只用一张 Hero。第二张图必须提供不可替代的新信息。
- Hero 有真实 Demo 时链接到 Demo；App 项目可链接到下载章节或直接下载地址。
- 中文为主的 README，Hero 中的产品说明、宣传语和界面说明也以中文为主。
- AI、Prompt、System Prompt、V1.md、Markdown、SQLite、API Key、macOS、模型名、产品名和文件名等技术名词可保留英文。
- 不在中文项目的 Hero 中塞入整段英文营销口号。
- 生成式图片不适合承载必须逐字准确的密集文字；文字准确性重要时，优先使用 HTML／CSS、SVG 或后期排版。
- 渲染后实际检查文字、缩放清晰度、亮／暗背景表现、图标边缘和链接。

只有本任务需要新建或编辑位图时，才使用图像生成工具。复用已有图或修改 SVG／HTML 时不需要为了形式重新生成。

### 5. 组装正文

公开产品 README 的常用结构：

```markdown
<div align="center">

<img src="assets/app-icon.png" width="96" alt="PROJECT_NAME 图标">

# PROJECT_NAME

**一句话定位**

[![License](LICENSE_BADGE)](LICENSE_URL)
![Platform](PLATFORM_BADGE)
![Release](RELEASE_BADGE)

<br>

[产品简介](#intro) · [产品截图](#screenshots) · [核心功能](#features) · [安装运行](#install) · [关于](#about)

<br>

[![PROJECT_NAME 主视觉](assets/banner.webp)](#install)

</div>

<a id="intro"></a>
## 产品简介

[1–2 段讲清用户、场景和结果。]

<a id="features"></a>
## 核心功能

[只写用户能感知的核心能力。]

<a id="install"></a>
## 安装运行

[直接下载入口、最短安装步骤和必要的首次打开说明。]

## License

[MIT](LICENSE) — use it, fork it, ship it.

---

<div align="center">

**Built with ❤️ by [@AUTHOR](AUTHOR_URL)**

[Download](DIRECT_DOWNLOAD_URL) · [Release Notes](RELEASE_URL) · [Report Issues](ISSUES_URL)

</div>
```

这是结构参考，不是必须逐字套用的模板：

- 导航只链接真实存在的章节，并使用稳定锚点。
- `产品截图`、`技术亮点`、`项目结构`、`Credits` 等仅在有信息价值时加入。
- `开发与验证`、构建测试命令、测试数量和“第一阶段手工验收”默认不放在面向用户的项目主页。
- 用户明确面向贡献者时，再加入 Development、Testing、Contributing 或链接到独立文档。
- 没有 Demo、下载包、Credits 或作者链接时，直接省略，不保留空壳。

### 6. 处理 Releases、DMG 与安装说明

如果项目提供桌面安装包，读取并遵循 [references/release-and-install.md](references/release-and-install.md)。关键规则：

- 同时检查仓库文件和 GitHub Release assets。
- README 的下载按钮应指向真实安装包，而不是只指向 Releases 列表页。
- 若仓库中存在应发布的 DMG 且用户已授权更新 Release，把它附到匹配的 Release，并再次读取 API 验证。
- Release 中所有公开 DMG 都应在安装／下载区域有可发现入口；不要只让用户猜测或进入多层页面寻找。
- 未签名或未公证的 macOS App，需要简短说明首次打开时如何在“系统设置 → 隐私与安全性”中选择“仍要打开”。

### 7. 处理许可证与页脚

- 只有仓库真实采用 MIT 时才写 MIT。缺少许可证时先确认，不凭偏好补充。
- 用户明确选择 MIT 后，添加标准 `LICENSE` 文件。
- README 中保持简洁：`[MIT](LICENSE) — use it, fork it, ship it.`
- 不默认追加整段中文法律解释；用户明确要求解释时再写。
- 页脚作者名链接到真实个人页或组织页。
- 页脚只放可用入口，例如直接下载、Release Notes、Report Issues、Live Demo。

### 8. 更新 GitHub About 元信息

需要 Description 或 Topics 时读取 [references/seo-best-practices.md](references/seo-best-practices.md)。

- Description 用一句话说明对象、核心能力和差异点，语言跟随主要受众。
- Topics 选择 7–9 个真实、高相关、可检索的词。
- 用户明确要求“同时更新简介／标签”或授权修改仓库时，执行更新并读取仓库确认结果。
- 只要求 README 文案时，不擅自修改 Repository About。

## 验证清单

### 内容

- 项目名、定位、功能、技术栈、许可证和兼容性均有事实依据。
- 首屏能快速回答“是什么”和“下一步去哪”。
- 中文主项目没有不必要的英文营销文案；必要技术名词未被生硬翻译。
- 公共 README 没有内部验收记录、临时说明、私有路径或模板占位符。

### 链接与安装

- 徽章、Hero、导航、License、Docs、Issues、作者页和页脚链接可用。
- 导航锚点在 GitHub 上能稳定跳转。
- 下载链接指向真实 Release asset；文件名、tag 和版本一致。
- 有 DMG 时检查 Release assets，不以本地仓库搜索结果代替线上检查。
- macOS 首次打开说明与项目签名／公证状态一致。

### 视觉

- 小徽章通常 2–5 个，都是事实信号。
- Hero 通常只有一张，缩小后仍清楚，文字无误。
- 项目图标按原文件正常使用；只有实际发现黑角、底色、裁切或模糊时再修正。
- 公开 README 不使用本地绝对图片路径。

### 变更验证

- 查看 `git diff -- README.md LICENSE assets/`，确保没有误删用户内容。
- 必要命令实际执行，或清楚说明未执行原因。
- 修改 GitHub Description、Topics 或 Release 后，再通过 GitHub API／CLI 读取确认。
- 最终交付不声称“已更新线上仓库”，除非 push 或 API 操作确实成功。

## 可选视觉工具

只有需要生成或处理 Hero 时才使用：

```text
templates/banner.html
scripts/gen_infographic.mjs
scripts/convert_webp_assets.mjs
scripts/compress_png_assets.mjs
```

示例：

```bash
node scripts/gen_infographic.mjs /tmp/readme-hero.html assets/banner.png 1920 1080
node scripts/convert_webp_assets.mjs assets/banner.png assets/banner.webp
```

项目已有可靠视觉素材时优先复用。不要为了展示工具能力而生成无必要图片。

## 交付汇报

最终只说明：

- README 的首屏、导航和正文发生了什么变化。
- 使用或新增了哪些视觉资产。
- 下载、Release、安装说明、License、About 和 Topics 哪些已实际更新。
- 哪些链接、图片和命令经过验证。
- 仍需用户决定或补充的真实信息。

不要把内部评分、生成过程和冗长方法论写进 README 或最终汇报。
