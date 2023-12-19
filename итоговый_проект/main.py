import random

import pygame
import sys

# Инициализация Pygame
pygame.init()

# Определение констант
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
GRID_SIZE = 3  # Количество строк и столбцов в сетке

# Определение цветов
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

CROSS = 'X'
CIRCLE = 'O'

# Создание пустой сетки
grid = [[' ' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

# Создание экрана
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(WHITE)#белый цвет экрана
pygame.display.set_caption("Крестики-нолики")

# Вычисление размера каждой ячейки в сетке
cell_width = SCREEN_WIDTH // GRID_SIZE
cell_height = SCREEN_HEIGHT // GRID_SIZE

def check_winner(symbol):
    # Проверка выигрышных комбинаций по горизонтали
    for row in grid:
        if all(cell == symbol for cell in row):
            return True

    # Проверка выигрышных комбинаций по вертикали
    for col in range(GRID_SIZE):
        if all(grid[row][col] == symbol for row in range(GRID_SIZE)):
            return True

    # Проверка выигрышных комбинаций по диагонали (левая верхняя - правая нижняя)
    if all(grid[i][i] == symbol for i in range(GRID_SIZE)):
        return True

    # Проверка выигрышных комбинаций по диагонали (левая нижняя - правая верхняя)
    if all(grid[i][GRID_SIZE - 1 - i] == symbol for i in range(GRID_SIZE)):
        return True

    return False


# Основной цикл программы
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Получение координат мыши при нажатии
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # Определение ячейки, в которую было произведено нажатие
            clicked_row = mouse_y // cell_height
            clicked_col = mouse_x // cell_width

            #Ход игрока
            if grid[clicked_row][clicked_col] == ' ':
                # Рисование крестика в ячейке
                pygame.draw.line(screen, BLACK, (clicked_col * cell_width, clicked_row * cell_height),
                                 ((clicked_col + 1) * cell_width, (clicked_row + 1) * cell_height), 2)
                pygame.draw.line(screen, BLACK, ((clicked_col + 1) * cell_width, clicked_row * cell_height),
                                 (clicked_col * cell_width, (clicked_row + 1) * cell_height), 2)
            # Запись символа в сетку
            grid[clicked_row][clicked_col] = CROSS

            # Ход компьютера
            # Выбираем рандомно ячейку
            computer_row, computer_col = random.choice(
                [(i, j) for i in range(GRID_SIZE) for j in range(GRID_SIZE) if grid[i][j] == ' '])

            # Рисование нолика в случайной пустой ячейке
            pygame.draw.ellipse(screen, BLACK,
                                pygame.Rect(computer_col * cell_width, computer_row * cell_height,
                                            cell_width, cell_height), 2)
            # Запись символа в сетку
            grid[computer_row][computer_col] = CIRCLE

            if check_winner(CROSS):
                print("Победил игрок!")
                running = False
            elif check_winner(CIRCLE):
                print("Победил компьютер!")
                running = False
            elif all(cell != ' ' for row in grid for cell in row):
                print("Ничья!")
                running = False


            # Вывод информации о ячейке, в которую было произведено нажатие
            print(f"Clicked on cell ({clicked_row}, {clicked_col})")



    # Рисование вертикальных линий сетки
    for i in range(1, GRID_SIZE):
        pygame.draw.line(screen, BLACK, (i * cell_width, 0), (i * cell_width, SCREEN_HEIGHT), 2)

    # Рисование горизонтальных линий сетки
    for j in range(1, GRID_SIZE):
        pygame.draw.line(screen, BLACK, (0, j * cell_height), (SCREEN_WIDTH, j * cell_height), 2)

    # Обновление экрана
    pygame.display.flip()

# Завершение работы Pygame
pygame.quit()
sys.exit()
