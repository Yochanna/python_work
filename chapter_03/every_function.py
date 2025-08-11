items = ["apple", "banana", "cherry"]
items.append("date")
items.insert(1, "blueberry")
print(items)

del items[0]
print(items)

popped = items.pop()
print("Popped:", popped)

items.remove("banana")
print(items)

items.sort()
print("Sorted:", items)

items.sort(reverse=True)
print("Reverse sorted:", items)

items.reverse()
print("Reversed:", items)

print("Length:", len(items))
