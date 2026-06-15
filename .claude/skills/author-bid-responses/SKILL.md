---
name: author-bid-responses
description: >-
  Author the responses to an artificial (!-marked) bid in the Strawberry Polish
  Club mdBook, following repo conventions (WBF abbreviations, -- ranges, the
  useful-space principle) and wiring any new file into SUMMARY.md. Use when a
  call named in a parent file has no authored continuation — a dead-end branch
  that breaks the pons ML import — or when asked to write responses to a specific
  bid such as 1♣-3♦!. Drafts ONE auction at a time and pauses for the user's
  bridge judgment before continuing.
argument-hint: '<auction or list>, e.g. "1♣-3♦!" — or the exported batch of target auctions'
---

# Author bid responses

Write the continuation (the responses) to an artificial call in the Strawberry
Polish Club system, in the repo's house style, so no branch dead-ends.

The list of auctions to work on is **supplied by the user** (exported from their
discovery session). This skill does not hunt for gaps — it authors responses to
the calls it is given. Work through them **one at a time** and stop for review
after each (the user is the bridge authority).

Read **`conventions.md`** (next to this file) once per session for the table
format, the `!` rule, notation, punctuation grammar, and the useful-space
principle. The abbreviation list lives in `book.toml`; `NOTES.md` and
`src/README.md` hold the design principles.

## When to use

- The user exports/points to artificial calls that lack an authored continuation.
- "Write the responses to `1♣-3♦!`" (or any single auction).
- Filling the dead-end branches that made the pons ML import fail.

## Step 1 — Understand the call

1. Locate where the call is **defined**: open the parent file and find its row
   (e.g. `1♣-3♦!` is `src/1C.md:30` → `3♦! | BAL FG, 12--15, 2--3♠, 2--3♥, 3--4♦, 3--4♣`).
   Read the **description cell** for what it shows: strength, suit lengths, and the
   F/INV/FG tag.
2. Read the **header gloss** and the prose above the table for the bidder's range.
3. Reconstruct the **full auction** and get the opener's range from `src/Openings.md`
   or the opening file (e.g. 1♣ = the three variants in `src/1C.md:1-16`).
4. Determine **whose call comes next** and what that hand already knows.

## Step 2 — Find analogues (stay consistent)

- Read the **closest authored continuation in this repo** and mirror its
  step-allocation and tag vocabulary. Good models: `src/1C/2CD.md` (a combined
  file), `src/1C/2H.md` (single response with pass-or-correct), `src/1C/1D.md`
  (file + inline `{#anchor}` sections).
- Optionally consult the sibling systems for prior art before inventing:
  `/home/jdh8/src/blueberry-precision`, `/home/jdh8/src/cranberry-moscito`,
  `/home/jdh8/src/watermelon-dutch` (same conventions).

## Step 3 — Design the responses

- Decide the **target**: are we forcing to game already (FG)? Inviting? Is slam
  live (e.g. opener could be 18+)? That sets which strains/levels matter.
- Apply the **useful-space principle**: give the cheapest steps to the hands that
  most need room; let sign-off / well-described hands spend the dearer steps.
  Responding to an artificial call, the steps are free — allocate deliberately.
- Honor **right-siding** for stopper-asks (let the stopper hand declare notrump).
- Keep the scheme as **small and memorable** as the meaning allows.

## Step 4 — Write the table

- Follow `conventions.md` for file-vs-inline and table grammar (header/body,
  cheapest call first, `!` on every artificial response, glyphs, `--` ranges,
  registered abbreviations, punctuation).
- Add a short **prose paragraph above the table** explaining the scheme and any
  non-obvious choice (every authored file does this).

## Step 5 — Wire into SUMMARY.md (new files only)

Add `- [<short descriptive title>](<relative path>)` under the opener at the
correct **2-space-per-level** indentation, in bid order among its siblings
(model: `src/SUMMARY.md:8-18`). Title is a short name, not the raw auction
(e.g. "Swapped 2♣♦", "Odwrotka 2♦").

## Step 6 — Verify

From the repo root:

- `mdbook build` — must exit 0 (same check as CI; catches a SUMMARY entry that
  points at a missing file and broken intra-book links). Output `./book` is
  gitignored.
- Confirm every relative `](*.md)` / `#anchor` you added resolves to a real file
  and heading.

## Step 7 — Stop for review

After **one** auction, present and wait:

- the auction and **what it shows**,
- the **table** you wrote (and the file path / inline anchor),
- the **SUMMARY.md** line added (if any),
- the **`mdbook build`** result,
- the **bridge reasoning** — why each step got its meaning (useful space,
  right-siding, slam/game targets) — so the user can confirm or correct.

Do not author the next auction until the user signs off. Leave changes unstaged
for the user to review and commit.
