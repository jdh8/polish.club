# What BBA's opener bids after 1♣ (X) XX

Checked 11 November 2026. The question: in BBA (EPBot), what do opener's calls
mean after 1♣ (X) XX, whether the doubler's partner passes or bids? It is
asked of two of BBA's systems. WJ is the Polish Club. 2/1 is in because our
1♣ can hold weak long clubs, which WJ's 1♣ cannot. How do the answers compare
with the book's list in [Opener.md][book]? The evidence sections record
BBA's book only; the last section is analysis. Nothing here edits the book.

[book]: ../src/1C/Competition/Opener.md

**Conclusion 1.** The two systems agree on the frame. A pass shows a minimum
(11–14) when the next hand bids and extras (13–18) when it passes. A double is
takeout over a one-level suit (in 2/1, over 2♣ too) and penalty over 1NT and
higher. Notrump bids show a stopper: 1NT 11–14, 2NT 13–14, 3NT 14–20.

**Conclusion 2.** In WJ a free new suit shows the strong hand, even 1♥ over
(1♦). The reason is the openings: WJ's 1♥ and 1♠ show 11–17 with 5+ cards, so
a 1♣ that later shows a five-card major must be 18+. In 2/1 a free one-level
suit is natural, 11–18 with 4–5 cards.

**Conclusion 3.** The clubs differ because the 1♣ openings differ. The WJ card
opens 2♣ Precision-style (11–14, 5+♣), so its 1♣ holds no minimum long clubs,
and its free 2♣ shows 15. The 2/1 1♣ can be a minimum with long clubs: its free
2♣ is 11–13 with 6+♣, a jump to 3♣ is 13–18 with 6+♣, and after (P) 2♣ is
11–14 with 6+♣.

**Conclusion 4.** The cuebids differ. In WJ, a cuebid of a minor shows both
majors (5-5 cheapest, 4-4 with a jump) and a cuebid of a major is artificial
with no stated shape. In 2/1 the cheapest cuebid is a strength cuebid
(14–21) and a jump cuebid is artificial.

**Conclusion 5.** None of this has been tested at the table. BBA never
redoubled in WJ: 0 XX in 492 doubles of 1♣. In 2/1 it reached 1♣ (X) XX 90
times in 128,000 boards, and opener's free one-level suit was its most common
action there.

## Method

`probe-bba-book` in [pons][pons] (commit 929dcc74) replays an auction onto an
EPBot with no cards dealt and reads the name and the bands of the rule that
matched (`epbot_get_info_meaning`). The bilans floor never runs, so a reading
is BBA's book, not what it would do with a particular hand. A rule label of
"calculated bid" means no book rule matched. Ranges are EPBot's total points as
it prints them. An upper bound of exactly 18 is how EPBot caps a "strong"
reading and means 18+. The same card sits in all four seats, and everything is
read non-vulnerable; [the pons notes][bba-book] found that vulnerability never
changes a reading.

[pons]: https://github.com/jdh8/pons
[bba-book]: https://github.com/jdh8/pons/blob/main/docs/ai-bidder/bba-book.md

- **WJ:** the card at `~/src/BBA/workspace/WJ.bbsa`. One row, `Strong jump
  shifts 2 = 0`, does not take effect under WJ: EPBot plays 1 whatever the card
  says, and the probe refuses to run on a row that does not take. The run used
  a copy with that row set to 1, which is what EPBot plays anyway.
- **2/1:** EPBot's own defaults (`--card none`). Pons's `cards/American.bbsa`
  gives the same structure; the differences are listed under
  [Card differences](#card-differences).
- **Self-play:** 16 shards of 8,000 boards each, BBA against BBA, counting
  every auction prefix (`--selfplay`). The WJ run used seeds 1762800000 and up;
  the 2/1 run used 1762900000 and up, with each shard's seed offset by 8,000.

```sh
cd ../pons
probe() { target/release/examples/probe-bba-book --vuls none --reach-depth 99 "$@"; }
probe --card WJ.bbsa --prefix "1♣ X XX" --max-depth 5 --extended -o wj.jsonl
probe --card none    --prefix "1♣ X XX" --max-depth 5 --extended -o 21.jsonl
probe --card none    --prefix "1♣ X"    --max-depth 3 --extended -o 21-x.jsonl
target/release/examples/probe-bba-book --card none --selfplay 8000 \
    --seed $((1762900000 + j * 8000)) --output reach-$j.jsonl   # j = 0..15
```

## The systems around the auction

| | WJ | 2/1 |
|---|---|---|
| 1♣ | "Polish 1C", 11–37 | 11–21, 3+♣ |
| 1♥♠ | 11–17, 5+# | 11–20, 5+# |
| 2♣ | Precision, 11–14, 5+♣, 0–4♥, 0–4♠ | strong, 19+ |
| 1♣ (X) XX | "strong", 10+ | penalty, 10+ |
| 1♣ (X) P | artificial, 0–10, 4+♣ | 0–9 |
| 1♣ (X) 1♦ | 0–11, 0–3♣ | natural, 6–17, 4+♦ |
| Self-play: 1♣, 1♣ (X), 1♣ (X) XX | 17,764, 492, 0 | 13,220, 695, 90 |

## Opener after 1♣ (X) XX (bid)

"Theirs" is the suit RHO bid. Lengths are quoted where the reading constrains
them.

| Opener's call | WJ | 2/1 |
|---|---|---|
| Pass | 11–14, any shape | 11–14; 3–5♣ over a one-level suit or 1NT |
| X over 1♦♥♠ | takeout, 14+, 3–5♣, 3–4 in each other suit, 0–4 theirs | takeout, 14–21, same shape |
| X over 2♣ | penalty, 12+, 4+♣ | takeout, 14–21 |
| X over 1NT | penalty, 12+ | penalty, 12–21 |
| X over 2♦♥♠ | penalty: 13+ with 4+♦; 12+ with 4–7 in a major | penalty: 13–21 with 5+♣ and 4–6♦; 12–21 with 4–5 in a major |
| X at the three-level | penalty, 11+, 3+ theirs | penalty, 11–21 |
| 1NT | 11–14, stopper | 11–14, stopper, 3–6♣ |
| 2NT | 13–14, stopper, jump included | 13–14, stopper; over 1NT, 18–19 |
| 3NT | 14–20, stopper | 14–20, stopper; over 1NT or 2♣, 18–21 with 6+♣ ("calculated bid") |
| 2♣ | 15, 5+♣ | 11–13, 6+♣ |
| 3♣ | 18, 5+♣; over 2♦, 15–19; over 2♥♠, 15–16 | jump: 13–18, 6+♣; over 2♦, 11–17; over 2♥♠, 11–16 |
| New suit at the one-level | 18, 5+ | 11–18, 4–5 |
| 2♦ | 18, 6+♦ | 11–15, 5+♣, 5–6♦ |
| 2♥♠ | 18, 5+; over 1NT, 17 with 4= | reverse: 15–18, 4–5; over 1NT, 15–17 |
| Jump to 3♦ | 18, 5+♦ | 14–18, 5+♣, 4–6♦ |
| Jump to 3♥♠ | 18, 6+ | 11–13, 6+♣, 5=M |
| Over 2M or at the three-level, a new suit | 16, 4= | 3♦ shows 5+♣ and 4–6♦; 3♥♠ is 14–16 or 14–18 with 6+♣ and 5=M |
| Cheapest cuebid | of a minor: both majors, 5+♥ and 5+♠, 11+; of a major: artificial, 11+ | strength cuebid, 14–21 |
| Jump cuebid | of a minor: 4+♥ and 4+♠; of a major: artificial | artificial, 11–21 |
| 4♥♠ | 11–14, 4= (4♥ over 3♠: 14–16) | 13–18, 6+♣, 5=M; at the three-level, 11–14 |

## Opener after 1♣ (X) XX (P)

| Opener's call | WJ | 2/1 |
|---|---|---|
| Pass | 13–18, 1–5♣, 1–4♦ | 13–18, 3–5♣ |
| 1♦ | 11–18, 0–3♣, 4+♦ | 11–18, 5+♣, 4–6♦ |
| 1♥♠ | 11–18, 4+ | 11–16, 4–5 |
| 1NT | "minimum", 11–12 | "minimum", 11–12, 3–5♣ |
| 2♣ | 15–18, 5+♣, 0–3♥, 0–3♠ | 11–14, 6+♣ |
| 2♦ | 18, 6+♦ | 17–18, 5+♣, 4–6♦ |
| 2♥♠ | 18, 5+ | 18, 4–5 |
| 2NT | 13–14, stoppers ("calculated bid") | "strong", 18–19 |
| 3♣ | 18, 5+♣ | 15–18, 6+♣ |
| 3♦ | 18, 5+♦ | 18, 5+♣, 5–6♦ |
| 3♥♠ | 18, 6+ | 11–13, 6+♣, 5=M |
| 3NT | 14–20, stoppers ("calculated bid") | 18–21, 6+♣ ("calculated bid") |
| 4♥♠ | 18, 7+ | 13–18, 6+♣, 5=M |

## What 2/1 opener actually bid

From the 90 times 2/1 self-play reached 1♣ (X) XX:

| 1♣ (X) XX … | Times | Opener's calls |
|---|--:|---|
| (1♥) | 32 | 1♠ 16, 1NT 5, 3♣ 3, X 2, P 2, 2♣ 2, 3NT 1, 2NT 1 |
| (1♦) | 19 | 1♥ 6, 2♣ 4, 1NT 3, P 2, 1♠ 2, 2♠ 1, 3♣ 1 |
| (1♠) | 18 | P 5, 2♣ 4, 2NT 2, 1NT 2, 2♥ 2, 3NT 2, X 1 |
| (2♠) | 8 | P 4, 3♣ 4 |
| (P) | 8 | 1NT 7, P 1 |
| (2♥) | 3 | P 2, 3♣ 1 |
| (3♥), (4♥) | 1 each | P |

Of the 82 calls after a bid, 24 were a free one-level suit and 10 were 2♣.
Opener passed 17 times.

## Card differences

Pons's `cards/American.bbsa` keeps both majors to 0–4 in 1♣, so the major-suit
rebids read 4= rather than 4–5. Jumps to 3♥♠ change from 11–13 with 6+♣ and
5=M to 13–18 with 4=M, and 4♥♠ change from 13–18 with 6+♣ and 5=M to 11–14 with
4=M. The cuebids lose their shape bands. Everything else matches EPBot's
defaults.

## Analysis

The previous draft, written from the WJ reading alone and set aside, applied
two choices made for this book. First, every later double by either partner is
penalty, so neither bot's takeout double is adopted. Second, the (P) case gets
its own table. It read:

> When RHO advances, a free new suit shows the strong variant. A minimum 1♣
> with a five-card major would have opened 1M.
>
> - **Pass:** 11–14, any shape
> - **Double:** penalty
> - **Cheapest notrump:** 11–14, stopper
> - **2♣:** 15–16, 5+♣
> - **Other new suit:** 17+, 5+ cards
> - **Cuebid of a major:** forcing, artificial
> - **Cuebid of a minor:** 5+♥ and 5+♠, or 4+♥ and 4+♠ if a jump
> - **3NT:** 15–20, stopper, to play
> - **4♥♠:** 11–14, exactly 4 cards, to play
>
> | 1♣ (X) XX - | |
> |------|-|
> | P    | 13–18, to play
> | 1♦♥♠ | NAT, 4+#
> | 1NT  | MIN, 11–12
> | 2♣   | 11–16, 5+♣, 0–3♥, 0–3♠
> | 2♦♥♠ | 17+, 5+#
> | 2NT  | BAL, 13–14
> | 3♣   | 17+, 5+♣, 0–3♥, 0–3♠
> | 3♦♥♠ | 17+, 6+#
> | 3NT  | 15–20, to play

The 2/1 reading bears on two of these lines.

- **Clubs.** Our 1♣ includes 11–16 with 5+♣, which WJ's 1♣ does not, so WJ's
  15-point free 2♣ leaves our minimum long clubs with no call except pass. 2/1
  handles that hand: a free 2♣ at 11–13 with 6+♣ and a jump to 3♣ with extras.
  After (P) the draft already gives 2♣ the whole 11–16 range, wider than 2/1's
  11–14.
- **Free one-level suits.** WJ's "strong" reading holds for a five-card major
  in our 1♣ too, since our 1♥♠ show 11–16. But our 1♣ can also be 5+♣ with a
  four-card major at 11–16, and 2/1 bids that major freely at the one-level
  (11–18, 4–5). So there is a choice: keep a free one-level major strong (WJ),
  or let it be natural on four cards (2/1), which self-play shows is the
  common action.

The cuebid has three candidates: WJ's majors two-suiter, 2/1's strength cuebid,
and the book's current game-forcing two-suiter with clubs. Neither bot gives a
reason to prefer one, since BBA never got to bid this auction in WJ.
