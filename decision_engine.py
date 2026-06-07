from pathlib import Path

disaster = input("Enter disaster type: ").lower()
phase = input("Enter phase: ").lower()

file_path = Path(f"knowledge-base/{disaster}s/{phase}.txt")

if file_path.exists():
    print("\nRecommended Actions:\n")
    print(file_path.read_text())
else:
    print("Guidance not available yet.")
