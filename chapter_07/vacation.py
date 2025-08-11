responses = {}
while True:
    name = input("What's your name? ")
    place = input("If you could visit one place, where would you go? ")
    responses[name] = place
    repeat = input("Enter another response? (yes/no): ")
    if repeat.lower() != "yes":
        break

print("Poll results:")
for n, p in responses.items():
    print(f"{n.title()} would like to visit {p.title()}.")
