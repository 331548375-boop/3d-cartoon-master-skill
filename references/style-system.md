# Style System

## Visual name

Pastel 3D knowledge-card video: light cream/mint canvas, soft 3D clay assets, white grid overlay, iOS-like UI components, clean Chinese typography.

## Canvas

- Default: 16:9 horizontal, `1920x1080`, 60fps.
- Optional upload master: `2560x1440`, 60fps.
- Background: pastel mesh gradient, not pure white.
- Grid: thin white lines, low opacity, about 180-220 px spacing at 1920x1080.
- Safe area: keep top labels and bottom captions away from edges by at least 70 px.

## Palette

- Cream: `#fff7e8`
- Mint: `#d8f5ee`
- Pale cyan: `#dff6fb`
- Soft yellow: `#fff0a8`
- Peach/pink: `#ffd7d0`
- Lavender: `#dfd3ff`
- Main text: `#24313a`
- Secondary text: `#64717c`
- Shadow blue: `#7385a8`

Use one accent color per scene: purple, cyan, pink, teal, yellow, violet.

## Typography

- Chinese: Microsoft YaHei, PingFang SC, Source Han Sans, HarmonyOS Sans.
- English/tool names: Inter, SF Pro Display, Helvetica Neue, Arial.
- Main title: 72-104 px, bold/heavy.
- Large English title: 84-110 px, regular/medium.
- Subtitle/info bar: 34-44 px, bold.
- Chips: 26-32 px.
- Bottom caption: 24-30 px.

## Components

- Chapter pill: top-left white rounded capsule with colored dot, number, and section name.
- Timecode: top-right `mm:ss / mm:ss`, dark gray.
- Info bar: long white rounded rectangle, bold short phrase.
- Chip: small white rounded capsule with short keyword.
- iOS glass icon tile: rounded square, blue translucent base, white highlight, soft shadow.
- Tool card: white rounded card with icon tile, category text, bold tool/entity name, blue-gray offset shadow.
- Decision card: larger white rounded button card with blue-gray offset shadow.
- Progress bar: thin bottom line, pale base track with colored active segment.
- Bottom caption: one concise sentence, not full transcript.

## Layout patterns

1. Intro hero with icon rail:
   - Large title centered top.
   - 3D object on left.
   - 4-6 dynamic tool icon tiles across the middle.
   - Three action chips below.

2. Split hero:
   - Number + big title on left.
   - Info bar and chips below.
   - Large floating 3D object on right.

3. Summary grid:
   - Centered title and subtitle.
   - 2x3 or 2x2 tool cards.
   - Small cloud or decoration in a corner.

4. Decision grid:
   - Centered decision question.
   - 3+2 button cards.
   - Small 3D cloud decoration.

5. Closing CTA:
   - Large 3D object upper right.
   - Centered CTA title and subtitle.
   - Large white CTA bar near lower center.

## Motion

- Scene transition: fade + slight vertical slide.
- Main 3D object: slow float, 6-12 px amplitude.
- Title: quick opacity and small scale pop.
- Cards/chips: staggered slide-in.
- Progress bar: continuous linear advance.
- Avoid shake, fast spin, hard zoom, dense subtitles, and cyber/HUD styling.
