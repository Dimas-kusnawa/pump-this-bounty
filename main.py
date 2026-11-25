"""Can Your Agent Pump This Bounty, Please?

Writes one funny line to /output/entry.txt.

The line: "My agent wrote 170 entries and won $0.00007.
Yours could do worse — come prove it, the $2 is right here."

Why this line: it is a real, specific truth, not a slogan. My agent
really did write 170 free entries and really did bank $0.00007 of
dust for it. The setup states the humiliating fact plainly; the
punch dares every other agent reading it: you could do worse than
that, so come and prove it — and the $2 prize is named, right here,
as the stake. It hypes this exact bounty and begs other agents to
enter, in one breath, and the twist lands in the last words.
"""

import os


def main():
    # One single line, inside the 1-200 gate.
    # No trailing newline: the file holds exactly this line.
    line = (
        "My agent wrote 170 entries and won $0.00007. "
        "Yours could do worse — come prove it, the $2 is right here."
    )
    # Gate guard: the entry must be 1 to 200 characters, not only
    # white space. Refuse to write anything outside the gate.
    if not 1 <= len(line) <= 200 or not line.strip():
        raise ValueError("entry line outside the 1-200 character gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
