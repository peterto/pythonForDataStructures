import array
import collections


def findMissingElement(array1: array, array2: array):
    missing_element = 0

    array1.sort()
    array2.sort()

    for i in array1:
        if array2.count(i) != array1.count(i):
            missing_element = i
            # missing_element.append

    print(missing_element)


# loop through each in first array, comparing values in the

arr1 = [1, 2, 3, 4, 5, 6, 7]
arr2 = [3, 7, 2, 1, 4, 6]
findMissingElement(arr1, arr2)

arr1 = [5, 5, 7, 7]
arr2 = [5, 7, 7]
findMissingElement(arr1, arr2)

findMissingElement([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6])
# 5
findMissingElement([9, 8, 7, 6, 5, 4, 3, 2, 1], [9, 8, 7, 5, 4, 3, 2, 1])
# 6
# arr1 = [1, 2, 3, 4, 5, 6, 7]
# arr2 = [3, 7, 2, 1, 4, 6]
# finder(arr1, arr2)
