foods = ["rice", "beans", "bread", "soup", "salad"]

print("The first three items in the list are:")
for f in foods[:3]:
    print(f)

print("\nThree items from the middle of the list are:")
for f in foods[1:4]:
    print(f)

print("\nThe last three items in the list are:")
for f in foods[-3:]:
    print(f)
