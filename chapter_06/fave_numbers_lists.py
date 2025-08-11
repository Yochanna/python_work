favorite_numbers = {"alice": [3, 9], "bob": [7], "charlie": [42, 5]}
for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite numbers are:")
    for n in numbers:
        print(f" - {n}")
