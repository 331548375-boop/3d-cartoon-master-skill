---
name: 3d-cartoon-master
description: "Create synchronized pastel 3D cartoon knowledge-card videos from talking-head/oral videos. Use when the user provides a口播视频/audio and wants the same layout style as the 10-page Codex Skill demo: soft pastel grid background, floating 3D clay assets, dynamic tool/logo cards, chapter pills, progress bars, concise Chinese titles, and no speaker footage. Also use when building reusable HyperFrames-compatible video template skills with bundled assets and imagegen fallback for missing 3D PNGs."
---

# 3D Cartoon Master

Turn a talking-head/oral video into a synchronized horizontal pastel 3D cartoon knowledge-card video. Treat the source video as audio, rhythm, and transcript only; do not show the speaker or reuse burned subtitles unless the user explicitly asks.

## Quick Workflow

1. Inspect the source with `ffprobe`: duration, resolution, fps, audio stream.
2. Extract original audio with `ffmpeg`; keep it as the only final voice track.
3. Transcribe speech with the best available path:
   - Prefer `video-to-subtitle-summary`, `ai-video-transcriber`, local `transcribe`, or Faster-Whisper.
   - Use visible subtitles only as a secondary hint; do not crop original subtitle frames into output.
4. Segment the transcript into 6-12 scenes by real speaking rhythm. Short videos can use fewer scenes; do not force all bundled assets to appear.
5. Extract dynamic entities from the口播:
   - tool names, product names, plugin names, workflow steps, feature names, or topic modules.
   - Replace sample names such as HyperFrames / Remotion / videocut with these dynamic entities.
6. Build a storyboard JSON: one main idea per scene, with `title`, `subtitle`, `chips`, `asset_key`, optional `tool_names`, and exact `start/end`.
7. Render with HyperFrames if available. If HyperFrames/Node is unavailable, use `scripts/render_3d_cartoon_master.py` as a deterministic local fallback.
8. Merge original audio, export H.264/AAC MP4, then inspect `ffprobe` and preview frames.

## Required References

Read these files when using this skill:

- `references/style-system.md`: layout rules, components, typography, motion.
- `references/asset-map.md`: bundled asset names and when to use them.
- `references/dependencies.md`: prerequisite skills/plugins/local tools and fallback behavior.
- `references/imagegen-prompts.md`: prompt recipes for missing 3D PNG assets.
- `references/storyboard-schema.md`: JSON schema for the bundled local renderer.
- `references/usage-and-tuning-guide.md`: reusable prompt template and precise tuning notes for components, typography, layout, motion, and dynamic entity replacement.

## Core Style

Use a light cream/mint/pastel gradient background with thin white grid lines. Use clean Chinese typography, iOS-like rounded components, white info bars, pill tags, tool-card grids, and floating 3D clay/toy assets. Keep copy sparse: no full-screen subtitles, no transcript dumps.

Default canvas:

- Horizontal: `1920x1080`, 60fps.
- Upload master if asked: `2560x1440`, 60fps.
- Use H.264, AAC, `yuv420p`, `+faststart`.

## Dynamic Logo Rule

The sample logos and names are placeholders. Never hard-code HyperFrames / Remotion / videocut / video-use / Generative / seedance2 unless the current transcript actually discusses them. For each new video:

1. Detect the entities in the口播.
2. Choose or generate matching icons.
3. Use the detected names in chapter pills, icon rails, summary cards, and decision cards.

If no matching logo exists, create a rounded iOS glass tile with initials, or use `imagegen` to create a matching transparent PNG.

## Missing Asset Rule

If a scene topic needs a 3D object not found in `assets/3d-objects/`, use the `imagegen` skill/tool to generate it in the same style. Generate on a flat chroma-key background and remove the background locally when transparency is needed. Save final project-bound PNGs under the active project folder and, if the user is improving the reusable skill, copy approved assets back into this skill's `assets/3d-objects/`.

## Local Fallback Renderer

After producing a storyboard JSON, run:

```powershell
python C:\Users\33154\.codex\skills\3d-cartoon-master\scripts\render_3d_cartoon_master.py `
  --storyboard path\to\storyboard.json `
  --audio path\to\voice.mp3 `
  --out path\to\output.mp4
```

The renderer creates the same pastel grid, chapter pill, dynamic cards, floating PNG asset, progress bar, and audio-synced MP4. Prefer HyperFrames for richer GSAP/HTML animation when it is installed; use the script when a stable local render is more important.

## Validation

Before final delivery:

- Confirm no original speaker frame appears.
- Confirm no original burned subtitle image appears.
- Confirm major text remains readable at phone-preview size.
- Confirm timing follows the transcript scene boundaries.
- Confirm `ffprobe` reports expected resolution/fps and an AAC audio stream.
