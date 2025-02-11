def hanoi(n, source, target, auxiliary):
    """
    Рекурсивний алгоритм для розв'язання головоломки "Ханойська вежа".
    :param n: Кількість дисків
    :param source: Початковий стовп
    :param target: Цільовий стовп
    :param auxiliary: Допоміжний стовп
    """
    if n == 1:
        print(f"Перемістіть диск 1 з {source} на {target}")
        return

    hanoi(n - 1, source, auxiliary, target)
    print(f"Перемістіть диск {n} з {source} на {target}")
    hanoi(n - 1, auxiliary, target, source)


if __name__ == "__main__":
    num_disks = int(input("Введіть кількість дисків: "))
    hanoi(num_disks, "A", "C", "B")
