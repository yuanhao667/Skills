# GitHub Release、DMG 与安装入口

处理桌面 App 的下载、Release 资产和首次安装说明时读取本文件。

## 先查事实

不要只在工作树中搜索 `.dmg` 后就判断“没有安装包”。检查：

1. 仓库中的构建产物或发布目录。
2. GitHub Releases 列表。
3. 对应 Release 的 `assets`、文件名、大小、下载次数和 `browser_download_url`。

使用当前环境可用的 GitHub CLI 或 API，例如：

```bash
gh release list
gh release view TAG --json tagName,name,url,assets
```

若需要机器可读的直接地址，从 `assets[].url`／`browserDownloadUrl` 读取，不凭文件名拼接后直接宣称可用。

## README 下载入口

安装区应同时满足“看得见”和“点一下能下载”：

```markdown
## 安装运行

[**下载最新版 DMG**](DIRECT_DMG_URL)

1. 下载并打开 DMG。
2. 将 App 拖入“应用程序”。
3. 从“应用程序”启动。
```

- 下载按钮直接链接 Release asset，不只链接到仓库首页或 Releases 列表。
- 同一个下载入口可在首屏、安装区和页脚出现，但不要生成多个互相矛盾的 URL。
- Release Notes 链接到对应 Release 页面；Report Issues 链接到 Issues。
- 多架构包要清楚标注 Apple Silicon、Intel 或 Universal，不让用户猜。

## 附加 DMG 到 Release

只有用户要求更新发布资产、或当前“完成发布／补齐下载”任务明确包含这一步时才执行。

1. 确认目标仓库、tag、版本和 DMG 文件。
2. 检查目标 Release 中是否已有同名资产。
3. 上传到匹配的 Release；覆盖同名文件前确认它确实是本次要替换的版本。
4. 再次读取 Release assets，确认文件名、大小和直接下载 URL。
5. 把 README 的链接更新为验证后的 URL。

不要把不同版本的 DMG 附到错误 tag，也不要仅把安装包提交进 Git 仓库而不提供 Release 入口。

## macOS 首次打开

仅在 App 未签名、未公证或实际会触发 Gatekeeper 提示时加入：

```markdown
### 首次打开

如果 macOS 提示无法验证开发者：

1. 先尝试打开一次 App。
2. 打开“系统设置 → 隐私与安全性”。
3. 在安全性提示旁点击“仍要打开”。
4. 再次确认“打开”。

详见 [Apple 官方说明](https://support.apple.com/guide/mac-help/open-a-mac-app-from-an-unidentified-developer-mh40616/mac)。
```

不要引导用户全局关闭 Gatekeeper，也不要默认使用 `xattr`、`spctl --master-disable` 等高风险绕过命令。已签名并公证的 App 不需要制造多余警告。

## 验证

- 下载 URL 返回的是预期安装包，不是 HTML 页面。
- README 中显示的版本与 Release tag 和资产名一致。
- 安装包架构与兼容性声明一致。
- Release 资产更新后线上 API 能重新读到。
- 首次打开说明只描述项目真实会遇到的情况。
