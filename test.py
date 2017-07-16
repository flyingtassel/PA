# -*- coding: utf-8 -*-

def is_palindrome(n):
    return str(n) == str(n)[::-1]

# 测试:
output = filter(is_palindrome, range(1, 10000))
print(list(output))