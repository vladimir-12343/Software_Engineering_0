import Heron_square

def main():
    a = float(input("Введите длину стороны a: "))
    b = float(input("Введите длину стороны b: "))
    c = float(input("Введите длину стороны c: "))
    print("Площадь треугольника равна: ", Heron_square.SquareHeron(a, b, c))

if __name__ == "__main__":
    main()
