from car import Car, ElectricCar

if __name__ == "__main__":
    my_beetle = Car("volkswagen", "beetle", 2016)
    print(my_beetle.get_descriptive_name())

    my_tesla = ElectricCar("tesla", "model 3", 2025)
    print(my_tesla.get_descriptive_name())
