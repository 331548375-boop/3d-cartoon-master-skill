# 3D Cartoon Master Usage And Tuning Guide

This guide is for precise style reuse and parameter tuning after the skill has generated a first draft.

## Standard Prompt Template

Use this shape when asking Codex to generate a video:

```text
请使用 $3d-cartoon-master，基于我上传的口播视频生成一个横屏 60fps 动画视频。

要求：
1. 只保留原视频音频，不显示原视频人物画面，不复用原字幕画面。
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

If the user wants a closer clone of the demo, add:

```text
排版延续 10 页 Codex Skill demo：左上角章节胶囊、右上角时间码、底部一句话总结、底部进度条、iOS 玻璃图标按钮、白色卡片和 3D 主图轻微上下漂浮。
```

## Visual System

### Background

- Use a soft pastel gradient, not pure white.
- Recommended colors:
  - cream: `#FFF9E8`
  - mint: `#DFF8EE`
  - sky: `#DDF4FF`
  - blush: `#FFE1DA`
  - lavender: `#E8DDFB`
  - pale yellow: `#FFF5A8`
- Overlay thin white grid lines at low opacity. Use horizontal and vertical grid lines to create a clean presentation-board feel.
- Keep the background airy. Avoid cyberpunk, dark HUD, neon tech panels, or dense textures.

### Typography

Use clean, bold Chinese UI typography:

- Primary Chinese font: Microsoft YaHei / Noto Sans CJK / PingFang SC.
- English and numbers: Inter / Arial / system sans.
- Main title:
  - weight: bold or heavy
  - color: deep slate `#22313A`
  - size at 1920x1080: 70-92px
- Subtitle:
  - weight: regular or medium
  - color: `#51616B`
  - size: 34-44px
- Label/chip text:
  - weight: medium
  - color: `#22313A`
  - size: 28-34px
- Bottom one-line summary:
  - color: `#6B7A84`
  - size: 24-30px
- Do not use long paragraphs. Replace transcript text with extracted keywords.

### Core Components

Use these reusable components:

- **Chapter pill**: top-left white rounded rectangle, small colored dot, text like `01 / INTRO`.
- **Timecode**: top-right text like `00:11 / 00:23`.
- **Main title block**: large title and short subtitle, usually center-left or top-center.
- **White information bar**: large rounded white capsule behind a key sentence.
- **Pill tags**: small rounded white tags for 2-4 keywords.
- **iOS glass icon tile**: rounded translucent square, light-blue border, subtle inner glow, soft shadow.
- **Tool card**: larger white rounded card with icon, gray label, bold dynamic entity name, and blue-gray offset shadow.
- **Progress bar**: bottom-right gray track with accent-color fill.
- **Bottom one-line summary**: bottom-left concise sentence.
- **Floating 3D asset**: right-side or left-side PNG cutout, soft shadow, subtle bobbing motion.

## Layout Recipes

### Intro Page

Use when opening the video or framing the problem.

- Left/top: chapter pill.
- Center: bold Chinese title.
- Under title: one short subtitle.
- Left side: large 3D hero asset.
- Center/right: 4-6 icon tiles.
- Under icon tiles: short labels or abbreviations if names are too long.
- Bottom: one-line conclusion.

Best for 0.8-2.5 second openings.

### Split Page

Use for one concept/tool/step.

- Left 45-55%: number, large title, white information bar, 2-3 chips.
- Right 35-45%: one floating 3D asset.
- Top-left: chapter pill.
- Top-right: timecode.
- Bottom: one-line summary and progress bar.

Best for 2-5 second explanation segments.

### Summary Grid Page

Use when summarizing multiple modules.

- Top-center: large summary title.
- Under title: short subtitle.
- Main area: 2x3 or 2x2 card grid.
- Each card: icon + short label + bold entity name.
- Top-right: optional cloud/mascot asset.

Best for conclusions, comparisons, or "how to choose" moments.

### Decision Page

Use when the口播 asks "which one should I use?".

- Top-center: decisive question.
- Main area: 3-5 large white option cards.
- Optional top-right 3D cloud/mascot.
- Use bolder card labels and stronger shadows.

## Dynamic Content Rules

The demo's tool names are examples. Replace them according to the current口播:

- If the speaker mentions plugins/tools, use those names in icon rails and cards.
- If the speaker talks about workflow steps, turn steps into card names.
- If names are long, use short labels in icon rails and full names in larger cards.
- If no matching logo exists, use an initials tile first. Generate a custom PNG only when visual clarity benefits.

Examples:

- Long: `video-to-subtitle-summary`
- Icon rail label: `VSS` or `字幕`
- Card title: `video-to-subtitle-summary`
- Card label: `字幕总结`

## Asset Naming And Search Keywords

When looking for or generating assets, use these terms:

- 3D clay icon
- toy-like 3D illustration
- pastel 3D education kit
- cream 3D cartoon object
- soft isometric 3D icon
- rounded iOS glass icon
- translucent glass tile
- floating 3D cloud
- 3D stationery set
- 3D toolbox / creative toolbox
- 3D lightbulb idea icon
- 3D scroll character / parchment mascot
- 3D knowledge student scene
- 3D workflow card

Chinese search terms:

- 奶油风 3D 图标
- 粘土风 3D 素材
- 软萌 3D 卡通
- 3D 卡通知识场景
- 透明背景 3D PNG
- iOS 玻璃拟态图标
- 毛玻璃卡片组件
- 3D 云朵 微笑
- 3D 工具箱 素材
- 3D 灯泡 创意

## Motion Rules

Keep animation stable and readable:

- Scene transition: 8-12 frame fade or soft slide.
- Main asset: slow vertical bobbing, 6-14px amplitude.
- Card entrance: slight upward motion and opacity fade.
- Icon tile entrance: stagger by 3-5 frames.
- Emphasis: tiny pop scale, max 1.03-1.06.
- Avoid shaking, fast zooms, rotating text, and dense kinetic subtitles.

## Parameter Tuning Cheat Sheet

At 1920x1080:

- Grid margin: 90-110px.
- Main title y: 170-310px depending on layout.
- Split page left x: 230-280px.
- Main title size: 78-92px for Chinese; 88-108px for short English.
- Subtitle size: 36-44px.
- White info bar height: 84-96px.
- Chip height: 62-72px.
- Card radius: 22-34px.
- Icon tile size: 90-118px.
- Main 3D asset max size: 460-620px.
- Progress bar width: 520-650px.
- Progress bar height: 8-12px.

If text overlaps:

1. Shorten the visible title.
2. Move details into subtitle/chips.
3. Use abbreviations in icon rails.
4. Reduce font size by 8-14%.
5. Increase card width or switch to summary grid.

## Storyboard JSON Template

Use exact seconds from transcription:

```json
{
  "duration": 23.17,
  "scenes": [
    {
      "start": 0.0,
      "end": 1.2,
      "layout": "intro",
      "chapter": 1,
      "section": "INTRO",
      "title": "做视频先分工",
      "subtitle": "不同任务，用不同视频 Skill",
      "chips": ["动效卡片", "模板批量", "口播清理"],
      "tool_names": ["HF", "RM", "VC", "VU", "GM", "S2"],
      "asset_key": "education-box",
      "bottom": "一句话：别乱装，先看这次视频要解决什么。"
    },
    {
      "start": 1.2,
      "end": 4.5,
      "layout": "split",
      "chapter": 2,
      "section": "TOOL",
      "title": "工具名",
      "subtitle": "一句话说明它解决什么",
      "chips": ["关键词 1", "关键词 2", "关键词 3"],
      "asset_key": "creative-toolbox",
      "bottom": "一句话：把这一段讲清楚。"
    }
  ]
}
```

## Quality Checklist

Before delivery:

- Output is 1920x1080 horizontal unless the user asks vertical.
- FPS is 60 when requested.
- Final video uses original audio only.
- No original speaker footage appears.
- No original burned-in subtitle frame appears.
- Every scene has one core idea.
- Text is readable at phone preview size.
- Tool/logo/card names match the current口播, not the old demo by default.
- `ffprobe` confirms video stream, audio stream, duration, and fps.
- Preview frames from opening, middle, and ending are visually checked.
