current_users = ["ada", "grace", "linus", "guido", "john"]
new_users = ["john", "mike", "ADA", "paul", "jane"]

current_lower = [u.lower() for u in current_users]
for u in new_users:
    if u.lower() in current_lower:
        print(f"{u} is taken, please enter a new username.")
    else:
        print(f"{u} is available.")
