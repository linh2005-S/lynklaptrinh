# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 21:47:58 2024

@author: linh
"""

#bai 37: Cho một chuỗi s chỉ chứa các 
#ký tự '(', ')', '{', '}', '[' và ']'. 
#Viết một hàm để xác định xem chuỗi đầu vào có hợp lệ hay không.
# dict.values(): trả về tất cả các giá trị trong từ điển đó dưới dạng một đối tượng dict_values.
# dict.keys(): trả về tất cả các khóa (keys) trong từ điển đó dưới dạng một đối tượng dict_keys.
# Ví dụ cho dễ hiểu: 
# s = {'a': 1, 'b': 2, 'c': 3}
# từ_khóa = s.keys()
# giá_trị = list(s.values())
# print(từ_khóa) output: 'a' , 'b' , 'c' 
# print(giá_trị) output: '1', '2' , '3' 
# list.pop(): loại bỏ và trả về phần tử cuối cùng của danh sách. 
def question_37(s: str) -> bool:
    start = []
    dấu_phù_hợp = {')': '(', '}': '{', ']': '['}
    for kí_tự in s:
        if kí_tự in dấu_phù_hợp.values():  
            start.append(kí_tự)
        elif kí_tự in dấu_phù_hợp.keys():  
            if start and start[-1] == dấu_phù_hợp[kí_tự]:
                start.pop()  
            else:
                return False 
    return not start 
s = "(]"
print(question_37(s))