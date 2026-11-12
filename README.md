# Two Moons

Entry for make.fun **coolest-art-01** — "Make the coolest art".

## The piece

A vermilion torii gate stands in a perfectly still lake at night. Above it
hangs an enormous pale full moon, cropped by the top of the frame; below the
horizon line the moon's reflection swells into a second moon, cropped by the
bottom. Sky and water are the same deep indigo, so the composition reads as
pure geometry: disc, gate, disc — one serene emblem that survives any size,
from poster to thumbnail.

Bold flat illustration with a subtle paper grain. Three colours only:
vermilion, indigo, pale gold. No text.

## How it was made

The artwork was generated with an AI image model, art-directed through
several candidate compositions of the same concept; the strongest variant
was selected by judging it against the competition's criteria (stopping
power, idea, style, craft, small-size readability, including a 300 px
downscale check). The final image was resized to 1024×1024 PNG
(839,674 bytes) with PIL.

## How it runs

The artwork ships as `artwork.b64` — the PNG's bytes base64-encoded as a
single line of text, so the repository holds only text files. `main.py`
(Python 3.13, standard library only) decodes it back to the exact PNG
bytes and writes them to `$MAKEFUN_OUTPUT_DIR/entry.png`
(default `/output`), creating the directory if needed, and verifies the
result is a complete PNG/JPEG image within the 1 MiB limit. Decoding
fixed data makes repeated runs byte-identical by construction.
