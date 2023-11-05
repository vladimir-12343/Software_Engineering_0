
def main():
    # Открываем файл с запрещенными словами и читаем их
    with open('input.txt', 'r') as file:
        forbidden_words = file.read().split()

    # Предложение для проверки
    sentence = "Hello, world! Python IS the programming language of thE future. My EMAIL is.... PYTHON is awesome!!!!"

    # Разбиваем предложение на слова
    words = sentence.split()

    # Функция для замены запрещенных слов в предложении
    def replace_forbidden_words(word):
        word_lower = word.lower()  # Приводим слово к нижнему регистру
        for forbidden_word in forbidden_words:
            if forbidden_word in word_lower:
                word = '*' * len(word)
        return word
    # Заменяем запрещенные слова и выводим предложение
    new_sentence = ' '.join(map(replace_forbidden_words, words))
    print(new_sentence)


if __name__ == "__main__":
    main()
