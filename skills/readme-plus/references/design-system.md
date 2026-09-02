# GitHub README 首屏设计系统

在制作或审查项目图标、Shields.io 徽章、章节导航、CTA 和 Hero 时读取本文件。

## 首屏层级

`project-home` 推荐顺序：

1. 项目图标或项目名。
2. 一句话定位。
3. 2–5 个事实徽章。
4. 可选主 CTA。
5. 一行章节导航。
6. 一张可点击 Hero。

名称、定位、徽章和导航可以放在 `<div align="center">` 内；正文恢复左对齐。不要为了模板完整而同时堆叠大 CTA、两行徽章、目录、Hero 和长介绍。

## 项目图标

- 默认直接使用项目正常提供的图标或 Logo。
- 用 GitHub README 的实际背景和尺寸渲染检查。
- 若出现黑角、异常底色、裁切、锯齿或缩放模糊，再人工修图或制作 README 专用版本。
- 不因主观偏好擅自重画品牌图标。
- 使用 `<img>` 时提供准确 `alt`，并控制尺寸，通常为 72–112 px。

## 黑色加彩色徽章

小徽章使用 `flat-square`。左侧标签统一使用深色 `labelColor=111827`，右侧用品牌色或语义色：

```markdown
[![License: MIT](https://img.shields.io/badge/License-MIT-FB923C.svg?style=flat-square&labelColor=111827)](LICENSE)
[![Release](https://img.shields.io/badge/Release-v1.0.0-22C55E?style=flat-square&labelColor=111827)](https://github.com/OWNER/REPO/releases)
![Platform](https://img.shields.io/badge/Platform-macOS-4F8FF7?style=flat-square&labelColor=111827&logo=apple&logoColor=white)
```

优先显示：

- License。
- Release／Build／Deployment 状态。
- Runtime 或平台。
- 1–2 个核心技术。

默认 2–5 个。不要使用无法验证的 `Production Ready`、`Best`、`100%` 等装饰性声明。

### 编码规则

- 空格使用 `_` 或 `%20`。
- 文本中的连字符使用 `--`，避免被 Shields.io 当作分隔符。
- 十六进制颜色不带 `#`。
- 中文和特殊字符使用 URL 编码。
- 使用 Simple Icons 支持的 `logo` 名称，并设置可读的 `logoColor`。
- 可点击徽章用 Markdown 链接包裹；纯事实徽章可以不加链接。

### 颜色语义

| 语义 | 建议方向 |
|---|---|
| Live／Passing／Stable | 绿色或青绿色 |
| License／Attention | 橙色或品牌辅助色 |
| Runtime／Platform | 蓝色或中性色 |
| Technology | 技术官方品牌色或项目品牌色 |

颜色可以跟随品牌，但不能掩盖失败、Beta 或不稳定状态。

## 可选主 CTA

只有当一个动作明显高于其他动作时才使用 `for-the-badge`，每个 README 最多一个：

```markdown
[![立即体验](https://img.shields.io/badge/立即体验-example.com-5EEAD4?style=for-the-badge&labelColor=111827)](https://example.com)
```

可选动作包括 Live Demo、Download、Install、Documentation。没有真实链接时省略。用户偏好章节浏览、或首屏已经有导航和下载区时，可以不使用大 CTA。

## 章节导航

导航保持一行，只包含 4–7 个对读者最有用的章节：

```markdown
[产品简介](#intro) · [产品截图](#screenshots) · [核心功能](#features) · [安装运行](#install) · [关于](#about)
```

为避免中文标题、emoji 或标点导致 GitHub 自动锚点不稳定，在标题前声明短英文锚点：

```markdown
<a id="install"></a>
## 安装运行
```

不要链接不存在的章节，也不要把完整目录塞进首屏。

## Hero

默认只使用一张：

```markdown
[![PROJECT_NAME 主视觉](assets/banner.webp)](#install)
```

规范：

- 推荐 16:9，优先复用真实产品截图或品牌资产。
- 使用真实截图时，不额外覆盖遮挡产品的装饰文字。
- 使用宣传图时，项目名、定位和主体应清楚，避免长段落和密集小字。
- 文案语言跟随 README 受众；中文项目以中文营销与说明文字为主，技术专名可以保留英文。
- 有 Demo 时链接到 Demo；App 可链接到安装章节或直接下载地址；没有目标时可以不包链接。
- `alt` 文字说明项目和图像作用。
- 渲染后检查文字、清晰度、色带、图标边缘和亮／暗背景。

只有第二张图能解释新的关键内容时，才增加功能图、流程图或对比图。

## 正文节奏

- H2 通常 5–8 个。
- 每个说明章节优先 1–3 个短段落。
- 项目结构只展示关键路径，不复制整个仓库。
- 安装和运行命令分别放在独立代码块中。
- 面向用户的产品 README 默认省略开发验证、测试数量和手工验收清单。
- Credits、License 和页脚保持简短。

## 反例

- 两张以上风格相近、信息重复的 Hero／功能图。
- 十几个无链接、无判断价值的技术徽章。
- 只有视觉效果、没有真实目标的大 CTA。
- 章节导航链接空章节或错误锚点。
- 项目图标尚未渲染就被擅自重画，或实际出现异常后仍未修正。
- 图片使用本地绝对路径，或链接到不可公开访问的地址。
- 为了对称保留空章节和模板占位符。
