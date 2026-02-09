""" 
Given a string representing a mathematical expression containing integers, parentheses,
addition, and subtraction operators, evaluate and return the result of the expression.

Example:
    Input: s = "18-(7+(2-4))"
    Ouput: 13
"""


def evaluate(s: str):
    sign = 1
    curr_num = 0
    res = 0
    stack = []
    for c in s:
        if c.isdigit():
            curr_num *= 10
            curr_num += ord(c) - ord('0')
        elif c == '-' or c == '+':
            res += curr_num * sign
            if c == '-':
                sign = -1
            else:
                sign = 1
            curr_num = 0
        elif c == ' ':
            continue

        elif c == '(':
            stack.append(res)
            stack.append(sign)
            res, sign = 0, 1
        elif c == ')':
            res += curr_num * sign
            res *= stack.pop()
            res += stack.pop()
            curr_num = 0
    return res + curr_num * sign


def main():
    asd = evaluate('18-(7+(2-4))')
    print(asd)


if __name__ == "__main__":
    main()
