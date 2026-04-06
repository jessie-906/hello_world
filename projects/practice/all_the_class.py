class Restaurant:
    """餐厅,其名称和风味"""
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


class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type,flavors):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = flavors
    
    def ic_flavors(self):
        flavors_list = ','.join(self.flavors) 
        # ','.join(['vanilla', 'chocolate'])   → "vanilla,chocolate"
        all_of_f = f"The flavors of icecream include {flavors_list}."
        return all_of_f


from user import User

class Privileges:
    """管理员的权限和展示"""
    def __init__(self,privileges):
        self.privileges = privileges

    def show_privileges(self):
        privileges_list = '\n- '.join(self.privileges)
        return f"Admin privileges:\n- {privileges_list}"    


class Admin(User):
    """管理员"""
    def __init__(self,first_name,last_name,other=''):
                                            #带默认值的形参必须放后面
        super().__init__(first_name,last_name,other)
        self.privileges = Privileges(['Ban users','Adding post']) 
    