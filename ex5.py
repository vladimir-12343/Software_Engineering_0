def main():
    from collections import Counter

    # Открываем файл для чтения
    with open('journal.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    authors = []
    themes = []

    # Разбираем записи и собираем авторов и темы
    for line in lines:
        parts = line.strip().split(': ')
        if len(parts) == 2:
            author, theme = parts
            authors.append(author)
            themes.append(theme)

    # Находим наиболее активного автора
    most_active_author = Counter(authors).most_common(1)

    # Находим самую часто встречающуюся тему
    most_common_theme = Counter(themes).most_common(1)

    print(f"Наиболее активный автор: {most_active_author[0][0]}")
    print(f"Самая часто встречающаяся тема: {most_common_theme[0][0]}")


if __name__ == "__main__":
    main()
