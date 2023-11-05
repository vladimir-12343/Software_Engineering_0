
def print_hi(name):
    with open("C:\\Users\\vladlen\\Desktop\\Software_Engineering_0\\Topic_7\\Статья.txt", "r", encoding="utf-8") as file:
        line = file.read()
        delimiters = [",", "|", ";", "."]
        my_list = []
        count = 0
        #Если символ delimiters встретился в строке, то строку по этому символу и split
        for delimiter in delimiters:
            line = " ".join(line.split(delimiter))
        result = line.split()
        print("Количесвто слов -", len(result))
        for word in result:
            if word not in my_list:
                # Добавляем те слова, которые еще не были добавлены в my_list
                my_list.append(result.count(word))
                if count <= result.count(word):
                    #Еслис читать, что предлог - это слово служебной части речи, то получаем следующее
                    count = result.count(word)
                    saveWord = word
        print(f"Наибольшее количество раз ({count}) встретилось слово -", '\''+saveWord+'\'')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
