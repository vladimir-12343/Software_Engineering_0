import random

def main(meaning):
    if 5 <= meaning <= 6:
        print("Вы победили! Значение кубика - ", meaning)
    elif 3 <= meaning <= 4:
        print("Зачение кубика - ", meaning)
        main(random.randint(1, 6))
    else:
        print("Вы проиграли! Значение кубика - ", meaning)


if __name__ == "__main__":
    main(random.randint(1, 6))
