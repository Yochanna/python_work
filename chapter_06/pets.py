pets = [
    {"type": "dog", "owner": "alice"},
    {"type": "cat", "owner": "bob"},
]
for pet in pets:
    print(f"{pet['owner'].title()} has a {pet['type']}.")
