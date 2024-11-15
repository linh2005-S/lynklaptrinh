# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 09:16:41 2024

@author: linh
"""

#Viết một hàm để đếm số từ trong một chuỗi. Một từ được định nghĩa là một chuỗi các ký tự
#không phải khoảng trắng
#split là tách chuỗi 
def question_13(s: str) -> int:
    các_từ = s.split()
    return len(các_từ)
print(question_13("Hello world, how are you?"))