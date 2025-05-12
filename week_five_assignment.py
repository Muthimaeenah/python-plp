# Assignment 1: Design Your Own Class (Smartphone Example) 📱
# Parent Class: Smartphone
class Smartphone:
    def __init__(self, brand, model, battery):
        self.brand = brand
        self.model = model
        self.__battery = battery  # Private attribute

    def charge(self, amount):
        """Increase battery life"""
        self.__battery = min(self.__battery + amount, 100)  # Max battery = 100
        return f"{self.model} charged to {self.__battery}%"

    def get_battery(self):
        """Getter method for private attribute"""
        return f"Battery level: {self.__battery}%"

# Child Class: Android (inherits from Smartphone)
class Android(Smartphone):
    def __init__(self, model, battery, play_store_version):
        super().__init__("Android", model, battery)
        self.play_store_version = play_store_version

    def update_play_store(self):
        return f"Updating Play Store to version {self.play_store_version}"

# Child Class: iPhone (inherits from Smartphone)
class iPhone(Smartphone):
    def __init__(self, model, battery, ios_version):
        super().__init__("iPhone", model, battery)
        self.ios_version = ios_version

    def update_ios(self):
        return f"Updating iOS to version {self.ios_version}"

# Creating objects
android_phone = Android("Galaxy S23", 80, "33.0.13")
iphone = iPhone("iPhone 15", 50, "17.4")

print(android_phone.get_battery())  # Output: Battery level: 80%
print(android_phone.charge(15))  # Output: Galaxy S23 charged to 95%
print(iphone.update_ios())  # Output: Updating iOS to version 17.4

# Activity 2: Polymorphism Challenge (Vehicles Example) 🚗✈️🚢
# Parent Class: Vehicle
class Vehicle:
    def move(self):
        """Method to be overridden"""
        pass

# Child Class: Car
class Car(Vehicle):
    def move(self):
        return "🚗 Driving on the road"

# Child Class: Plane
class Plane(Vehicle):
    def move(self):
        return "✈️ Flying in the sky"

# Child Class: Boat
class Boat(Vehicle):
    def move(self):
        return "🚢 Sailing on water"

# Using Polymorphism
vehicles = [Car(), Plane(), Boat()]

for vehicle in vehicles:
    print(vehicle.move())  
