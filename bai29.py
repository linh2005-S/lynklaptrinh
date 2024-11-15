# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 20:50:49 2024

@author: linh
"""

#bài 29:  Số trung vị của một danh sách các số nguyên là giá trị ở vị trí giữa khi danh sách được sắp
#xếp theo thứ tự tăng dần. Nếu danh sách có số lượng phần tử là lẻ, số trung vị là giá trị
#giữa. Nếu danh sách có số lượng phần tử là chẵn, 
#số trung vị là trung bình cộng của hai giá trị ở giữa
# len(object): Trả về độ dài của một đối tượng 
# list.sort(): Dùng để sắp xếp các phần tử trong danh sách theo thứ tự tăng dần
# list.sort(reverse=True): Sắp xếp các phần tử trong danh sách theo thứ tự giảm dần
# list.sort(key=len): Sắp xếp theo độ dài của chuỗi 
from typing import Optional, Tuple, List
def question_29(nums: List[int])-> Optional[Tuple[int, int]]:
    nums.sort()
    n = len(nums)
    if n % 2 != 0:
        return float(nums[n // 2])
    else:
        return (nums[n // 2 - 1] + nums[n // 2]) / 2.0
print(question_29([1, 3, 4, 2, 5]))
