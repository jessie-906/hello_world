from pathlib import Path
import json

def get_user_information(path):
    """Get the user's information"""
    if path.exists():
        contents = path.read_text()
        all_the_information = json.loads(contents)
        return all_the_information
    else:
        return None

def get_new_user_information(path):
    """Prompt the user to enter the username"""
    first_name = input("What's your first name? ")
    last_name = input("What's your last name? ")
    user_gender = input("What's your gender? ")    
    information = {
        "first_name":first_name,
        "last_name":last_name,
        "user_gender":user_gender,
    }   
    return information

def greet_new_users(path):
    information = get_new_user_information(path)
    store_information(path,information)
    reply = ''
    for key, value in information.items():
        reply += f"\n{key}:{value}"          
    return "We'll remember your information:" + reply 

def store_information(path,information):
    """store user's information"""    
    contents = json.dumps(information)
    path.write_text(contents)
    
def greet_uers():
    """Greet the user and mention their information"""
    path = Path('information.json')
    all_the_information = get_user_information(path)
    if all_the_information:
        name = input(f"Are you {all_the_information['first_name']}?"
        "\nyes 0r no ")
        if name == "yes":
            return  (f"Welcome back,{all_the_information['first_name']}."
            f"{all_the_information['last_name']}! ")
        
        elif name == "no":
            print(greet_new_users(path))
        else:
            return ("Invalid input. Please try again.")
    else:
        print(greet_new_users(path))

print(greet_uers())

        