""" 
In number theory, a happy number is defined as a number that, when repeatedly subjected
to the process of squaring its digits and summing those squares, eventually leads to 1 [1].
An unhappy number will never reach 1 during this process, and will get stuck in an infinite
loop.

Given an integer, determine if it's a happy number.

Example:

Input: n = 23
Output. True
Explanation: 2^2 + 3^2 = 13 => 1^2 + 3^2 = 10 => 1^2 + 0^2 = 1
"""


def get_next_num(x: int) -> int:
    next_num = 0
    while x > 0:
        digit = x % 10
        x //= 10
        next_num += digit ** 2
    return next_num


def happy_number(n: int) -> bool:
    slow = fast = n
    while True:
        slow = get_next_num(slow)
        fast = get_next_num(get_next_num(fast))
        if fast == 1:
            return True
        elif fast == slow:
            return False


def main():
    print(happy_number(23))
    print(happy_number(116))


if __name__ == "__main__":
    main()
