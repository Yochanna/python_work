filenames = ["cats.txt", "dogs.txt"]

for fn in filenames:
    try:
        with open(fn, encoding="utf-8") as f:
            print(f"\nContents of {fn}:")
            print(f.read().rstrip())
    except FileNotFoundError:
        
        print(f"\nSorry, {fn} does not exist.")
