# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 10:18:53 2024

@author: linh
"""

#bai 23: Viết một hàm nhận vào một mảng các số nguyên nums 
#Trả về True nếu có bất kỳ giá trị nào xuất hiện ít nhất hai lần 
#trong mảng, và trả về False nếu tất cả các phần tử trong mảng đều khác nhau
#set: loại bỏ các phần tử trùng lặp trong mảng nums
from typing import List 
def question_23(nums: List[int]) -> bool:
    s = set()  
    for n in nums:
        if n in s: 
            return True  
        s.add(n)    
    return False  
print(question_23([1, 2, 3, 1]))  
