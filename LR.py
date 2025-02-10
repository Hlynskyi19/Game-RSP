def sum_int_number(number):
    """
    Обчислює суму цілих чисел від 1 до заданого додатного числа.

    >>> sum_int_number(10)
    55
    >>> sum_int_number(0)
    0
    >>> sum_int_number(-5)
    0
    >>> sum_int_number("abc")
    0
    >>> sum_int_number(5)
    15
    """
    try:
        number = int(number)  # Переконуємось, що вхідне значення є цілим числом
        if number < 0:
            return 0
        return sum(range(1, number + 1))
    except ValueError:
        return 0  # Якщо введено нечислове значення, повертаємо 0


if __name__ == "__main__":
    import doctest

    doctest.testmod()  # Запускаємо тестування
    print(sum_int_number(10))
