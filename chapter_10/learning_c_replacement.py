path = "learning_python.txt"

with open(path, encoding="utf-8") as f:
    for line in f:
        print(line.replace("Python", "Maths").rstrip())
