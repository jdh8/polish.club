# Notation on suit variables

In competitive and defensive bidding, combinations of calls grow factorially.
It is convenient to replace unknown suits with variables, just like how algebra
brings computation to a higher level.

This book usually follows principles introduced in BML and [CSS][css].

[css]: https://developer.mozilla.org/en-US/docs/Web/CSS

## Suit variables

x, y, z are suit variables.  They are lowercase so that they never read as
doubles: (1y) X is a double of a suit opening, and 2x is a suit overcall.

A variable stands for the same suit throughout a table, header and body rows
alike.  There are no implicit rules.  Variables are unordered, different
variables may stand for the same suit, and a variable may stand for a suit
already named in the auction.  The second header cell of a table states every
restriction it relies on, such as x < y, x ≠ y, or x ≠ ♠.  Restrictions that
follow from the legality of bids are omitted: (1x) 1y already implies x < y.

For example, given x < y < z:

- (1y) 2x matches (1♥) 2♣ but not (1♥) 2♠.
- (1y) 2z matches (1♥) 2♠ but not (1♥) 2♣ or (1♥) 2NT.

Without restrictions, 1♠ - 4x matches 1♠ - 4♠ as well.  A separate rule for
1♠ - 4♠ still applies there because of precedence.

## Precedence

Multiple rules may match the same auction.  The rule with the highest
precedence applies.

### Precedence of strain symbols

Concrete strain > suit class > suit variable

- Concrete strain: ♣, ♦, ♥, ♠, NT
- Suit class: M, m, <abbr title="red suit">R</abbr>, <abbr title="black suit">B</abbr>
- Suit variable: x, y, z

### Juxtaposition of strain symbols

Juxtaposition of strain symbols produces multiple rules, similar to `|` in
regular expression.  For example, 2MNT is a valid expression that matches
2♥, 2♠, and 2NT.

### Specificity of rules

Specificity is determined like CSS [specificity].  The rule with the most concrete
strains wins.  Then we compare the number of suit classes.  Note that juxtaposition
expands to multiple rules instead of one.  For example:

- 1♥ - 2x > 1R - 2B
- Comparing 1MNT - 2x and 1x - 1R:
  - 1M - 2x = 1x - 1R
  - 1NT - 2x > 1x - 1R

[specificity]: https://developer.mozilla.org/en-US/docs/Web/CSS/Specificity

### Precedence of rules

The most specific rule applies.  If there are multiple rules with the same
specificity, compare specificity lexicographically.  For example, 1M - 2x > 1x - 1R
because 1M is more specific than 1x.  If there are still multiple rules with the
same specificity, the last rule applies, like CSS and laws but not BML.
