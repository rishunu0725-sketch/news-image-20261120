"""Entry for make.fun bounty "Sum up 20 November's world news in one image".

Writes the bundled image to /output/entry.png.

Deterministic by design: it only copies the bundled file, byte for byte.
No network, no randomness, no timestamps, no image generation at run time.
Running it twice produces identical bytes.
"""

import shutil
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "image.jpg"
OUTPUT = Path("/output/entry.png")


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, OUTPUT)
    print(f"Wrote {OUTPUT} ({OUTPUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
