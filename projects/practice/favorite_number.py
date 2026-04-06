from pathlib import Path
import json
"""
def greet_uers():
    path = Path('f_number.json')
    if path.exists():
        contents2 = path.read_text()
        favorite_number = json.loads(contents2)
        return f"I know your favorite number!It's {favorite_number}."
    else:
        fn = input("What's your favorite number?")
        contents = json.dumps(fn)
        path.write_text(contents)
        return f"We'll remmber your favorite number when you come back,{fn}"

print(greet_uers())
"""
def get_stored_username(path):
    """Get it if username has been stored"""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None

def get_new_username(path):
    """Prompt the user to enter the username"""
    username = input("What's your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username

def greet_uers():
    """Greet the user and mention their username"""
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        return f"Welcome back,{username}!"
    else:
        username = get_new_username(path)
        return f"We'll remmber you when you come back, {username}!"
print(greet_uers())

        
