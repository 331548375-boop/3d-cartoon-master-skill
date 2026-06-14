# Imagegen Prompts For Missing Assets

Use `imagegen` only when the current口播 needs a 3D object or icon that is missing from `assets/3d-objects/` or `assets/logos/`.

## Transparent 3D object prompt

```text
Use case: stylized-concept
Asset type: transparent PNG cutout for a pastel 3D cartoon knowledge-card video
Primary request: Generate one {scene_topic} 3D object/icon.
Style/medium: soft pastel 3D clay illustration, toy-like rounded shapes, glossy plastic and soft clay material, friendly professional education-video style
Composition/framing: single centered object, slight isometric/front perspective, generous padding, clean silhouette
Lighting/mood: soft studio lighting, ambient occlusion, subtle contact shadow only on the object
Color palette: mint green, sky blue, cream yellow, coral pink, light lavender
Constraints: no text, no watermark, no brand logo unless provided, no realistic photo, no complex background
Background for removal: perfectly flat solid #00ff00 chroma-key background, no gradient, no floor plane, no shadow on background, do not use #00ff00 in the subject
```

After generation, remove the chroma-key background with the installed imagegen helper and save the final PNG into the active project. If the asset should become reusable, copy it into this skill's `assets/3d-objects/` with a descriptive lowercase filename.

## Dynamic logo/icon tile prompt

```text
Use case: logo-brand
Asset type: app-style icon for an iOS glass tile in a pastel explainer video
Primary request: Create a simple abstract icon representing "{tool_or_topic}".
Style/medium: minimal rounded 3D app icon, soft gradient, clean geometric mark, no tiny details
Composition/framing: centered icon mark, square composition, transparent or chroma-key removable background
Color palette: blue, cyan, mint, violet, soft white highlight
Text: no text unless the user provides exact short initials
Constraints: no official brand impersonation unless the user provided the logo, no watermark, no busy background
```

Prefer initials in code for unknown tools if speed matters. Use imagegen for polished reusable icons.

## Background prompt

Usually generate pastel gradient and grid with code. If a bitmap background is requested:

```text
Use case: productivity-visual
Asset type: 16:9 video background
Primary request: A soft pastel mesh gradient background with subtle white grid lines.
Style/medium: clean modern UI background, cream mint, pale cyan, soft yellow, peach, lavender
Composition/framing: wide 16:9, lots of negative space, no objects
Constraints: no text, no logo, no watermark, no dark cyber style
```
