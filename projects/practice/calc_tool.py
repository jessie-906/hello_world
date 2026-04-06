def multiply(n):
    return (n*n)


def plus(a,b):
    return a+b


def circle_area(r):
    return (r*r*3.14)

def get_number(prompt):
    while True:
        n=input(prompt)
        if n == "q":
           return None
        try:
           return float(n)
        except ValueError:
           print("请输入正确的数字或q退出")


   

history = []
last_result = None
while True:
    print("==== 简易工具 ====")


    if last_result is not None:
                print("上一次结果",last_result)
    


    print("1. 加法")
    print("2. 平方")
    print("3. 圆面积")
    print("q. 退出")
    print("0.查看历史记录")
    
    choice = input("请选择功能:")
    
       

    if choice == "q":
        break

    elif choice == "1":
        
         a = get_number("请输入第一个数字（q退出）")
         if a is None:
            break 
         b = get_number("请输入第二个数字（q退出）")
         if b is None:
            break
         last_result = (plus(a,b))
         history.append({
            "operation":"plus",
            "a":a,
            "b":b,
            "result":last_result
            })
         print(last_result)
         

    elif choice == "2":
         n = get_number("请输入数字（q退出）")
         if n is None:
            break
         last_result = (multiply(int(n)))
         history.append({
            "operation":"square",
            "n":n,
            "result":last_result
            })
         print(last_result)
         

    elif choice == "3":
         n = get_number("请输入数字（q退出）")
         if n is None:
            break
         last_result = (circle_area(float(n)))
         history.append({
            "operation":"circle_area",
            "n":n,
            "result":last_result
            })
         print(last_result)
         

    elif choice == "0":
      if len(history)  == 0:
         print("暂无历史记录")   
      else:
         print("历史记录：")
         for index, item in enumerate(history,start=1):
            if item["operation"] == "plus":
               print(f"{index}.plus: {item['a']}+{item['b']} = {item['result']}")
            elif item["operation"] == "square":
               print(f"{index}.square: {item['n']}^2 = {item['result']}")
            elif item["operation"] == "circle_area":
               print(f"{index}.circle_area: {item['n']}^2*3.14 = {item['result']}")
    else:
        print("无效选择")
    
    