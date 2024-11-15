# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 21:22:19 2024

@author: linh
"""

#bai 33: Cho một danh sách nums
#chứa các số nguyên. Viết một hàm để tìm phần tử lớn thứ 2 và
#phần tử nhỏ thứ 5 trong danh sách
from typing import List
from typing import Tuple
def question_33(nums: List[int]) -> Tuple[int, int]:
    ds = list(set(nums))
    ds.sort()
    if len(ds)>5:
        solonthu2 = ds[-2]
        sobethu5 = ds[4]
    else:
        return None
    return solonthu2, sobethu5
nums = [3, 1, 4, 5, 9, 2, 6, 8, 7]
print(question_33(nums))  