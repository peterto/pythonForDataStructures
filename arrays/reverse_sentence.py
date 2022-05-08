import string


def reverseSentence(sentence: string) -> string:
    sentence = sentence.strip()
    stack = []

    # split_sentence = sentence.split()
    final_sentence = ''

    # if len(split_sentence) == 0:
    #     print('empty')
    #     return
    #
    # right = len(split_sentence) - 1
    #
    # for i in range(len(split_sentence)):
    #     final_sentence += split_sentence[right].strip() + " "
    #     right -= 1
    #
    # print(final_sentence.strip(' '))

    if sentence == "":
        print("nothing here")
        return ""

    word = ""
    temp_word = ""
    right = len(sentence) - 1

    for i in range(len(sentence)):
        stack.append(sentence[right])

        if sentence[right].isspace():
            # print(len(sentence[right]))
            for j in range(len(stack)):
                temp_word += stack.pop()
            # print(temp_word)

        if right == 0:
            temp_word += ' '
            for j in range(len(stack)):
                temp_word += stack.pop()

        # print(temp_word)

        if temp_word.isspace():
            temp_word = ''

        word += temp_word
        temp_word = ''
        # print(sentence[right])
        right -= 1

    # word += sentence[0]
    # print(sentence[0])

    print(word.strip())


reverseSentence("")
reverseSentence("             ")
reverseSentence("A")
reverseSentence("this is a test")
reverseSentence("Hi John,              are you ready to go?")
reverseSentence("        space before")
reverseSentence("        hello john            how are you      ")
