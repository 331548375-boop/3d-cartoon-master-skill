# Storyboard JSON Schema

Use this schema before running `scripts/render_3d_cartoon_master.py`.

```json
{
  "duration": 23.17,
  "scenes": [
    {
      "start": 0.0,
      "end": 3.2,
      "layout": "intro",
      "chapter": 1,
      "section": "INTRO",
      "title": "做视频别乱装 Skill",
      "subtitle": "先搞清楚工具分工，再谈高质量出片",
      "chips": ["写内容", "剪素材", "批量出片"],
      "tool_names": ["工具A", "工具B", "工具C"],
      "asset_key": "education-box",
      "bottom": "一句话：先看内容来源，再选工具。"
    }
  ]
}
```

## Layout values

- `intro`: opening page with large title, 3D object, dynamic icon rail, chips.
- `split`: default page with left text and right floating 3D object.
- `summary`: 2x3 tool-card grid.
- `decision`: large decision button grid.

## Asset keys

Use keys from `references/asset-map.md`: `education-box`, `creative-toolbox`, `student-knowledge`, `scroll-character`, `idea-lightbulb`, `storyboard-scene`, `blue-cloud`, `white-cloud`, `flower`, `pink-flower`, `dessert-roll`.

## Dynamic entity fields

- `tool_names`: names extracted from the current口播. Use these for intro icon rails and summary cards.
- `cards`: optional richer summary cards. Each card can be a string or `{ "name": "...", "label": "..." }`.
- `chips`: short labels only. Avoid full sentences.

Do not hard-code the sample tools unless they are actually in the transcript.
