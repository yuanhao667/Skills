# GitHub About：Description 与 Topics

需要撰写、建议或直接更新 GitHub Repository About 时读取本文件。

## Repository Description

用一句话说明：为谁或在哪个平台，解决什么问题，最关键的能力是什么。

推荐结构：

```text
[对象／平台] + [核心产品类型]，支持 [2–3 个关键能力]。
```

示例：

```text
本地原生 macOS Prompt 工作台，支持结构化编辑、AI 对照与不可变版本管理。
```

规则：

1. 语言跟随项目主要受众；中文项目不强制改成英文。
2. 一句话说清，不堆关键词，不写两段背景。
3. 使用可验证的产品能力，不写“最强”“Amazing”“100%”等评价。
4. 不用多余 emoji 和感叹号。
5. 控制在 GitHub Description 可读长度内，通常不超过 160 个字符。

## GitHub Topics

推荐 7–9 个真实、高相关、能帮助搜索和分类的词。

| 类别 | 建议数量 | 示例 |
|---|---:|---|
| 平台／技术栈 | 2–3 | `macos-app`, `swiftui`, `typescript` |
| 核心能力 | 2–3 | `prompt-management`, `version-control`, `markdown` |
| 应用领域 | 1–2 | `ai-tools`, `developer-tools` |
| 关键集成 | 0–2 | `deepseek`, `openai-api` |

选择规则：

- 用 GitHub 接受的小写连字符格式。
- 项目确实使用或支持该技术时才加入。
- 避免 `software`、`tool`、`project`、`github` 等过宽词。
- 不为了凑数添加相邻但不真实的热门技术。
- 关键词可以与 Description 部分重合；清晰比机械去重重要。

## 执行边界

- 用户要求“帮我写一下”时只交付建议文本。
- 用户要求“更新这个部位”“同时添加标签”或授权修改 GitHub 仓库时，执行更新。
- 更新前确认目标 owner／repo，更新后重新读取 Description 和 Topics 验证。
- README 文件中的 About 章节与 GitHub 侧边栏 About 不是同一项，不要只改 README 后声称侧边栏已经更新。

## README 的可检索性

- H1 使用正式项目名，不堆 SEO 关键词。
- 开头 1–2 句话准确描述项目对象、输入、行为和结果。
- 使用清楚的 H2 章节和可复制命令。
- 数字、性能或支持范围只有可验证时才写。
- 不为搜索引擎牺牲自然语言和阅读节奏。
