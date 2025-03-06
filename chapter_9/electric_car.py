from car import Car as parent_class
from battery import Battery as smaller_variable

class ElectricCar(parent_class):
    """Represent aspects of a car, specific to electric vehicles."""

    def init(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().init(make, model, year)
        self.battery = smaller_variable

    def fill_gas_tank(self):
        print("This car does not take gas.")