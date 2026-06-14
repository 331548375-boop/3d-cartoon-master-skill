from __future__ import annotations

import argparse
import json
import math
import subprocess
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont


SKILL_DIR = Path(__file__).resolve().parents[1]
ASSETS = SKILL_DIR / "assets"

OBJECTS = {
    "education-box": ASSETS / "3d-objects" / "education-box.png",
    "creative-toolbox": ASSETS / "3d-objects" / "creative-toolbox.png",
    "student-knowledge": ASSETS / "3d-objects" / "student-knowledge-scene.png",
    "scroll-character": ASSETS / "3d-objects" / "scroll-character.png",
    "idea-lightbulb": ASSETS / "3d-objects" / "idea-lightbulb.png",
    "storyboard-scene": ASSETS / "3d-objects" / "storyboard-scene.png",
    "blue-cloud": ASSETS / "3d-objects" / "blue-smile-cloud.png",
    "white-cloud": ASSETS / "3d-objects" / "white-fluffy-cloud.png",
    "flower": ASSETS / "3d-objects" / "yellow-flower-mascot.png",
    "pink-flower": ASSETS / "3d-objects" / "pink-flower-scene.png",
    "dessert-roll": ASSETS / "3d-objects" / "dessert-roll.png",
}

SAMPLE_LOGOS = {
    "hyperframes": ASSETS / "logos" / "sample-hyperframes.png",
    "hf": ASSETS / "logos" / "sample-hyperframes.png",
    "remotion": ASSETS / "logos" / "sample-remotion.png",
    "rm": ASSETS / "logos" / "sample-remotion.png",
    "videocut": ASSETS / "logos" / "sample-videocut.png",
    "videocut-skills": ASSETS / "logos" / "sample-videocut.png",
    "vc": ASSETS / "logos" / "sample-videocut.png",
    "video-use": ASSETS / "logos" / "sample-video-use.png",
    "vu": ASSETS / "logos" / "sample-video-use.png",
    "generative": ASSETS / "logos" / "sample-generative.png",
    "generative media": ASSETS / "logos" / "sample-generative.png",
    "gm": ASSETS / "logos" / "sample-generative.png",
    "seedance": ASSETS / "logos" / "sample-seedance2.png",
    "seedance2": ASSETS / "logos" / "sample-seedance2.png",
    "seedance2-skill": ASSETS / "logos" / "sample-seedance2.png",
    "s2": ASSETS / "logos" / "sample-seedance2.png",
}

ACCENTS = [
    (156, 79, 245),
    (47, 167, 242),
    (247, 91, 157),
    (38, 204, 190),
    (255, 205, 54),
    (128, 92, 245),
    (65, 199, 232),
]

FONT_DIR = Path("C:/Windows/Fonts")


def font(name: str, size: int) -> ImageFont.FreeTypeFont:
    for p in [FONT_DIR / name, FONT_DIR / "msyh.ttc", FONT_DIR / "simhei.ttf", FONT_DIR / "arial.ttf"]:
        if p.exists():
            return ImageFont.truetype(str(p), size)
    return ImageFont.load_default()


F_TITLE = font("msyhbd.ttc", 86)
F_TITLE_BIG = font("msyhbd.ttc", 96)
F_SUB = font("msyh.ttc", 38)
F_BAR = font("msyhbd.ttc", 36)
F_CHIP = font("msyh.ttc", 28)
F_PILL = font("msyhbd.ttc", 34)
F_SMALL = font("msyh.ttc", 26)
F_LOGO = font("msyh.ttc", 30)


def ease(x: float) -> float:
    x = max(0.0, min(1.0, x))
    return x * x * (3 - 2 * x)


def text_size(text: str, fnt: ImageFont.FreeTypeFont) -> tuple[int, int]:
    box = ImageDraw.Draw(Image.new("RGB", (1, 1))).textbbox((0, 0), text, font=fnt)
    return box[2] - box[0], box[3] - box[1]


def rounded_rect(draw, box, radius, fill, outline=None, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


BG_CACHE: dict[tuple[int, int], Image.Image] = {}
TILE_CACHE: dict[tuple[str, int], Image.Image] = {}
FIT_CACHE: dict[tuple[int, int, int], Image.Image] = {}


def build_background(w: int, h: int) -> Image.Image:
    key = (w, h)
    if key not in BG_CACHE:
        BG_CACHE[key] = _build_background_uncached(w, h)
    return BG_CACHE[key].copy()


def _build_background_uncached(w: int, h: int) -> Image.Image:
    img = Image.new("RGBA", (w, h), (255, 255, 255, 255))
    pix = img.load()
    for y in range(h):
        ny = y / max(1, h - 1)
        for x in range(w):
            nx = x / max(1, w - 1)
            r = int(250 - 25 * ny + 12 * math.sin(nx * math.pi * 1.4))
            g = int(238 + 12 * nx + 16 * (1 - ny))
            b = int(226 + 20 * (1 - nx) + 24 * ny)
            # mint/cyan wash
            g += int(28 * max(0, 1 - abs(nx - 0.52) * 2))
            b += int(28 * max(0, 1 - abs(nx - 0.45) * 2))
            # pale yellow right
            r += int(20 * max(0, nx - 0.64))
            g += int(18 * max(0, nx - 0.64))
            pix[x, y] = (min(r, 255), min(g, 255), min(b, 255), 255)
    layer = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer, "RGBA")
    step = int(w * 0.106)
    x0 = int(w * 0.047)
    y0 = int(h * 0.105)
    x1 = int(w * 0.953)
    y1 = int(h * 0.93)
    for x in range(x0, x1 + 1, step):
        d.line((x, y0, x, y1), fill=(255, 255, 255, 125), width=1)
    for y in range(y0, y1 + 1, int(h * 0.164)):
        d.line((x0, y, x1, y), fill=(255, 255, 255, 125), width=1)
    return Image.alpha_composite(img, layer)


IMG_CACHE: dict[Path, Image.Image] = {}


def load_image(path: Path) -> Image.Image:
    if path not in IMG_CACHE:
        IMG_CACHE[path] = Image.open(path).convert("RGBA")
    return IMG_CACHE[path]


def fit(im: Image.Image, max_w: int, max_h: int) -> Image.Image:
    key = (id(im), max_w, max_h)
    if key in FIT_CACHE:
        return FIT_CACHE[key].copy()
    im = im.copy()
    im.thumbnail((max_w, max_h), Image.Resampling.LANCZOS)
    FIT_CACHE[key] = im
    return im.copy()


def draw_chapter(draw, scene, index: int, accent, w: int):
    text = f"{scene.get('chapter', index + 1):02d} / {scene.get('section', 'PAGE')}"
    tw, th = text_size(text, F_PILL)
    x, y = int(w * 0.038), 52
    rounded_rect(draw, (x, y, x + tw + 68, y + 62), 15, (255, 255, 255, 245))
    draw.ellipse((x + 26, y + 20, x + 48, y + 42), fill=accent)
    draw.text((x + 62, y + 10), text, font=F_PILL, fill=(35, 48, 58))


def draw_timecode(draw, t: float, duration: float, w: int):
    def fmt(s):
        return f"{int(s // 60):02d}:{int(s % 60):02d}"
    draw.text((w - 95, 78), f"{fmt(t)} / {fmt(duration)}", font=F_SMALL, fill=(66, 79, 91), anchor="ra")


def draw_progress(draw, t: float, duration: float, accent, w: int, h: int):
    x0, x1 = int(w * 0.58), int(w * 0.895)
    y = int(h * 0.948)
    draw.rounded_rectangle((x0, y, x1, y + 8), radius=4, fill=(196, 191, 172, 140))
    draw.rounded_rectangle((x0, y, x0 + int((x1 - x0) * min(1, t / duration)), y + 8), radius=4, fill=accent)


def make_icon_tile(name: str, size: int = 110) -> Image.Image:
    cache_key = (name, size)
    if cache_key in TILE_CACHE:
        return TILE_CACHE[cache_key].copy()
    tile = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(tile, "RGBA")
    d.rounded_rectangle((7, 8, size - 5, size - 4), radius=24, fill=(138, 194, 255, 88), outline=(255, 255, 255, 180), width=2)
    d.rounded_rectangle((16, 13, size - 18, size - 18), radius=18, fill=(235, 248, 255, 135))
    key = name.strip().lower()
    logo_path = SAMPLE_LOGOS.get(key)
    if not logo_path:
        for k, p in SAMPLE_LOGOS.items():
            if k in key:
                logo_path = p
                break
    if logo_path and logo_path.exists():
        logo = fit(load_image(logo_path), int(size * 0.55), int(size * 0.55))
        tile.alpha_composite(logo, ((size - logo.width) // 2, (size - logo.height) // 2))
    else:
        initials = "".join([part[:1] for part in name.replace("-", " ").split()[:2]]).upper() or "AI"
        d.text((size / 2, size / 2 + 2), initials, font=font("arialbd.ttf", int(size * 0.28)), fill=(50, 91, 135), anchor="mm")
    TILE_CACHE[cache_key] = tile
    return tile.copy()


def draw_chip(draw, x: int, y: int, text: str):
    tw, _ = text_size(text, F_CHIP)
    rounded_rect(draw, (x, y, x + tw + 48, y + 58), 14, (255, 255, 255, 238))
    draw.text((x + 24, y + 13), text, font=F_CHIP, fill=(43, 55, 64))
    return x + tw + 78


def draw_bottom_caption(draw, scene, w: int, h: int):
    caption = scene.get("bottom") or scene.get("caption") or ""
    if caption:
        draw.text((int(w * 0.048), int(h * 0.955)), caption, font=F_SMALL, fill=(92, 106, 116))


def draw_split_scene(base, scene, index, t, duration):
    w, h = base.size
    accent = ACCENTS[index % len(ACCENTS)]
    d = ImageDraw.Draw(base, "RGBA")
    draw_chapter(d, scene, index, accent, w)
    draw_timecode(d, t, duration, w)
    number = str(scene.get("chapter", index + 1))
    d.text((int(w * 0.08), int(h * 0.215)), number, font=F_TITLE, fill=accent)
    title = scene.get("title", "Untitled")
    d.text((int(w * 0.12), int(h * 0.285)), title, font=F_TITLE_BIG if len(title) < 18 else F_TITLE, fill=(36, 50, 59))
    info = scene.get("subtitle", "")
    if info:
        rounded_rect(d, (int(w * 0.12), int(h * 0.39), int(w * 0.52), int(h * 0.47)), 15, (255, 255, 255, 242))
        d.text((int(w * 0.138), int(h * 0.412)), info, font=F_BAR, fill=(35, 48, 58))
    x = int(w * 0.12)
    for chip in scene.get("chips", [])[:4]:
        x = draw_chip(d, x, int(h * 0.535), chip)
    asset = OBJECTS.get(scene.get("asset_key", ""), OBJECTS["creative-toolbox"])
    obj = fit(load_image(asset), int(w * 0.34), int(h * 0.5))
    float_y = int(math.sin(t * 2.2 + index) * 8)
    base.alpha_composite(obj, (int(w * 0.60), int(h * 0.25) + float_y))
    draw_bottom_caption(d, scene, w, h)
    draw_progress(d, t, duration, accent, w, h)


def draw_intro_scene(base, scene, index, t, duration):
    w, h = base.size
    accent = ACCENTS[index % len(ACCENTS)]
    d = ImageDraw.Draw(base, "RGBA")
    draw_chapter(d, scene, index, accent, w)
    draw_timecode(d, t, duration, w)
    title = scene.get("title", "做视频别乱装 Skill")
    subtitle = scene.get("subtitle", "先搞清楚工具分工，再谈高质量出片")
    d.text((w // 2, int(h * 0.185)), title, font=F_TITLE, fill=(36, 50, 59), anchor="mm")
    d.text((w // 2, int(h * 0.285)), subtitle, font=F_SUB, fill=(83, 99, 110), anchor="mm")
    obj = fit(load_image(OBJECTS.get(scene.get("asset_key", "education-box"), OBJECTS["education-box"])), int(w * 0.27), int(h * 0.52))
    base.alpha_composite(obj, (int(w * 0.08), int(h * 0.30) + int(math.sin(t * 2) * 8)))
    names = scene.get("tool_names", [])[:6]
    if names:
        start_x = int(w * 0.31)
        gap = int(w * 0.085)
        for i, name in enumerate(names):
            tile = make_icon_tile(name, 112)
            x = start_x + i * gap
            y = int(h * 0.39) + int(math.sin(t * 2.2 + i) * 5)
            base.alpha_composite(tile, (x, y))
            d.text((x + 56, y + 144), name, font=F_LOGO, fill=(43, 55, 64), anchor="mm")
    x = int(w * 0.38)
    for chip in scene.get("chips", ["写内容", "剪素材", "批量出片"])[:4]:
        x = draw_chip(d, x, int(h * 0.618), chip)
    draw_bottom_caption(d, scene, w, h)
    draw_progress(d, t, duration, accent, w, h)


def draw_summary_scene(base, scene, index, t, duration, decision=False):
    w, h = base.size
    accent = ACCENTS[index % len(ACCENTS)]
    d = ImageDraw.Draw(base, "RGBA")
    draw_chapter(d, scene, index, accent, w)
    draw_timecode(d, t, duration, w)
    d.text((w // 2, int(h * 0.215)), scene.get("title", "先看内容来源"), font=F_TITLE, fill=(36, 50, 59), anchor="mm")
    if scene.get("subtitle"):
        d.text((w // 2, int(h * 0.30)), scene["subtitle"], font=F_SUB, fill=(83, 99, 110), anchor="mm")
    deco_key = scene.get("asset_key", "blue-cloud" if not decision else "white-cloud")
    deco = fit(load_image(OBJECTS.get(deco_key, OBJECTS["blue-cloud"])), int(w * 0.16), int(h * 0.18))
    base.alpha_composite(deco, (int(w * 0.78), int(h * 0.12) + int(math.sin(t * 2) * 8)))
    cards = scene.get("cards") or scene.get("tool_names") or ["写内容", "剪素材", "补素材", "批量出片", "发布前检查"]
    if decision:
        positions = [(0.12, 0.42), (0.37, 0.42), (0.62, 0.42), (0.12, 0.60), (0.37, 0.60)]
        for i, label in enumerate(cards[:5]):
            x = int(w * positions[i][0]); y = int(h * positions[i][1])
            d.rounded_rectangle((x + 8, y + 14, x + int(w * 0.19) + 8, y + 112), radius=17, fill=(109, 126, 160, 180))
            d.rounded_rectangle((x, y, x + int(w * 0.19), y + 100), radius=17, fill=(255, 255, 255, 248))
            d.text((x + int(w * 0.095), y + 50), str(label), font=F_BAR, fill=(35, 48, 58), anchor="mm")
    else:
        positions = [(0.07, 0.40), (0.37, 0.40), (0.67, 0.40), (0.07, 0.62), (0.37, 0.62), (0.67, 0.62)]
        for i, item in enumerate(cards[:6]):
            name = item["name"] if isinstance(item, dict) else str(item)
            label = item.get("label", "") if isinstance(item, dict) else ""
            x = int(w * positions[i][0]); y = int(h * positions[i][1])
            cw, ch = int(w * 0.25), int(h * 0.145)
            d.rounded_rectangle((x + 8, y + 14, x + cw + 8, y + ch + 14), radius=17, fill=(109, 126, 160, 170))
            d.rounded_rectangle((x, y, x + cw, y + ch), radius=17, fill=(255, 255, 255, 248))
            tile = make_icon_tile(name, 88)
            base.alpha_composite(tile, (x + 34, y + 30))
            d.text((x + 145, y + 42), label or "工具", font=F_LOGO, fill=(83, 99, 110))
            d.text((x + 145, y + 84), name, font=F_BAR, fill=(35, 48, 58))
    draw_bottom_caption(d, scene, w, h)
    draw_progress(d, t, duration, accent, w, h)


def active_scene(scenes, t):
    for i, scene in enumerate(scenes):
        if float(scene["start"]) <= t < float(scene["end"]):
            return i, scene
    return len(scenes) - 1, scenes[-1]


def frame_at(story, t, w, h):
    scenes = story["scenes"]
    duration = float(story.get("duration", scenes[-1]["end"]))
    idx, scene = active_scene(scenes, t)
    p = (t - float(scene["start"])) / max(0.001, float(scene["end"]) - float(scene["start"]))
    base = build_background(w, h)
    overlay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    layout = scene.get("layout", "split")
    if layout == "intro":
        draw_intro_scene(overlay, scene, idx, t, duration)
    elif layout == "summary":
        draw_summary_scene(overlay, scene, idx, t, duration)
    elif layout == "decision":
        draw_summary_scene(overlay, scene, idx, t, duration, decision=True)
    else:
        draw_split_scene(overlay, scene, idx, t, duration)
    fade = min(ease(min(1, p / 0.12)), ease(min(1, (1 - p) / 0.10)))
    overlay.putalpha(overlay.getchannel("A").point(lambda a: int(a * fade)))
    return Image.alpha_composite(base, overlay).convert("RGB")


def run_ffmpeg(cmd):
    subprocess.run(cmd, check=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--storyboard", required=True)
    parser.add_argument("--audio", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--width", type=int, default=1920)
    parser.add_argument("--height", type=int, default=1080)
    parser.add_argument("--fps", type=int, default=60)
    parser.add_argument("--preview-dir")
    args = parser.parse_args()

    story = json.loads(Path(args.storyboard).read_text(encoding="utf-8-sig"))
    duration = float(story.get("duration", story["scenes"][-1]["end"]))
    total_frames = math.ceil(duration * args.fps)
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    silent = out.with_name(out.stem + "_visual_only.mp4")

    cmd = [
        "ffmpeg", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24",
        "-s", f"{args.width}x{args.height}", "-r", str(args.fps), "-i", "-",
        "-an", "-c:v", "libx264", "-preset", "medium", "-crf", "18",
        "-pix_fmt", "yuv420p", str(silent)
    ]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    assert proc.stdin is not None
    for n in range(total_frames):
        frame = frame_at(story, n / args.fps, args.width, args.height)
        proc.stdin.write(frame.tobytes())
        if n % (args.fps * 5) == 0:
            print(f"rendered {n}/{total_frames}")
    proc.stdin.close()
    if proc.wait() != 0:
        raise RuntimeError("ffmpeg visual render failed")

    run_ffmpeg([
        "ffmpeg", "-y", "-i", str(silent), "-i", args.audio,
        "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
        "-shortest", "-movflags", "+faststart", str(out)
    ])

    if args.preview_dir:
        preview = Path(args.preview_dir)
        preview.mkdir(parents=True, exist_ok=True)
        for sec in [0.5, duration * 0.25, duration * 0.5, duration * 0.75, max(0.5, duration - 0.5)]:
            frame_at(story, sec, args.width, args.height).save(preview / f"frame_{sec:05.2f}.jpg", quality=92)
    print(out)


if __name__ == "__main__":
    main()
