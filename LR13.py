def sum_positive_numbers(*numbers):
    result = []
    for number in numbers:
        try:
            if isinstance(number, int) and number > 0:
                result.append(sum(range(number + 1)))  # Використання sum() і range()
            else:
                result.append(0)
        except TypeError:
            result.append(0)  # Якщо вхідні дані не є числом, повертаємо 0
    return result


if __name__ == "__main__":
    print(
        sum_positive_numbers(5, -3, 10, 7, "abc", 4.5)
    )  # Тест із різними типами даних
