# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 08:51:44 2024

@author: linh
"""
#Viết một hàm để tính giai thừa của số nguyên dương tích của tất cả các số từ 1 đến n

def question_6(n: int) -> int:
    if n==0 or n==1:
        return 1
    else:
        kết_quả = n
        for i in range(2,n):
            kết_quả *= i
    return kết_quả
print(question_6(5))   