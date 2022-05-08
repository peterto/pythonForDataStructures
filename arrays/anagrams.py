import string


def anagram(str1: string, str2: string) -> bool:
    # new_array = str1.lower().strip(" ").split()
    # new_array2 = str2.lower().strip(" ").split()

    str1.lower().strip(" ")
    str2.lower().strip(" ")

    if len(str1) != len(str1):
        return False
    else:

        new_array = []
        new_array2 = []

        for l in range(len(str1)):
            if str1[l] != " ":
                new_array.append(str1[l])

        for l in range(len(str2)):
            if str2[l] != " ":
                new_array2.append(str2[l])

        new_array.sort()
        new_array2.sort()

        print(new_array)
        print(new_array2)
        for l in range(len(new_array)):
            if new_array[l] != new_array2[l]:
                return False

        return True


print(anagram('dog', 'god'))
print(anagram('clint eastwood', 'old west action'))
print(anagram('aa', 'bb'))

# examples:
# anagram('dog', 'god')
# True

# anagram('clint eastwood', 'old west action')
# True

# anagram('aa', 'bb')
# False


primes = [2, 3, 5, 7, 11, 13, 17, 19]
temp = primes[3:6]

print(temp)
