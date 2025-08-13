class Car:
   
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        return f"{self.year} {self.make} {self.model}"

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        if miles >= 0:
            self.odometer_reading += miles


class Battery:
    
    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        
        if self.battery_size == 40:
            r = 150
        elif self.battery_size == 65:
            r = 225
        else:
            r = 200
        print(f"This car can go about {r} miles on a full charge.")


class ElectricCar(Car):
    
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()



if __name__ == "__main__":
    my_leaf = ElectricCar("nissan", "leaf", 2024)
    print(my_leaf.get_descriptive_name())
    my_leaf.battery.describe_battery()
    my_leaf.battery.get_range()
