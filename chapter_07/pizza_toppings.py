prompt = "Enter a topping (or 'quit' to stop): "
while True:
    topping = input(prompt)
    if topping.lower() == "quit":
        break
    print(f"Adding {topping}.")
