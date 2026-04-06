history = []
history.append(5)
history.append(6)
history.append(2)

for i in history:
    print(i)






for index, item in enumerate(history,start=1):
        
            if item["type"] == "income":    
                total_income += item["amount"]
            else:   
                total_expenditure += item["amount"]

print("1.view all")
print("2.only view income")
print("3.only view expenditure")



if choice == "1":        
            print("--------")
            
            print(f"Total Income: {total_income}({item['description']})")
            
            print(f"Total Expenditure: {total_expenditure}({item['description']})")
            print(f"Balance: {total_income - total_expenditure}")
            print(f"time:{item['time']}")

elif choice == "2":
            print("--------")
            if item["type"] == "income":
                print(f"Total Income: {total_income}({item['description']})")
                print(f"time:{item['time']}")
            
elif choice == "3":
            print("--------")
            if item["type"] == "expenditure":
                print(f"Total Expenditure: {total_expenditure}({item['description']})")
                print(f"time:{item['time']}")  



choice = input("please select the function(press q to exit):")