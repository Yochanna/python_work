import json
from pathlib import Path

path = Path("favorite_number.json")
if path.exists():
    number = json.loads(path.read_text(encoding="utf-8"))
    print(f"I know your favorite number! It is {number}.")
else:
    number = input("What is your favorite number? ")
    path.write_text(json.dumps(number), encoding="utf-8")
    print("Got it. I will remember that.")
