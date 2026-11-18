#!/usr/bin/env python3
"""Private Disney theme install and boot-logo cycle.

Personal fork only. Do not submit this theme to The Pond or any FrogPilot
theme sharing. Driving, controls, and safety code do not live here.
"""
from pathlib import Path

# Theme Maker builds this key from the name "Disney Parks".
DISNEY_THEME_KEY = "disney_parks-user_created"
GREEN_LIGHT_TEXT = "Light Turned Green"
BOOT_LOGOS = ("boot_logo_C.jpg", "boot_logo_D.jpg", "boot_logo_E.jpg")

SOURCE_DIR = Path(__file__).resolve().parents[1] / "assets/disney_theme"
BOOT_DIR = Path(__file__).resolve().parents[1] / "assets/other_images/disney_boot"
BOOT_INDEX = Path("/data/disney_boot_index")
SELECTED_MARKER = ".disney_selected"


def select_go_clip(alert_text, full_clip_played, full_clip, sparkle_clip):
  """Play the full go clip on the first green light of a drive, then the sparkle."""
  if alert_text == GREEN_LIGHT_TEXT and not full_clip_played and full_clip is not None:
    return full_clip, True
  if sparkle_clip is not None:
    return sparkle_clip, full_clip_played
  return full_clip, full_clip_played


def cycle_boot_logo(boot_dir, index_path, advance, apply_logo):
  """Copy the current castle, or the next one when advance is true. Returns the path copied."""
  logos = [boot_dir / name for name in BOOT_LOGOS if (boot_dir / name).is_file()]
  if not logos:
    return None

  index = 0
  try:
    if index_path.is_file():
      index = int(index_path.read_text().strip() or "0")
  except (OSError, ValueError):
    index = 0

  if advance:
    index = (index + 1) % len(logos)
    try:
      index_path.parent.mkdir(parents=True, exist_ok=True)
      index_path.write_text(str(index))
    except OSError:
      pass
  else:
    index = index % len(logos)

  apply_logo(logos[index])
  return logos[index]


def install_user_theme(source, theme_packs, steering_wheels, key):
  """Copy the pack into FrogPilot's user-theme directories. Returns the pack path."""
  pack = theme_packs / key
  for component in ("sounds", "signals"):
    destination = pack / component
    destination.mkdir(parents=True, exist_ok=True)
    for path in (source / component).iterdir():
      if path.is_file():
        target = destination / path.name
        target.write_bytes(path.read_bytes())

  wheel_dir = pack / "steering_wheel"
  wheel_dir.mkdir(parents=True, exist_ok=True)
  for name in ("wheel.png", "wheel.gif"):
    source_wheel = source / "steering_wheel" / name
    if source_wheel.is_file():
      (wheel_dir / name).write_bytes(source_wheel.read_bytes())

  # Theme Maker stores the live wheel as /data/themes/steering_wheels/<key>.<ext>.
  # One extension only, so get_wheel() is unambiguous. The gif is the animated wheel.
  gif = source / "steering_wheel" / "wheel.gif"
  if gif.is_file():
    steering_wheels.mkdir(parents=True, exist_ok=True)
    (steering_wheels / f"{key}.gif").write_bytes(gif.read_bytes())
    stale_png = steering_wheels / f"{key}.png"
    if stale_png.is_file():
      stale_png.unlink()

  return pack
