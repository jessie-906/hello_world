class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        r_name = f"The name of this restaurant is {self.restaurant_name}"
        c_type = f"The type of this restaurant is {self.cuisine_type}"
        return r_name + "\n" + c_type

    def open_restaurant(self):
        return "The restaurant is open."

    def set_number_served(self,number):
        self.number_served += number