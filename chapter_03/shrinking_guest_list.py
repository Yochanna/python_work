guests = ["Katherine Johnson", "Ada Lovelace", "Dorothy Vaughan",
          "Rosalind Franklin", "Marie Curie", "Alan Turing"]

print("Sorry, we can only invite two people for dinner.")

while len(guests) > 2:
    removed = guests.pop()
    print(f"Sorry {removed}, maybe next time.")

for g in guests:
    print(f"{g}, you're still invited.")

guests.clear()
print("Guest list is now empty:", guests)
