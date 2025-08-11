sandwich_orders = ["tuna", "pastrami", "veggie"]
finished_sandwiches = []
while sandwich_orders:
    current = sandwich_orders.pop(0)
    print(f"I made your {current} sandwich.")
    finished_sandwiches.append(current)
print("Finished:", finished_sandwiches)
