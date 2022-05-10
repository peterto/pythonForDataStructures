import string

from stacks_and_queues.stack_implementation import Stack


def balancedParanthesesCheck(parentheses: string) -> bool:
    right_side_paren = 0
    left_side_paren = 0
    right_side_bracket = 0
    left_side_bracket = 0
    right_side_curly = 0
    left_side_curly = 0
    if not len(parentheses):
        return "empty"

    for i in parentheses:
        if i == "[":
            left_side_bracket += 1
        elif i == "(":
            left_side_paren += 1
        elif i == "{":
            left_side_curly += 1
        elif i == "]":
            right_side_bracket += 1
        elif i == ")":
            right_side_paren += 1
        elif i == "}":
            right_side_curly += 1

    # print(left_side)
    # print(right_side)
    if left_side_bracket == right_side_bracket and left_side_paren == right_side_paren and left_side_curly == right_side_curly:
        return True

    return False


def balancedParanthesesCheckOptimal(parentheses: string) -> bool:
    s = Stack()

    for i in range(len(parentheses)):
        if parentheses[i] == "(" or parentheses[i] == "[" or parentheses == "{":
            print(f"pushing {parentheses[i]}")
            s.push(parentheses[i])
        elif parentheses[i] == ")":
            if s.peek() != "(":
                s.pop()
                return False
            else:
                s.pop()
        elif parentheses[i] == "]":
            print(f"removing {parentheses[i]}")
            if s.peek() != "[":
                s.pop()
                return False
            else:
                s.pop()
        elif parentheses == "}":
            if s.peek() != "{":
                s.pop()
                return False
            else:
                s.pop()
        elif s.isEmpty():
            return False
        # s.pop()
    return True


def balancedParanthesesCheckCorrect(s: string) -> bool:
    if len(s) % 2 != 0:
        return False

    opening = set('([{')

    matches = {('(', ')'), ('[', ']'), ('{', '}')}

    stack = []

    for paren in s:

        if paren in opening:
            stack.append(paren)

        else:

            if len(stack) == 0:
                return False

            last_open = stack.pop()

            if (last_open, paren) not in matches:
                return False

    return len(stack) == 0


# "[()]" is balanced
# "[(])" is not balanced


# print(balancedParanthesesCheck("[]"))
# true
# print(balancedParanthesesCheck("[](){([[[]]])}"))
# true
# print(balancedParanthesesCheck("()(){]}"))
# print(balancedParanthesesCheck("[(])"))
# false


# print(balancedParanthesesCheckOptimal("[]"))
# # true
print(balancedParanthesesCheckOptimal("[](){([[[]]])}"))
# # true
# print(balancedParanthesesCheckOptimal("()(){]}"))
# # false
# print(balancedParanthesesCheckOptimal("[(])"))
# # false


# print(balancedParanthesesCheckCorrect("[]"))
# # true
# print(balancedParanthesesCheckCorrect("[](){([[[]]])}"))
# # true
# print(balancedParanthesesCheckCorrect("()(){]}"))
# # false
# print(balancedParanthesesCheckCorrect("[(])"))
# # false
