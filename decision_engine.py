from pathlib import Path

disaster = input("Enter disaster type: ").lower()
phase = input("Enter phase: ").lower()

file_path = Path(f"knowledge-base/{disaster}s/{phase}.md")

if file_path.exists():
    print("\n" + "="*50)
    print(file_path.read_text(encoding="utf-8"))
    print("="*50)
else:
    print("Guidance not available yet.")
