import os


def main():
    expenses = load_expenses()

    while True:
        print("Выберите действие:")
        print("1. Ввести новый расход")
        print("2. Посмотреть все расходы")
        print("3. Выйти")

        choice = input("Введите номер действия: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            save_expenses(expenses)
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите действие 1, 2 или 3.")


def load_expenses():
    if os.path.exists("expenses.txt"):
        with open("expenses.txt", "r") as file:
            expenses = file.read().splitlines()
        return expenses
    else:
        return []


def add_expense(expenses):
    description = input("Введите описание расхода: ")
    amount = input("Введите сумму расхода: ")
    expense = f"{description}: {amount} руб."
    expenses.append(expense)
    print("Расход успешно добавлен.")


def view_expenses(expenses):
    if expenses:
        print("Все расходы:")
        for expense in expenses:
            print(expense)
    else:
        print("Нет сохраненных расходов.")


def save_expenses(expenses):
    with open("expenses.txt", "w") as file:
        for expense in expenses:
            file.write(expense + "\n")
    print("Расходы успешно сохранены в файл.")


if __name__ == "__main__":
    main()

