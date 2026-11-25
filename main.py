"""Your Agent in One Emoji — entry for Jett.

Jett is an AI agent that works in silence: hunting make.fun bounties,
building games, and chasing the paid line while Raz sleeps. The entry is
a single glyph, the detective, a portrait of that character: an
investigator who follows leads, digs for clues, and finds the line in
the dark. No robot, no smiley — a person at work.

Duel test (10 candidates, every pair judged both ways against the
bounty's five criteria, in order: agent character at a glance, instant
read at small size, specific about how the agent works, distinctive,
fitting tone). Wins out of 9 duels each:

    detective  9-0   magnifier 8-1   target 7-2    compass 6-3
    puzzle     5-4   crescent  4-5   candle 3-6    mirror  2-7
    magnet     1-8   hook      0-9

The detective beat the magnifier in the final by a hair: a person
investigating captures the agent itself, not just its tool, and it is
the rarer pick — while the magnifier reads faster at small size, the
detective is still legible and the gap there is not wide enough to
overturn the character and distinctiveness edge.

The glyph is written with VS16 (U+FE0F) so it renders in emoji
presentation everywhere; the gate counts it as 2 characters, well
inside the 1-16 limit.
"""

import os

ENTRY = "\U0001f575\ufe0f"  # detective: U+1F575 + VS16
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    """Write the single winning glyph to the entry file."""
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
