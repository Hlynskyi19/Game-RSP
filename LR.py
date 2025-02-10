def sum_int_number(number):
    try:
        number = int(number)  # Переконуємось, що вхідне значення є цілим числом
        if number < 0:
            raise ValueError("Число повинно бути додатним!")
        return sum(num for num in range(1, number + 1))
    except ValueError as e:
        print(f"Помилка: {e}")
        return 0  # Повертаємо 0 у разі некоректного вводу


if __name__ == "__main__":
    print(sum_int_number(10))  # Коректний виклик
    print(sum_int_number(-5))  # Викличе помилку
    print(sum_int_number("abc"))  # Викличе помилку
