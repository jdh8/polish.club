# Strawberry Polish Club — authoring conventions

Quick reference for writing bidding tables. The authoritative sources live in the
repo; this file collects the non-obvious rules in one place. When in doubt, copy
the shape of an existing file.

- **Abbreviations** — the single source of truth is `book.toml`
  `[preprocessor.abbr.list]`. Read it; never invent a tag that is not registered.
- **Design principles** — `NOTES.md` (useful space, right-siding).
- **Hand evaluation & punctuation grammar** — `src/README.md`.

## Suit symbols & input

Type the literal Unicode glyphs **♣ ♦ ♥ ♠** (not tokens). `(R)` renders as the
"relay" abbreviation. The `[preprocessor.replace]` step only colors the glyphs;
there is nothing else to escape.

## The `!` artificial marker

Append `!` with **no space** to any call that does not naturally show the
denomination named: `2♠!`, `3♦!`, `2NT!`, `4M!`, `3♣♦!`. Natural calls get no `!`.
The marker goes after the whole token, including shorthand (`3M!`, `4X!`).

## Table format (GitHub-flavored pipe tables)

- A **header row** is the row directly above the `|---|---|` separator. Cell 1 is
  the auction prefix ending in `-`; cell 2 is a short gloss (usually the bidder's
  range/shape). Example: `| 1♣-2♣- | FG, 5+♦ |`.
- **Body rows**: cell 1 is the call, cell 2 is the dense description. The trailing
  pipe is omitted (repo style): `| 2♦!    | NAT, 11--14 or 18+, 4+♦`.
- Order body rows **cheapest call first** (1♦ before 1♥ … before 3NT).
- Put a short **prose paragraph above each table** explaining the scheme — every
  authored file does this (see `src/1C/2CD.md`, `src/1C/2H.md`).

## Auction → file / anchor

- **File path** mirrors the auction: opening directory + the call. `1♣-2♥` →
  `src/1C/2H.md`; `1♠-2♦` → `src/1S/2R.md` (combined). Letters: ♣→C ♦→D ♥→H ♠→S,
  NT stays `NT`.
- **Inline anchor** for a deeper continuation: `## 1♣-1♦-2♣ {#1C-1D-2C}` — the id
  is the auction with glyphs mapped to letters (`src/1C/1D.md:109`).
- **File vs inline**: a *first response to an opener-level artificial call* (depth
  2, e.g. `1♣-3♦`) gets its **own file** `src/<OPENER>/<CALL>.md`. A continuation
  *under an already-authored response* gets an **inline `## … {#anchor}` section**
  in the existing file.
- **Combined files**: when two calls pair naturally, follow precedent and use one
  file with two tables: `2CD.md` (swapped 2♣/2♦), `2R.md` (red transfers 2♦/2♥),
  `1M.md` (1♥/1♠), `2M.md` (major shorthand). Each table still uses an explicit or
  shorthand auction header.

## Punctuation grammar (`src/README.md`)

- comma `,` = **AND** (all conditions hold): `INV, 9--11, 6+♣`
- semicolon `;` = **OR** (alternatives), often across `<br>` lines
- colon `:` introduces a general description before specifics
- ranges use `--` (smart-punctuation renders an en-dash): `11--19`, `0--3♠`

## Length / shape notation

`5+♣` = 5 or more; `4=♥` = exactly 4; `2--4♠` = 2 to 4; `#` = "the suit" in
context; `M` / `OM` = the major / other major; `m`, `MM`, `mm` = minor(s)/major(s);
`33(43)` = a shape where the parenthesized suits may swap order; `0--1 outside A/K`
= at most one of those honors outside.

## Call-type tags (use only registered ones — see `book.toml`)

`book.toml` `[preprocessor.abbr.list]` is the full registry — read it. The
load-bearing ones for responses: `F`, `INV`, `FG`, `NAT`, `S/O` (signoff),
`P/C` (pass or correct). If you need a concept with no registered tag, describe
it in words rather than inventing an abbreviation.

## Hand evaluation

Methods (HCP, Total points, Fifths, BUM-RAP, NLTC) and stopper definitions live
in `src/README.md` — read it rather than relying on a copy here.

## Fit-promised calls need little authoring

**Fit-promised calls** (e.g. a control slam try in an agreed major) aren't
dead-ends — the fallback is always fleeing to the 8+ fit. A one-line gloss
suffices; don't author an exhaustive continuation.

## Design principles (`NOTES.md`)

- **Useful space** — give the cheapest steps to the hands that most need room to
  explore; make well-described or sign-off hands spend the dearer steps. This is
  *almost an axiom when responding to an artificial call*, where the steps carry
  no natural meaning and the allocation is entirely free.
- **Right-siding tension** — can override useful space. In a stopper-ask, let the
  hand holding the stopper declare notrump (so the lead runs up to it), even at
  the cost of a cheap step.
