# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 09:07:28 2024

@author: linh
"""
#bài 12:Viết một hàm để tạo ra một số nguyên ngẫu nhiên từ 1 đến 1000. 
#Sau đó, kiểm tra xem số đó có phải là số nguyên tố hay không.
# Số nguyên tố là số nguyên dương lớn hơn 1 và chỉ có hai ước số dương là 1 và chính nó
def question_12() -> bool:
    import random
    n = random.randint(1, 1000)
    print(f"Số ngẫu nhiên : {n}")
    if n<2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
        return True
print(question_12())