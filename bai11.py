# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 09:05:05 2024

@author: linh
"""
#bai 11: Viết một hàm question_11(n) để trả về số Fibonacci thứ 
#nghĩa như sau:
 #F(0) = 0
 #F(1) = 1
 #F(n) = F(n-1) + F(n-2) với n > 1
def question_11(n: int) -> int:
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a
print(question_11(10))
        