class User:
    """用户，及其名字，性别等，和登录次数"""
    def __init__(self,first_name,last_name,other:''):
        self.first_name = first_name
        self.last_name = last_name
        self.other = other
        self.login_attempts = 0
    
    def describe_user(self):
        full_name = f"The first name of this user is {self.first_name.title()}"\
            f"\nThe last name of this user is {self.last_name.title()}"
        if self.other:
            # 安全获得 gender，如果没有则使用'unknown'(get()用法)
            #赋值给gender，没有的话下面的 {gender} 则写 {self.other['gender']}(不安全)                                
            gender = self.other.get('gender','unknown')
            print(full_name + f"\nThe gender of this user is {gender}")
        else:        
            print(full_name)

    def greet_user(self):
        print(f"Hello,{self.first_name.title()}.{self.last_name.title()}")
    
    def increment_login_attempts(self):
        self.login_attempts += 1

        
    def reset(self):
        self.login_attempts = 0
