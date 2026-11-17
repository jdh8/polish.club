# Forcing and negative heart bids after 1♦ (1♠)

Checked 17 November 2026. This is research and design analysis, not a change
to the published system. The opening here is the repository's natural 1♦:
five diamonds, or an unbalanced hand with four. Precision precedents are
identified separately because a short diamond changes the costs considerably.

**The current structure already provides the requested distinction:**
[2♦ shows 10+ with five hearts, while 2♥ is nonforcing](../src/1D/Competition.md).
The interesting question is which other call should pay for that distinction.
There are two different objectives:

- **Separate immediate calls:** opener knows at once whether responder has
  forcing or negative-free-bid strength with hearts.
- **One transfer covering both:** responder can stop in 2♥ or continue
  forcing, but opener initially knows the suit rather than the strength.

The first three structures below include alternatives of both kinds.

## 1. Strong 2♦, weak 2♥: keep the present heart split

W. “Tom” Reynolds describes this exact split in his own partnership:
**1♦ (1♠) 2♦ is at least a one-round force with 5+♥; 2♥ is the negative
free bid.** His negative double promises exactly four hearts. In his fuller
Precision structure, 2♣ transfers to diamonds, 2♠ shows a balanced game
force, and clubs move to higher transfers. His weak heart bid has six
cards and weak-two strength. Opener may reject the heart transfer, typically
with a singleton; his listed alternatives show diamonds, clubs, or natural
notrump. This establishes the heart split, not the repository's entire
response table. ([Reynolds, 3–4 November 2025](https://bridgewinners.com/bwcomments/user/w-tom-reynolds/?page=3),
commenting on [*Precision 1D-(1M)-2C*](https://bridgewinners.com/article/view/precision-1d-1m-2c/).)

**Fit here — our analysis.** The present version preserves natural forcing
2♣ and natural 1NT, but spends the natural 2♦ raise. Its constructive
diamond raises therefore start with 2♠ and cannot stop in 2♦. This is a
meaningful cost opposite this long-diamond opening, even though it may be a
smaller issue opposite Precision's short diamond.

The benefit is immediate separation of weak long hearts from stronger
five-card hearts. Unlike a game-force-through-double method, it can retain
a genuinely invitational heart hand without forcing game. The table still
needs to say which continuations are forcing after opener completes 2♥.

## 2. Start transfers at 1NT: keep the split and recover 2♦

DavidKok publishes a version particularly relevant here: his 1♦ promises
five cards except for 4441/1444. After **1♦ (1♠)** his table gives:

| Response | Meaning |
| --- | --- |
| X | 4+♥, 6+ |
| 1NT | 5+♣, 8+ |
| 2♣ | 3+♦, 10+ |
| 2♦ | 5+♥, 8+ |
| 2♥ | 6+♥, 4–7 |

His rules make the artificial calls transfers and explicitly retain the
negative 2♥. Thus clubs consume natural 1NT while the diamond raise can
finish in 2♦. He labels the overall structure a simplified proposal with
some ranges still needing adjustment. ([25 December 2025, post 6 and
linked table](https://www.bridgebase.com/forums/topic/91402-transfer-responses-in-competition/),
[table image](https://i.imgur.com/FhMzQeH.png).)

**Fit here — our analysis.** This is the clearest alternative if retaining
both separate heart calls and a two-level diamond raise matters more than
responding a natural 1NT. The partnership must assign the balanced
8–10-point hand that currently bids 1NT. Moving clubs into that slot does
not make that hand disappear. The 10+ diamond transfer also does not by
itself restore the repository's desired *constructive* diamond raise;
adopting a lower threshold would be a further design choice.

## 3. Switch: use 2♣ for hearts of different strengths

Hinden–Osborne's tournament notes explicitly exchange the unbid suits
after **1m (1♠/2♠)**. Thus **1♦ (1♠) 2♣ shows hearts and 2♥ shows clubs**.
Completing a transfer at the two or three level is regressive: opener is
prepared to play there. Their club-showing 2♥ is not game-forcing.
The card does not supply a complete heart strength/length schedule or the
meaning of opener's intervening 2♦ rebid. ([2025 Champions' Cup card,
note 11, p. 4](https://championships.eurobridge.org/2025CC/Systems/OPEN/O-ENGLAND-HINDEN-OSBORNE.pdf#page=4).)

In an exact-auction discussion, Michael Rosenberg advocates simply making
2♣ show hearts, keeping strong hearts out of double. Michael Roche's
different proposal gives 2♣ the negative-free-bid hands but retains
double-then-hearts for a five-card game force. These are distinct versions,
not interchangeable definitions of Switch. ([19–21 July 2025 discussion](https://bridgewinners.com/article/view/a-negative-free-bid-problem/).)

**Fit here — our analysis.** The all-strength version is attractive because
it preserves a natural 2♦ response and gives opener an extra rebid below
2♥. A weak responder can pass a suitable 2♥ completion; stronger hands
continue. Clubs have to be shown higher, normally through 2♥ to 3♣.
There is no longer a direct natural negative 2♥ response: the same hands
enter through 2♣ instead.

The extra 2♦ rebid is especially useful opposite this natural opening,
but needs an explicit agreement. It could describe a diamond-oriented
minimum unsuitable for hearts; whether responder may then pass it must
also be defined. Neither that suggested meaning nor a full continuation
scheme is established by the cited card. See the existing
[Switch research](1d-1s-2c-hearts.md) for additional named-partnership
evidence of the exact suit exchange.

## 4. Rotate the three suits: diamonds → hearts → clubs

Adam Meyerson gives **1♦ (1♠) 2♣ = 5+♦, 2♦ = 5+♥, 2♥ = 5+♣ INV+**,
with natural 1NT and a four-heart double. His six-card transfers need no
values; five cards generally need 8+. He plays a strong club with very
short diamonds. ([26 December 2025, post 10](https://www.bridgebase.com/forums/topic/91402-transfer-responses-in-competition/).)

**Fit here — our analysis.** This also accommodates weak and strong hearts
through one transfer and keeps a route to 2♦. Compared with Switch,
hearts start one step higher and diamonds one step lower. Compared with
the current table, clubs lose 2♣ and the direct negative 2♥ disappears.
For this repository, lowering the diamond requirement from five cards to
ordinary support would be an adaptation, not Meyerson's published method.

## 5. Natural 2♥ nonforcing; strong hearts through double

Karen Walker's authored treatment uses negative free bids of roughly
5–10 points, sometimes a soft 11, with six cards or a suitable five-card
suit. A negative double followed by a new suit is game-forcing, while a
jump in a new suit is invitational. She explicitly illustrates
**1♦ (1♠) X**, followed by 2♥ or 3♥, with five hearts and game values.
(*Negative Freebids*, [part 1](https://www.kwbridge.com/bb/nfb-1.htm)
and [part 3](https://www.kwbridge.com/bb/nfb-3.htm).)

Macaulay–Iaboni's *Maritime Club* gives the exact auction too: 2♥ is
nonforcing with 5+♥; double followed by 2♥ shows 5+♥ and a game force;
both two-level minor responses remain forcing. ([May 2020 notes,
p. 44](https://sites.utoronto.ca/bridge/convsam/MaritimeClub.pdf#page=44).)

The main hazard is documented rather than hypothetical. David Caprera
reports **1♦ (1♠) X (2♠); X (P) 3♥**, passed with a game-forcing
responder because opener thought the hearts were a weak five-card suit.
His double could contain either hand type. ([19 July 2025](https://bridgewinners.com/article/view/a-negative-free-bid-problem/).)

**Fit here — our analysis.** This spends no artificial suit response, but
delays heart length and strength until competition may have removed the
necessary space. It also needs a home for invitational five-card hearts:
“double then hearts = GF” is stronger than the current 2♦'s “10+”.
Simply writing both weak-five and GF-five hands into double is incomplete
unless the later auctions distinguish them.

## What I would investigate next

For this system, the most promising comparison is **the current split
versus all-strength Switch**. The current split preserves cheap clubs
and immediate heart strength information. Switch restores the natural
diamond raise and gives opener 2♦ below 2♥. DavidKok's structure is the
third candidate if natural 1NT is expendable.

Before adopting any version, settle these specific cases:

1. Five weak hearts too poor for the chosen negative-free-bid standard.
2. Five invitational hearts, not enough to force game.
3. A minimum opener with one heart and long diamonds.
4. A balanced responder with 8–10 points if natural 1NT is reassigned.
5. **1♦ (1♠) transfer (2♠/3♠)**: what do opener's pass and double show,
   and how does responder distinguish competing, inviting, and forcing?

These are design tests, not further agreements found in the sources.
The research establishes usable precedents and their costs; it does not
establish that one scheme wins more often in play.
