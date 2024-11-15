# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 22:34:19 2024

@author: linh
"""

#bài 2:  Viết một hàm tạo ra n số nguyên ngẫu nhiên từ 1 đến 100 
#Sau đó, tính tổng và trung bình của các số này
# danhsach.append(): Thêm 1 phần tử vào cuối danh sách
import random
def question_2(n: int) -> (int, float):
    danh_sách = []
    for i in range(n):
        x = random.randint(1, 100)
        danh_sách.append(x)
    tổng = sum(danh_sách)
    trung_bình = tổng / n
    return (tổng, trung_bình)
print(question_2(5))