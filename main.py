#!/usr/bin/env python3
"""food-picture-01 entry (v4): copy the ramen artwork to /output/entry.png.

Photorealistic spicy tantanmen ramen: chopsticks lifting tall glossy
noodles high, a halved jammy egg with a thick dripping deep-orange yolk,
vivid red chili-sesame broth with a glossy oil swirl, savoury minced
pork, bright bok choy, scallions and sesame, steam and warm bokeh on
dark wood.
"""
import hashlib
import os

ART_SHA256 = "7d68b0920367ad22db9b610ab474ee638b475ebb686b34607c53a65e59f2a392"
ART_SIZE = 460137


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "art.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    with open(src, "rb") as f:
        data = f.read()
    assert len(data) == ART_SIZE, f"art.png size {len(data)} != {ART_SIZE}"
    assert hashlib.sha256(data).hexdigest() == ART_SHA256, "art.png sha256 mismatch"
    with open(dst, "wb") as f:
        f.write(data)
    print(f"wrote {dst} ({len(data)} bytes, sha256 {ART_SHA256[:12]}...)")
    print("entry ready: spicy tantanmen ramen, tall noodle pull, dripping egg, red broth")


if __name__ == "__main__":
    main()
