"""
reply = ("We'll remember your information:"
            f"\nfirst name:{information['first_name']}"
            f"\nlast name:{information['last_name']}"
            f"\ngender:{information['user_gender']}")
"""
def ffff():
    information = {
            "first_name":'first_name',
            "last_name":'last_name',
            "user_gender":'user_gender',
        }
    inf = ''   
    for key, value in information.items():
        inf += f"\n{key}:{value}"    
    return inf

print(ffff())