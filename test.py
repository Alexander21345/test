users = {"admin" : "1234"}
secret = "42"

def login():
    login = input("введи логин")
    password = input("введи пароль")

    if login in users.keys():
        if users[login] == password:
            print("успешно")
            print(secret)

def register():
    login = input("введи логин")
    password = input("введи пароль")
    if login in users.keys():
        print("логин занят")
    else:
        users[login] = password
        print("регистрация норм")

def error():
    print("данные гавно")
while True:
    q1 = input("вход или регистрация ?")
    if q1 == "вход":
        login()
        break
    elif q1 == "регистрация":
          register()
    else:
          error()