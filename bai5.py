# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 23:29:44 2024

@author: linh
"""

#bài 5: Viết một hàm để tìm phần tử x trong một danh sách lst 
#Nếu tìm thấy, trả về vị trí (chỉ số) của phần tử đó, nếu không, trả về None 
#
def question_5(lst: list, x: int) -> int or None:
    if x in lst:
        return lst.index(x)   
# Nếu x được tìm thấy trong danh sách, dòng này sẽ trả về chỉ số (vị trí) 
#của lần xuất hiện đầu tiên của x trong danh sách
    return None
print(question_5([1, 2, 3, 4, 5], 3))