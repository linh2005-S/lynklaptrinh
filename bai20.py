# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 09:45:50 2024

@author: linh
"""

#bai 20: Viết một hàm yêu cầu người dùng nhập một giá trị từ bàn phím. Nếu người dùng không
#nhập bất kỳ giá trị nào từ bàn phím (chỉ nhấn Enter), hàm sẽ trả về None 
from typing import Optional
def question_20() -> Optional[str]:
    s = input("Nhập giá trị từ bán phím: ")
    if s:
        return s
    else:
        return None
print(question_20())