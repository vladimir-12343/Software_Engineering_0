import Heron

def main():
    one = [12, 25, 3, 48, 71]
    two = [5, 18, 40, 62, 98]
    three = [4, 21, 37, 56, 84]
    my_conList = one+two+three
    my_conList.sort()
    print("площади треугольника, составленного из минимальных элементов -", Heron.SquareHeron(my_conList[0], my_conList[1], my_conList[2]))
    print("площади треугольника, составленного из максимальных элементов -", Heron.SquareHeron(my_conList[len(my_conList)-1], my_conList[len(my_conList)-2], my_conList[len(my_conList)-3]))

if __name__ == "__main__":
    main()
