guests = ["Ada Lovelace", "Grace Hopper", "Marie Curie"]
print(f"{guests[1]} can't make it.")
guests[1] = "Rosalind Franklin"

for g in guests:
    print(f"Please join me for dinner, {g}.")
