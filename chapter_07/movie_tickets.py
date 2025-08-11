while True:
    age_text = input("Enter your age (or 'quit'): ")
    if age_text.lower() == "quit":
        break
    age = int(age_text)
    if age < 3:
        print("Ticket is free.")
    elif age <= 12:
        print("Ticket is $10.")
    else:
        print("Ticket is $15.")
