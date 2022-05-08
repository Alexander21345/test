# 1) администратор управляет меню(добавляет ппицу в меню, удаляет)
# 2) поользователь делает заказ (выбирает из меню пиццы, автоматически рассчитывается ст-ть заказа)
menu = {
     'margarita': 400,
     'pepperoni' : 600
}

def add_pizza(name, price) :
    if name in menu.keys():
        print("пицца уже есть в меню")
    else:
        menu[name] = price


def remove_pizza(name) :
    if name in menu.keys():
        print("пицца уже есть в меню. удаляем")
        del menu[name]
    else:
        print("нет в меню.удаляем")
