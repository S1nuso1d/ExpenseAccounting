def menu():
    print("\nМеню:")
    print("1.Добавить расход")
    print("2.Показать расходы:")
    print("3.Показать сумму")
    print("4.Удалить расход")
    print("5.Выход")

def ask_expense():
    return

def week_total():
    return

def expense_del():
    return



while True:
    menu()
    choise = input("Ваш выбор: ")

    if choise == "5":
        break

    elif choise == "1":
        ask_expense()

    elif choise == "2":
        print()

    elif choise == "3":
        week_total()

    elif choise == "4":
        expense_del()