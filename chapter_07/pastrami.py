sandwich_orders = ["tuna", "veggie", "pastrami", "chicken"]
print("Sorry, the deli has run out of pastrami.")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")
finished_sandwiches = []
while sandwich_orders:
    current = sandwich_orders.pop(0)
    print(f"I made your {current} sandwich.")
    finished_sandwiches.append(current)
print("Finished:", finished_sandwiches)
