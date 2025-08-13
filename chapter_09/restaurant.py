class Restaurant:
   
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.name} is now open!")


if __name__ == "__main__":
    r1 = Restaurant("Mama Mia", "Italian")
    r2 = Restaurant("Sushi Lane", "Japanese")
    r3 = Restaurant("Spice Hub", "Indian")

    r1.describe_restaurant()
    r2.describe_restaurant()
    r3.describe_restaurant()
