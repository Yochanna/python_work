my_pizzas = ["margherita", "pepperoni", "bbq"]
friend_pizzas = my_pizzas[:] 

my_pizzas.append("hawaiian")
friend_pizzas.append("veggie")

print("My favorite pizzas are:")
for p in my_pizzas:
    print(p)

print("\nMy friend's favorite pizzas are:")
for p in friend_pizzas:
    print(p)
