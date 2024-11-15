# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 09:21:39 2024

@author: linh
"""
#bài 16:  Viết một hàm để tính trung bình cộng, 
#nhận vào số lượng tham số bất kỳ và trả về giá trị
#trung bình cộng của chúng
def question_16(*arg) -> float:
    if not arg:
        return None
    return sum(arg)/len(arg)
print(question_16(1,2,3,4,5))
