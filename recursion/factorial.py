def factorial(input_num: int) -> int:

    if input_num == 0:
        return 1
    else:
        return input_num * factorial(input_num - 1)


print(factorial(4))
