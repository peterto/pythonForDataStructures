import array


def arrayPairSum(int_array: array, sum_number: int) -> int:

    if len(int_array) < 2:
        return
    pairs_count = 0
    pairs = {}
    int_array.sort()

    left_pointer = 0
    right_pointer = len(int_array) - 1

    while left_pointer <= right_pointer:
        if left_pointer == right_pointer:
            break
        if int_array[left_pointer] + int_array[right_pointer] == sum_number:
            pairs_count += 1
            left_pointer += 1

        right_pointer -= 1
    return pairs_count


# ex: arrayPairSum([1, 3, 2, 2], 4)
# (1, 3)
# (2, 2)

print(arrayPairSum([1, 3, 2, 2], 4))
print(arrayPairSum([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10))
print(arrayPairSum([1,2,3,1],3))
print(arrayPairSum([1,3,2,2],4))
