def sum_int_number(number):
    return sum(num for num in range(1, number + 1))


if __name__ == "__main__":
    print(sum_int_number(10))
