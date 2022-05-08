import string
import collections


def stringCompression(input_string: string) -> string:
    end_string = collections.defaultdict(int)
    compressed_string = ""

    if len(input_string) == 0:
        return ""

    if len(input_string) == 1:
        return input_string + str(1)

    for letter in input_string:

        if end_string[letter] == 0:
            end_string[letter] += 1
        else:
            end_string[letter] += 1

    for key, value in end_string.items():
        # print(f"{key}{value}")
        compressed_string += key
        compressed_string += str(value)

        # print(item.values)

    # end_string.values()

    # print(compressed_string)

    return compressed_string


print(stringCompression('AAAAABBBBCCCCaa'))
# A5B4C4
print(stringCompression('AABBCC'))
# A2B2C2
print(stringCompression('AAABCCDDDDD'))
# A3B1C2D5
print(stringCompression(''))
#
print(stringCompression('A'))
#