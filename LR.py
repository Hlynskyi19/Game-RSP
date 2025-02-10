def sum_int_number(number):
    sum_result = 0
    for num in range(1, number + 1):
        sum_result += num
    return sum_result


if __name__ == "__main__":
    print(sum_int_number(10))
