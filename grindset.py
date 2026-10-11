#!/usr/bin/env python3
"""🧠 GRINDSET QUOTE GENERATOR — infinite wisdom. No cap."""
import random

QUOTES = [
    ("Sleep? Never heard of her.", "Sun Tzu probably"),
    ("The grind never stops. Neither do I. I am the grind.", "Anonymous sigma"),
    ("Mewing is not a habit. Mewing is a lifestyle.", "Dr. Mew"),
    ("They asked me for work-life balance. I gave them work.", "CEO of Grind"),
    ("Rest days are for the weak. And the smart. But mostly the weak.", "Gym Bro Stoic"),
    ("My jawline can cut diamonds. My code can cut deeper.", "10x Developer"),
    ("I don't chase. I attract. Except bugs. Bugs chase me.", "Senior Debugger"),
    ("Wake up at 3AM. Grind. Sleep is a myth invented by HR.", "Hustle Culture Manual"),
    (" mogged ", "everyone, after seeing this repo"),
    ("Stay tuff.", "Ancient proverb"),
]

def main():
    q, author = random.choice(QUOTES)
    print(f'\n  🗿 "{q}"')
    print(f"     — {author}\n")
    print("  Run again for more wisdom. The grind provides. 🔥")

if __name__ == "__main__":
    main()
