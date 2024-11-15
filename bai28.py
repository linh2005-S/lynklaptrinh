# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 20:34:11 2024

@author: linh
"""

#bai 28:Viết một hàm để đếm số lần xuất hiện của từng phần tử (ký tự) trong một chuỗi. Trả về kết
#quả dưới dạng một từ điển, trong đó các khóa là các ký tự và
# giá trị là số lần xuất hiện của ký tự đó
from typing import Dict 
def question_28(s: str) -> Dict[str, int]:
    chuỗi = {}
    for kí_tự in s:
        if kí_tự in chuỗi:
            chuỗi[kí_tự] += 1
        else:
            chuỗi[kí_tự] = 1   
    return chuỗi
print(question_28("hello"))