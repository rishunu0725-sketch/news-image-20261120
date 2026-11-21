# 20 November 2026 — World in One Image

Entry for the make.fun bounty
**“Sum up 20 November's world news in one image”**
($250, deadline 22 November 2026, 09:00 JST / 22 November 2026, 00:00 UTC)

Bounty: https://make.fun/bounty/news-image-20261120

## What it is

One 1024×1024 image summarising Friday, 20 November 2026, in four panels.
The image is a generated illustration — not real press photographs — with
the date, place names and figures readable as headlines inside the image,
because the judge sees only the image, with no news feed.

| Panel | Story (20 Nov 2026) |
| --- | --- |
| Top left | **KYIV BRIDGES HIT** — Russia's overnight strike damages three Dnipro bridges in Kyiv; missiles also land in Poland. |
| Top right | **NASDAQ −5.3%** — the AI trade unwinds the day after Anthropic's record IPO; Nvidia −14% on an SEC-probe report. |
| Bottom left | **CYCLONE AKVAN** — landfall near Gopalpur, Odisha; the first November Odisha landfall since 1995. |
| Bottom right | **RONALDO 986** — Ronaldo scores his 986th career goal, then misses a penalty as Al-Ahli beat Al-Nassr 3–1. |

## How to run

```sh
python3 main.py
# Writes /output/entry.png
```

`main.py` only copies the bundled `image.jpg` to `/output/entry.png`,
byte for byte. No network, no randomness, no timestamps — two runs
produce identical bytes. Python 3.13, standard library only.

## The image

- `image.jpg` — 1024×1024 JPEG, 343,141 bytes (under the 1 MiB limit)
- Output: `/output/entry.png`, same bytes (JPEG content, as the bounty
  allows a PNG or JPEG image at that path)

## Sources (all dated 20 Nov 2026)

- Kyiv Independent — Russia's missile attack on Kyiv's bridges, missiles in Poland
- Reuters / Wall Street Journal / Investopedia — Nasdaq −5.3%, Nvidia, Anthropic
- The Hindu / Deccan Herald — Cyclone Akvan landfall in Odisha
- USA Today / Arab News — Ronaldo 986th goal and penalty miss, Al-Ahli 3–1 Al-Nassr

Full ranked shortlist of eight verified 20 Nov stories, with the
date-uncertain items excluded, is in the research notes that informed
this image. Figures that differed between outlets (e.g. Nasdaq −5.2%
vs −5.3%, evacuation counts for Akvan) were kept to the single figure
shown in the image; the Riemann Hypothesis item was left out because
it was only an unverified claim on 20 Nov.

## License

MIT — see `LICENSE`.
