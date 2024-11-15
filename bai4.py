# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 23:24:19 2024

@author: linh
"""

#bài 4:Viết một hàm để kiểm tra xem một số nguyên được nhập vào có phải là số chẵn hay không.
# Trả về True nếu số đó là số chẵn False nếu là số lẻ

def question_4(n: int)-> bool:
    if n % 2 == 0:
        return True
    elif n % 2 != 0:
        return False
print(question_4(4)) 