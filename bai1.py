# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 21:08:48 2024

@author: linh
"""

#bài 1: Bạn được cung cấp một số nguyên dương n. 
#Viết hàm xác định xem n phải số nguyên tố hay không 
#(snt là số nguyên dương > 1, có 2 ước sô dương là 1 và chính nó)

def question_1(n: int)-> bool:
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
print(question_1(11))