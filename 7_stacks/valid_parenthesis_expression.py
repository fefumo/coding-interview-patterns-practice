""" 
Given a string representing an expression of parentheses containing the characters ' ( ', ') ',
' [ ' , ' ] ' , ' { ' , or ' } ', determine if the expression forms a valid sequence of parentheses.

A sequence of parentheses is valid if every opening parenthesis has a corresponding closing 
parenthesis, and no closing parenthesis appears before its matching opening parenthesis.

Example 1:
    Input: s = "([]{})"
    Output: True
Example 2:
    Input: s = "([]{)}"
    Output: False
Explanation: The ' ( ' parenthesis is closed before its nested ' { ' parenthesis is closed.
"""


def check_string(s: str) -> bool:
    hash_map = {'(': ')', '{': '}', '[': ']'}
    stack = []
    for c in s:
        if c in hash_map:
            stack.append(c)
        else:
            if stack and hash_map[stack[-1]] == c:
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    return False


def main():
    s1 = "([]{})"
    print(check_string(s1))
    s2 = "([]{)}"
    print(check_string(s2))


if __name__ == "__main__":
    main()
