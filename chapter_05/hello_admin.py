usernames = ["admin", "ada", "grace"]
for u in usernames:
    if u == "admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {u}, thank you for logging in again.")
