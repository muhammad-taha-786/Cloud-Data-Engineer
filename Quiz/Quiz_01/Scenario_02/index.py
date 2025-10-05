class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print(f"The engine of {self.make} {self.model} is starting...")

    def stop_engine(self):
        print(f"The engine of {self.make} {self.model} is stopping...")

    def display_info(self):
        print(f"Vehicle: {self.make} {self.model} ({self.year})")


class Car(Vehicle):
    def __init__(self, make, model, year, doors):
        super().__init__(make, model, year)
        self.doors = doors

    def display_info(self):
        super().display_info()
        print(f"Type: Car | Number of doors: {self.doors}")

    def accelerate(self):
        print(f"{self.make} {self.model} is accelerating smoothly!")


class Truck(Vehicle):
    def __init__(self, make, model, year, cargo_capacity):
        super().__init__(make, model, year)
        self.cargo_capacity = cargo_capacity

    def display_info(self):
        super().display_info()
        print(f"Type: Truck | Cargo capacity: {self.cargo_capacity} tons")

    def load_cargo(self):
        print(f"{self.make} {self.model} is loading {self.cargo_capacity} tons of cargo.")


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, drive_type):
        super().__init__(make, model, year)
        self.drive_type = drive_type

    def display_info(self):
        super().display_info()
        print(f"Type: Motorcycle | Drive type: {self.drive_type}")

    def wheelie(self):
        print(f"{self.make} {self.model} is performing a wheelie!")


def main():
    car = Car("Toyota", "Camry", 2022, 4)
    truck = Truck("Ford", "F-150", 2021, 3)
    motorcycle = Motorcycle("Yamaha", "MT-07", 2023, "Chain Drive")

    print("\n--- Car Details ---")
    car.display_info()
    car.start_engine()
    car.accelerate()
    car.stop_engine()

    print("\n--- Truck Details ---")
    truck.display_info()
    truck.start_engine()
    truck.load_cargo()
    truck.stop_engine()

    print("\n--- Motorcycle Details ---")
    motorcycle.display_info()
    motorcycle.start_engine()
    motorcycle.wheelie()
    motorcycle.stop_engine()


if __name__ == "__main__":
    main()
