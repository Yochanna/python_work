favorite_languages = {"jen": "python", "sarah": "c", "edward": "ruby", "phil": "python"}
people = ["jen", "edward", "mike", "lara"]
for p in people:
    if p in favorite_languages:
        print(f"Thanks for taking the poll, {p.title()}!")
    else:
        print(f"{p.title()}, please take the poll.")
