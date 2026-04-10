import pytest

class Employee:
    def __init__(self,first_name,last_name,salary):
        self.first_name = float(first_name)
        self.last_name = last_name
        self.salary = salary
    
    def give_raise(self,increment=''):
        if increment:       #默认加薪5000元
            self.salary += 5000
            return self.salary
        
        else:               #加薪所输入的其它值
            self.salary += float(increment)
            return self.salary

@pytest.fixturem 
def first_employee():
    """创建一个供多个测试使用的实例"""
    my_employee = Employee('alice','green',9000)
    return my_employee

def test_give_default_raise(first_employee):  
    """测试加薪默认值5000元""" 
    assert my_employee.give_raise == 14000

def test_give_custom_raise(first_employee):
    """测试加薪其它值,如6000元"""   
    my_employee.give_raise(6000)
    assert my_employee.give_raise == 15000
