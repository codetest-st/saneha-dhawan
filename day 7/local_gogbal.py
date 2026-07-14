user="Anil"
def sayhello():
    global user
    user="john"
    print(f"hello,{user}!,{globals()['user']}")
    sayhello()
    print(user)