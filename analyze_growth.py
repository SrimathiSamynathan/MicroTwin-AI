"""Measure stem and root length from a side-on photo of microgreen seedlings.

Setup: photograph the tray from the side against a plain background, with a
ruler or a 5 cm marker in the frame. Roots must be visible (clear tray or
gel). Tune the HSV thresholds below for your lighting.

Usage:
  python analyze_growth.py photo.jpg --cm-per-px 0.02 --seed-line-y 400 --day 6
"""
import argparse
import json

import cv2
import numpy as np

p = argparse.ArgumentParser()
p.add_argument("image")
p.add_argument("--cm-per-px", type=float, required=True, help="5 cm marker length / its pixel length")
p.add_argument("--seed-line-y", type=int, required=True, help="pixel row of the seed or soil line")
p.add_argument("--day", type=int, default=0)
a = p.parse_args()

img = cv2.imread(a.image)
if img is None:
    raise SystemExit("Could not read image")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Shoot: green pixels above the seed line
green = cv2.inRange(hsv, (35, 60, 40), (90, 255, 255))
shoot = green[: a.seed_line_y, :]
# Root: pale, low-saturation pixels below the seed line
pale = cv2.inRange(hsv, (0, 0, 170), (180, 60, 255))
root = pale[a.seed_line_y :, :]


def extent(mask, from_top):
    rows = np.where(mask.sum(axis=1) > 3 * 255)[0]  # ignore stray pixels
    if rows.size == 0:
        return 0
    return (mask.shape[0] - rows.min()) if from_top else (rows.max() + 1)


stem_cm = extent(shoot, True) * a.cm_per_px
root_cm = extent(root, False) * a.cm_per_px

record = {
    "day": a.day,
    "stem_cm": round(stem_cm, 1),
    "root_cm": round(root_cm, 1),
    "root_stem_ratio": round(root_cm / stem_cm, 2) if stem_cm else None,
}
print(json.dumps(record, indent=2))