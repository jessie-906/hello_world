def plus(a,b):
    return a+b

def minus(a,b):
    return (a-b)

def get_number(prompt):
    while True:
        n=input(prompt)
        if n == "q":
            return None
        
        try:
            return float(n)
        except ValueError:
            print("please enter the correct number or press 0 to exit")

def get_n_an(use):
    while True:
        n=input(use)
        if n == "q":
            return None
        else:
            return n
            

history = []

while True:
    import datetime

    print("==== 简易记账本 ====")

    print("1. income")
    print("2. expenditure")
    print("3. record")
    print("0. exit")
    choice = input("please select the function(press q to exit)：")

    
    if choice == "1":
        use = get_n_an("please enter your use:")
        a = 0
        
        while True:    
            b = get_number("please enter the amount(press q to exit):")
            if b is None:
                break
        
            last_result = (plus(a,b))
            a = last_result

            history.append({
                "type":"income",
                "amount":b,
                "total_income":last_result,
                "description":use,
                "time":datetime.datetime.now()
                })   
        
    elif choice == "2":
        use = get_n_an("please enter your use:")
        a = 0
        while True:
            b = get_number("please enter the amount(press q to exit):")
            if b is None:
                break
            
            last_result = (minus(a,b))
            a = last_result
            history.append({
                "type":"expenditure",
                "amount":b,
                "total_expenditure":last_result,
                "description":use,
                "time":datetime.datetime.now()
                }) 
            
        
    elif choice == "3":
        
        total_income = 0
        total_expenditure = 0
        if len(history)  == 0:
         print("暂无历史记录")   
        else:
         print("历史记录：")

        for index, item in enumerate(history,start=1):
    
            if item["type"] == "income":    
                total_income += item["amount"]
            else:   
                total_expenditure += item["amount"]

        income_by_desc = {}
        expenditure_by_desc = {}

        for item in history:
            desc = item["description"]
            amount = item["amount"]

            if item["type"] =="income":
                if desc not in income_by_desc:
                    income_by_desc[desc] = 0
                income_by_desc[desc] += amount

            else:
                if desc not in expenditure_by_desc:
                    expenditure_by_desc[desc] = 0
                expenditure_by_desc[desc] += amount

        print("=== 收入分类 ===")
        for desc,total in income_by_desc.items():
            print(f"{desc}:{total}:")

        print("=== 支出分类 ===")
        for desc, total in expenditure_by_desc.items():
            print(f"{desc}: {total}")
    
    elif choice == "q":
        break
    
     




