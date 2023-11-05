def main():
    # Открываем файл input.txt для чтения
    with open("text.txt", "r") as file:
        text = file.read()

    # Считаем количество букв, слов и строк
    num_letters = count_letters(text)
    num_words = count_words(text)
    num_lines = count_lines(text)

    # Выводим статистику
    print(f"Количество букв латинского алфавита: {num_letters}")
    print(f"Количество слов: {num_words}")
    print(f"Количество строк: {num_lines}")

def count_letters(text):
    # Считаем количество букв латинского алфавита (a-zA-Z)
    latin_letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    count = sum(1 for char in text if char in latin_letters)
    return count

def count_words(text):
    # Разбиваем текст на слова по пробелам и символам новой строки
    words = text.split()
    return len(words)

def count_lines(text):
    # Считаем количество строк, разделяя текст по символам новой строки
    lines = text.split("\n")
    return len(lines)

if __name__ == "__main__":
    main()

