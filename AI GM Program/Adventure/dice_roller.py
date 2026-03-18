import random
import sys

def roll_dice(notation):
    notation = notation.lower().strip()
    modifier = 0

    if '+' in notation:
        parts = notation.split('+')
        notation = parts[0]
        modifier = int(parts[1])
    elif '-' in notation:
        parts = notation.split('-')
        notation = parts[0]
        modifier = -int(parts[1])

    if 'd' in notation:
        parts = notation.split('d')
        num_dice = int(parts[0]) if parts[0] else 1
        die_size = int(parts[1])
    else:
        print(f"Invalid notation: {notation}")
        return

    rolls = [random.randint(1, die_size) for _ in range(num_dice)]
    total = sum(rolls) + modifier

    mod_str = ""
    if modifier > 0:
        mod_str = f" + {modifier}"
    elif modifier < 0:
        mod_str = f" - {abs(modifier)}"

    print(f"Rolling {num_dice}d{die_size}{mod_str}")
    print(f"  Rolls: {rolls}")

    if num_dice == 1 and die_size == 20:
        if rolls[0] == 20:
            print(f"  *** NATURAL 20! ***")
        elif rolls[0] == 1:
            print(f"  *** NATURAL 1 — GM Intrusion! ***")

    print(f"  Total: {total}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        roll_dice(sys.argv[1])
    else:
        roll_dice("d20")