# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 09:41:43 2024

@author: linh
"""

#bài 19: Viết một hàm để kiểm tra xem một số nguyên nhập 
#vào có lớn hơn một số nguyên cho trước n hay không.
def question_19(x: int, n: int) -> bool:
    if x > n:
        return True
    else:
        return False
print(question_19(5, 10))