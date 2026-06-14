# 3D Cartoon Master Skill

把口播视频生成音画同步的奶油风 3D 卡通知识卡片视频的 Codex Skill。

这个 Skill 适合把一段口播 / 讲解视频变成：

- 横屏 3D 卡通知识视频
- 不显示原视频人物画面
- 不复用原视频字幕画面
- 只保留原视频音频
- 根据口播节奏自动切分页面
- 每页只提炼核心词 / 短句
- 使用奶油白、浅薄荷、淡黄、天蓝、珊瑚粉、浅紫等柔和配色
- 使用 3D clay / toy-like 图标、iOS 玻璃卡片、进度条、章节胶囊等组件

## 下载

请下载：

```text
release/3d-cartoon-master-skill-lite.zip
```

这是轻量版，小于 25MB，适合 GitHub 网页直接上传和下载。

## 安装方法

1. 找到你的 Codex skills 目录：

Windows 通常是：

```text
C:\Users\你的用户名\.codex\skills
```

macOS / Linux 通常是：

```text
~/.codex/skills
```

2. 解压 `3d-cartoon-master-skill-lite.zip`。

解压后目录结构应该是：

```text
.codex/skills/3d-cartoon-master/SKILL.md
.codex/skills/3d-cartoon-master/assets/
.codex/skills/3d-cartoon-master/references/
.codex/skills/3d-cartoon-master/scripts/
.codex/skills/3d-cartoon-master/agents/
```

3. 重启 Codex，或者刷新技能列表。

4. 在聊天框里调用：

```text
请使用 $3d-cartoon-master，基于我上传的口播视频生成一个横屏 60fps 动画视频。
```

## 推荐提示词

```text
请使用 $3d-cartoon-master，基于我上传的口播视频生成一个横屏 60fps 动画视频。

要求：
1. 只保留原视频音频，不显示原视频人物画面，也不要复用原字幕画面。
2. 先提取逐字稿和时间轴，按真实说话节奏切分场景。
3. 画面做成软萌奶油 3D 卡通知识卡片风：
   - 奶油白 / 浅薄荷 / 淡黄 / 天蓝 / 珊瑚粉 / 浅紫渐变背景
   - 细白色网格线
   - 圆润 3D clay/toy-like 主图，轻微等距视角，柔和打光，软阴影
   - 中文标题清晰，深灰/黑色
   - 每个场景只表达一个核心意思
   - 大标题 + 短副标题 + 一个 3D 图标/主图 + 少量标签/卡片
4. 不要满屏字幕，只提炼每段核心词/短句。
5. 最终导出 MP4，音频必须和动画节奏同步。
```

## 可精调内容

你可以继续要求 Codex 精调：

- 背景颜色
- 字体大小
- 中文标题
- 关键词标签
- 3D 主图素材
- LOGO / 工具名 / 卡片名
- 进度条
- 章节胶囊
- iOS 玻璃图标按钮
- 单页排版
- 整体动效

例子：

```text
请只修改第 3 页 / 时间段 00:08-00:12 的画面，其它页面保持不变。

这一页我想改成：
- 标题：先判断任务
- 副标题：别先问哪个 Skill 最强
- 关键词标签：写内容 / 剪素材 / 补素材
- 主图素材：3D 奶油风小机器人拿着清单
- LOGO/卡片：替换成当前口播里提到的工具名

排版要求：
- 左文右图
- 不要放整段字幕
- 保持奶油风 3D 卡通知识卡片风格
- 保持原时间轴和音频同步
```

## 依赖说明

建议本地具备：

- Codex
- Python
- ffmpeg
- ffprobe

可选增强：

- HyperFrames
- Remotion
- video-master
- video-use
- video-to-subtitle-summary
- ai-video-transcriber
- imagegen

如果缺少某些视频插件，Skill 会尽量使用本地脚本作为 fallback。

如果缺少某个 3D 素材，可以让 Codex 调用 imagegen 生成透明 PNG 素材。

## 轻量版和完整版区别

轻量版移除了 `assets/source/` 原始素材备份目录。

保留内容包括：

- 核心 Skill 文件
- 渲染脚本
- 使用说明
- storyboard 规则
- 风格规则
- 核心 3D PNG 素材
- 示例 LOGO 素材
- UI 组件素材

正常使用不受影响。

## 许可证

建议使用 MIT License。

如果你要公开给别人用，可以在 GitHub 仓库里选择 MIT License。
