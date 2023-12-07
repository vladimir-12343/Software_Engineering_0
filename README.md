# Тема 10. Декораторы и исключения.
Отчет по Теме #10 выполнил:
- Будылин Владимир Владимирович
- АИС-21-1

| Задание | Сам_раб | 
| ------ | ------ | 
| Задание 1 | + |
| Задание 2 | + |
| Задание 3 | + |
| Задание 4 | + |
| Задание 5 | + |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

## Задание 1. Вовочка решил заняться спортивным программированием на python, но для этого он должен знать за какое время выполняется его программа. Он решил, что для этого ему идеально подойдет декоратор для функции, который будет выяснять за какое время выполняется та или иная функция. Помогите Вовочке в его начинаниях и напишите такой декоратор. Подсказка: необходимо использовать модуль time.

### Результат.
![Меню](https://github.com/vladimir-12343/Software_Engineering_0/blob/Тема_10/pic/2023-11-20_13-57-53.png)
![Меню](https://github.com/vladimir-12343/Software_Engineering_0/blob/Тема_10/pic/2023-11-20_13-58-17.png)

## Вывод. 
Создал декоратор timing_decorator, который измеряет время выполнения функции и выводит его после выполнения. Затем я применил этот декоратор к функции fibonacci.


## Задание 2. Посмотрев на Вовочку, вы также загорелись идеей спортивного программирования, начав тренировки вы узнали, что для решения некоторых задач необходимо считывать данные из файлов. Но через некоторое время вы столкнулись с проблемой что файлы бывают пустыми, и вы не получаете вводные данные для решения задачи. После этого вы решили не просто считывать данные из файла, а всю конструкцию оборачивать в исключения, чтобы избежать такой проблемы. Создайте пустой файл и файл, в котором есть какая-то информация. Напишите код программы. Если файл пустой, то, нужно вызвать исключение (“бросить исключение”) и вывести в консоль “файл пустой”, а если он не пустой, то вывести информацию из файла

### Результат.
![Меню](https://github.com/vladimir-12343/Software_Engineering_0/blob/Тема_10/pic/2023-11-20_13-57-53.png)
![Меню](https://github.com/vladimir-12343/Software_Engineering_0/blob/Тема_10/pic/2023-11-20_13-58-17.png)

## Вывод. 
В результате выполнения программа считать данные из обоих файлов и обработает возможные исключения. Если файл пустой, будет вызвано исключение ValueError, и программа выведет "Файл пустой". Если файл не пустой, программа выведет информацию из файла.


## Задание 3.Напишите функцию, которая будет складывать 2 и введенное пользователем число, но если пользователь введет строку или другой неподходящий тип данных, то в консоль выведется ошибка “Неподходящий тип данных. Ожидалось число.”. Реализовать функционал программы необходимо через try/except и подобрать правильный тип исключения. Создавать собственное исключение нельзя. Проведите несколько тестов, в которых исключение вызывается и нет. Результатом выполнения задачи будет листинг кода и получившийся вывод в консоль 

### Результат.
![Меню](https://github.com/vladimir-12343/Software_Engineering_0/blob/Тема_10/pic/2023-11-20_13-57-53.png)
![Меню](https://github.com/vladimir-12343/Software_Engineering_0/blob/Тема_10/pic/2023-11-20_13-58-17.png)

## Вывод. При вводе числа программа выведет результат сложения. При вводе строки или другого неподходящего типа данных, программа поймает исключение ValueError и выведет соответствующее сообщение об ошибке. В тестах приведены примеры с разными типами ввода


## Задание 4. Создайте собственный декоратор, который будет использоваться для двух любых вами придуманных функций. Декораторы, которые использовались ранее в работе нельзя воссоздавать. Результатом выполнения задачи будет: класс декоратора, две как-то связанными с ним функциями, скриншот консоли с выполненной программой и подробные комментарии, которые будут описывать работу вашего кода.

### Результат.
![Меню](https://github.com/vladimir-12343/Software_Engineering_0/blob/Тема_10/pic/2023-11-20_13-57-53.png)
![Меню](https://github.com/vladimir-12343/Software_Engineering_0/blob/Тема_10/pic/2023-11-20_13-58-17.png)

## Вывод.создали класс ExecutionTimeDecorator, который является декоратором. Он измеряет время выполнения оборачиваемой функции и выводит его в консоль. Затем мы применили этот декоратор (@ExecutionTimeDecorator) к двум функциям (example_function_1 и example_function_2). Когда мы вызываем эти функции, мы видим, что время выполнения выводится в консоль после их выполнения.



## Задание 5. Создайте собственное исключение, которое будет использоваться в двух любых фрагментах кода. Исключения, которые использовались ранее в работе нельзя воссоздавать. Результатом выполнения задачи будет: класс исключения, код к котором в двух местах используется это исключение, скриншот консоли с выполненной программой и подробные комментарии, которые будут описывать работу вашего кода.

### Результат.
![Меню](https://github.com/vladimir-12343/Software_Engineering_0/blob/Тема_10/pic/2023-11-20_13-57-53.png)
![Меню](https://github.com/vladimir-12343/Software_Engineering_0/blob/Тема_10/pic/2023-11-20_13-58-17.png)

## Вывод. Этот код включает две функции, каждая из которых использует собственное исключение CustomException.

