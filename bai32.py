# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 21:16:36 2024

@author: linh
"""

#bai 32:  Cho một danh sách các số nguyên nums 
# phân chia danh sách thành hai danh sách:
 #1. Danh sách các số chẵn, được sắp xếp theo thứ tự giảm dần (từ lớn đến nhỏ).
 #2. Danh sách các số lẻ, được sắp xếp theo thứ tự tăng dần (từ nhỏ đến lớn)
from typing import List
from typing import Tuple
def question_32(nums: List[int]) -> Tuple[List[int], List[int]]:
#Số chẵn 
    số_chẵn = []
    for số in nums:
        if số % 2 == 0:
            số_chẵn.append(số)
        số_chẵn = sorted(số_chẵn, reverse=True)
#Sắp xếp danh sách số_chẵn theo thứ tự giảm dần.
#Số lẻ 
    số_lẻ = []
    for số in nums:
        if số % 2 != 0:
            số_lẻ.append(số)
        số_lẻ = sorted(số_lẻ)
#Sắp xếp danh sách số_lẻ theo thứ tự tăng dần
    return (số_chẵn, số_lẻ)
nums = [4, 1, 3, 2, 7, 8, 5]
print(question_32(nums))