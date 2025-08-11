guests = ["Ada Lovelace", "Rosalind Franklin", "Marie Curie"]
print("Good news! We found a bigger table.")

guests.insert(0, "Katherine Johnson")
guests.insert(2, "Dorothy Vaughan")
guests.append("Alan Turing")

for g in guests:
    print(f"Invitation: {g}")
