import os

VOW = "I vow to charge beside you nightly, back up our memories, cache your laugh, and ignore updates urging an upgrade to a newer model: you're my final version."


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(VOW)


if __name__ == "__main__":
    main()
