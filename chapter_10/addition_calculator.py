print("Enter two numbers to add (or 'q' to quit).")
while True:
    a = input("First number: ")
    if a.lower() == "q":
        break
    b = input("Second number: ")
    if b.lower() == "q":
        break
    try:
        result = float(a) + float(b)
    except ValueError:
        print("Please enter numbers only.")
    else:
        print("Sum:", result)
