name = input("What is your name? ")
with open("guest.txt", "w", encoding="utf-8") as f:
    f.write(name + "\n")
print("Thanks, entry saved.")
