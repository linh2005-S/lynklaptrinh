# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 21:41:18 2024

@author: linh
"""

#bai 36:  Cho một mảng nums gồm các số nguyên khác nhau. 
#Viết một hàm để trả về tất cả các hoán
#vị có thể của mảng đó. Bạn có thể trả về kết quả theo bất kỳ thứ tự nào.
from typing import List
def question_36(nums: List[int])-> List[List[int]]:
    def tao_hoanvi(hientai, dao):
        if not dao:
            ketqua.append(hientai)
        for i in range(len(dao)):
            tao_hoanvi(hientai + [dao[i]], dao[:i]+dao[i+1:])
    ketqua = []
    tao_hoanvi([], nums)
    return ketqua
nums = [1,2,3]
print (question_36(nums))