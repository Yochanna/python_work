path = "learning_python.txt"


with open(path, "w", encoding="utf-8") as f:
    f.write("I love learning Python.\n")
    f.write("Python makes working with data fun.\n")
    f.write("Python helps me automate boring stuff.\n")


with open(path, encoding="utf-8") as f:
    contents = f.read()
print(contents)


with open(path, encoding="utf-8") as f:
    for line in f:
        print(line.rstrip())


with open(path, encoding="utf-8") as f:
    lines = f.readlines()
for line in lines:
    print(line.rstrip())
