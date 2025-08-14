print("Enter 'q' to quit.")
with open("guest_book.txt", "a", encoding="utf-8") as f:
    while True:
        name = input("Name: ")
        if name.lower() == "q":
            break
        f.write(name + "\n")
        print(f"Welcome, {name}!")
