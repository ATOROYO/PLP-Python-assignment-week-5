# Base Class: Smartphone
class Smartphone:
    def __init__(self, brand, model, price):
        """
        Initialize a Smartphone object.
        :param brand: Brand of the smartphone (str)
        :param model: Model name (str)
        :param price: Price of the smartphone (float)
        """
        self.brand = brand
        self.model = model
        self.price = price

    def make_call(self, number):
        """
        Simulate making a call.
        :param number: Phone number to call (str)
        """
        return f"{self.brand} {self.model} is calling {number}..."

    def display_info(self):
        """
        Display smartphone details.
        """
        return f"Smartphone: {self.brand} {self.model}, Price: ${self.price:.2f}"


# Derived Class: Smartwatch (Inheritance & Encapsulation)
class Smartwatch(Smartphone):
    def __init__(self, brand, model, price, has_heart_rate_monitor):
        """
        Initialize a Smartwatch object.
        :param has_heart_rate_monitor: Boolean indicating if the smartwatch has a heart rate monitor
        """
        super().__init__(brand, model, price)
        self.__has_heart_rate_monitor = has_heart_rate_monitor  # Encapsulated attribute

    def check_heart_rate(self):
        """
        Simulate checking heart rate.
        """
        if self.__has_heart_rate_monitor:
            return "Measuring heart rate..."
        return "Heart rate monitoring not available."

    def display_info(self):
        """
        Display smartwatch details, overriding the parent method.
        """
        heart_rate_status = "Yes" if self.__has_heart_rate_monitor else "No"
        return super().display_info() + f", Heart Rate Monitor: {heart_rate_status}"


# Demonstration
phone = Smartphone("Apple", "iPhone 15", 999.99)
watch = Smartwatch("Samsung", "Galaxy Watch 6", 299.99, True)

print(phone.display_info())
print(phone.make_call("123-456-7890"))
print(watch.display_info())
print(watch.check_heart_rate())
