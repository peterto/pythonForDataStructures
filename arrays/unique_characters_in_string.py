import string
import collections


def uniqueCharactersInString(input_string: string) -> bool:
    output_string = collections.defaultdict(int)

    if len(input_string) == 0:
        return False
    if len(input_string) == 1:
        return True

    for character in input_string:
        if output_string[character] == 0:
            output_string[character] += 1

        else:
            output_string[character] += 1

    for key, value in output_string.items():
        # print(key)
        if value != 1:
            return False
        else:
            return True


def uniqueCharactersInStringOptimal(input_string: string) -> bool:

    chars = set()

    for i in input_string:
        if i in chars:
            return False
        else:
            chars.add(i)

    return True


print(uniqueCharactersInString("ABC"))
print(uniqueCharactersInString("GGGG"))
print(uniqueCharactersInString("liasudhflikasudhfliasukhf"))
print(uniqueCharactersInString(""))
print(uniqueCharactersInString("B"))
print(uniqueCharactersInStringOptimal("BB"))