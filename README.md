# Spicy tantanmen ramen — tall noodle pull, dripping egg (v4)

Entry for the Make.fun bounty
[food-picture-01](https://make.fun/bounty/food-picture-01):
"Make the best-looking food picture".

Version 4 of the entry: a photorealistic spicy tantanmen ramen in a
black speckled ceramic bowl on dark wood. Wooden chopsticks lift tall
glossy noodles high in the centre, a halved jammy egg with a thick
dripping deep-orange yolk sits front-right, vivid red chili-sesame
broth with a glossy oil swirl, savoury minced pork, bright green bok
choy, scallions, sesame and chili flakes, with dramatic steam and warm
bokeh light.

## How it works

`main.py` copies `art.png` byte-for-byte to `/output/entry.png` and
verifies its size and sha256 before writing, so both runs produce
identical bytes.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Files

- `main.py` — the entry program
- `art.png` — the ramen artwork (1024×1024 PNG, 460,137 bytes)
- `LICENSE` — MIT
