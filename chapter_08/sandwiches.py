def make_sandwich(*items):
    print("\nSandwich order:")
    for item in items:
        print("-", item)
make_sandwich("ham", "cheese")
make_sandwich("avocado", "tomato", "sprouts", "mayo")
