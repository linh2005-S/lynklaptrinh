# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 09:36:26 2024

@author: linh
"""

#bai17: Viết một hàm để tạo ra một danh sách gồm n
# số nguyên ngẫu nhiên từ 1 đến 100. Sau đó,
#sắp xếp danh sách theo thứ tự giảm dần
# List.append(): Thêm một phần tử vào cuối danh sách 
# list.sort(): Dùng để sắp xếp các phần tử trong danh sách theo thứ tự tăng dần
# list.sort(reverse=True): Sắp xếp các phần tử trong danh sách theo thứ tự giảm dần
# list.sort(key=len): Sắp xếp theo độ dài của chuỗi 
import random 
def question_17(n: int) -> list:
    danh_sách = []
    for i in range(n):
        x = random.randint(1, 100)
        danh_sách.append(x)
    danh_sách.sort(reverse= True)
    return danh_sách
print(question_17(5))