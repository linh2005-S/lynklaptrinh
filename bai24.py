# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 10:19:19 2024

@author: linh
"""

#bài 24: Viết một hàm nhận vào một mảng số nguyên nums có kích thước 
#Trả về phần tử chiếm đa số trong mảng. 
#Phần tử chiếm đa số là phần tử xuất hiện nhiều hơn [n / 2] lần. Bạn có
#thể giả định rằng phần tử chiếm đa số luôn tồn tại trong mảng
from typing import List 
def question_24(nums: List[int]) -> int:
    a = None
    đếm = 0
    for num in nums:
        if đếm == 0:
            a = num
            đếm = 1
        elif num == a:
            đếm += 1
        else:
            đếm -= 1
    return a
print(question_24([3, 2, 3]))
 