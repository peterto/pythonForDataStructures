import string


def rec_sum(input_num: int) -> int:
    if input_num == 0:
        return 0
    else:
        return input_num + rec_sum(input_num - 1)


# print(rec_sum(4))

def sum_func(input_num: int) -> int:
    if len(str(input_num)) == 1:
        return input_num
    else:
        # print(input_num)
        print(int(input_num))
        return input_num % 10 + sum_func(input_num / 10)


print(sum_func(4321))


def word_split(phrase: string, list_of_words: set):

    pass
