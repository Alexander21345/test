users = {"admin" : "1234"}
secret = "42"

while True:
    q1 = input("вход или регистрация ?")
    if q1 == "вход":
        login = input ("введи логин")
        password = input("введи пароль")

        if login in users.keys():
            if users[login] == password:
                print("успешно")
                print(secret)
                break
    elif q1 == "регистрация":
        login = input("введи логин")
        password = input("введи пароль")
        if login in users.keys():
            print("логин занят")
        else:
            users[login] = password
            print("регистрация норм")
    else:
        print("данные гавно")