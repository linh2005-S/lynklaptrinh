# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 10:33:22 2024

@author: linh
"""

#bai 25: Cho một mảng các số nguyên nums
#đã được sắp xếp theo thứ tự không giảm. Viết một hàm
#để trả về một mảng chứa bình phương của mỗi số trong 
#sắp xếp theo thứ tự không giảm.
# list.sort(): Dùng để sắp xếp các phần tử trong danh sách theo thứ tự tăng dần
# list.sort(reverse=True): Sắp xếp các phần tử trong danh sách theo thứ tự giảm dần
# list.sort(key=len): Sắp xếp theo độ dài của chuỗi 
from typing import List 
def question_25(nums: List[int]) -> List[int]:
    bình_phương = [số ** 2 for số in nums]
    bình_phương.sort()
    return bình_phương 
print(question_25([-4, -1, 0, 3, 10]))  
