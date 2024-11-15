# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 09:17:45 2024

@author: linh
"""

#bai 14: Viết một hàm để kiểm tra xem một chuỗi có phải là chữ số hay không. Chuỗi được coi là
#chữ số nếu tất cả các ký tự trong chuỗi là số và không có ký tự nào khác.
# string.isdigit(): Được sử dụng để kiểm tra xem tất cả các ký tự trong chuỗi có phải là chữ số (digit) hay không.
def question_14(s: str) -> bool:
    if s.isdigit():
        return True
    return False
print(question_14("12345"))