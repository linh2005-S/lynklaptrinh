# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 09:53:43 2024

@author: linh
"""

#bai 21:  Viết một hàm nhận vào một danh sách số nguyên ngẫu nhiên và một số nguyên dương.
# Hàm sẽ tìm trong danh sách hai số có tổng bằng với số nguyên dương kia và trả về cặp số 
from typing import Optional, Tuple, List
def question_21(nums: List[int], target: int) -> Optional[Tuple[int, int]]: 
    ds = {}
    for a in nums:
        socantim = target - a
        if socantim in ds:
            return(socantim, a)
        ds[a] = True
    return None
print(question_21([2, 7, 11, 15], 9)) 