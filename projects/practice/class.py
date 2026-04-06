

from all_the_class import Restaurant as R
my_restaurant = R('big_restaurant','shandong_cuisine')

print(my_restaurant.describe_restaurant())
print(my_restaurant.open_restaurant())
#restaurant.number_served = 32
#print(f"{restaurant.number_served}")
#restaurant.set_number_served(32)
#print(f"{restaurant.number_served}")
#restaurant.set_number_served(32)
#print(f"{restaurant.number_served}")




my_icecreamstand = IceCreamStand('big_icecreamstand','british_type',['vanilla','chocolate'])
                                            #可直接输入 列表 元组 或 字典 实例，分别用[],(),{}
print(my_icecreamstand.ic_flavors())


           #alice_user = User("alice","black",{'gender' :"woman"})
#alice_user.describe_user()
#alice_user.greet_user()
#alice_user.increment_login_attempts()
#print(f"{alice_user.login_attempts}")
#alice_user.increment_login_attempts()
#print(f"{alice_user.login_attempts}")
#alice_user.reset()
#print(f"{alice_user.login_attempts}")



from all_the_class import Admin     
import all_the_class

first_admin =all_the_class.Admin('bob','write')
print(first_admin.privileges.show_privileges())
