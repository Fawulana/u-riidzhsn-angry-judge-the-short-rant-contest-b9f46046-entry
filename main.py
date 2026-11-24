"""Angry Judge: The Short Rant Contest.

Writes one short, funny rant about a small everyday annoyance to
/output/entry.txt. Deterministic: the rant is hardcoded, no randomness,
no network, no clock, stdlib only (no imports at all).
"""

import os

RANT = (
    # 304 characters: well inside the 400-character gate, no trailing
    # newline so the file holds exactly the rant and nothing else.
    "The self-checkout called me a thief. I scanned one bag of rice and it "
    "screamed \"UNEXPECTED ITEM IN THE BAGGING AREA\" like I had smuggled a "
    "grand piano. Then it froze, summoned a human, and made me stand there "
    "while the whole queue watched. I came for milk. I left with a criminal "
    "record and trust issues."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(RANT)


if __name__ == "__main__":
    main()
