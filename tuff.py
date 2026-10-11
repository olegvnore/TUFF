#!/usr/bin/env python3
"""🔥 TUFF METER 3000 — measures your TUFF level. No cap."""
import random
import time

BARS = ["░", "▒", "▓", "█"]

def scan_aura():
    print("🔥 Scanning aura...")
    for i in range(1, 6):
        time.sleep(0.3)
        bar = "█" * i + "░" * (5 - i)
        print(f"   [{bar}] {i * 20}%")
    return random.randint(9000, 9999)

def verdict(level):
    if level >= 9900:
        return "🗿 MAXIMUM TUFF. You mog everyone in a 10km radius."
    if level >= 9500:
        return "💪 ULTRA TUFF. Sigma grindset detected."
    return "🔥 TUFF. Keep grinding, king."

def main():
    print("=" * 45)
    print("   🔥 TUFF METER 3000 🔥")
    print("   certified tuff measuring device")
    print("=" * 45)
    level = scan_aura()
    print(f"\n🗿 TUFF LEVEL: {level}")
    print(verdict(level))
    print("\n💀 Mogging complete. Stay tuff. No cap fr fr.")

if __name__ == "__main__":
    main()
