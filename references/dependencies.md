# Dependencies And Front Package

This skill is a style/workflow skill plus bundled assets. It cannot magically install every plugin on another user's machine, so always check what is available and choose the best path.

## Core recommended package

- `video-master`: route the video workflow, inspect source, choose production path.
- `video-use`: general editing and timeline composition.
- `video-to-subtitle-summary`: quick subtitle/transcript extraction.
- `ai-video-transcriber` or local `transcribe`: ASR fallback.
- `steal-video`: optional source-video structure distillation when the user wants to imitate a creator's scripting pattern.
- `HyperFrames by HeyGen`: preferred renderer for HTML/CSS/GSAP motion cards.
- `Documents`: optional, for DOCX script outputs or prompt packages.
- Local tools: `ffmpeg`, `ffprobe`, Python, Node/npm/npx.

## Optional enhancement package

- `Remotion`: use when the user wants a reusable React video template, batch generation, or data-driven series.
- `videocut`: use when口播 cleaning,口误 recognition, or Jianying draft export is needed.
- `Generative Media` / `muapi-media-generation`: use when external image/video/music generation is explicitly requested.
- `seedance`: use when the user wants AI generated B-roll or cinematic video shots, not just card animation.
- `check-video`: use before publishing to inspect risk, clarity, cover/title/description.
- `muapi-media-editing`: use for AI enhancement/editing of existing media.

## Fallback hierarchy

1. HyperFrames + ffmpeg when plugin and CLI are available.
2. Local script renderer + ffmpeg when HyperFrames or Node is unavailable.
3. Remotion only when React/template maintainability matters.
4. imagegen only for missing PNG assets, not for every UI component.

## User-facing setup note

If a new Codex user has no plugins/skills installed, tell them the minimum useful setup is:

`video-master`, `video-to-subtitle-summary` or `transcribe`, `HyperFrames by HeyGen`, `imagegen`, plus local `ffmpeg/ffprobe`.

The bundled renderer can still create a local MP4 when HyperFrames is absent, as long as Python, Pillow, and ffmpeg are available.
