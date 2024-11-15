# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 10:10:05 2024

@author: linh
"""
# Viết một hàm nhận vào một mảng các số nguyên nums 
#Di chuyển tất cả các số 0 trong mảng về cuối mảng 
#trong khi vẫn giữ nguyên thứ tự của các phần tử không phải số 0
from typing import List
def question_22(nums: List[int]) -> None:
    so= 0
    for i in range(len(nums)):
       if nums[i] !=0:
           nums[so], nums[i]= nums[i], nums[so]
# Nếu phần tử tại vị trí i khác 0, dòng này hoán đổi vị trí của phần tử đó với phần tử tại vị trí so.
#Điều này đảm bảo các phần tử khác 0 được di chuyển về phía đầu danh sách.
           so+=1
    return nums
print(question_22([0, 1, 0, 3, 12]))