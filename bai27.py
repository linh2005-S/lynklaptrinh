# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 11:33:13 2024

@author: linh
"""

#bai27:  Viết một hàm để tìm chuỗi tiền tố chung dài nhất 
#trong một mảng các chuỗi. Nếu không có
# tiền tố chung, trả về một chuỗi rỗng 
# string.startswith(): Kiểm tra xem một chuỗi có bắt đầu bằng một đoạn chuỗi con cụ thể hay không. 
from typing import List 
def question_27(strs: List[str]) -> str:
    if not strs:
#Dòng này kiểm tra xem danh sách đầu vào strs có rỗng hay không
        return ""
    chuỗi = strs[0]
    for s in strs[1:]:
        while not s.startswith(chuỗi):
            chuỗi = chuỗi[:-1]
#Bên trong vòng lặp lồng nhau, nếu chuỗi hiện tại s không bắt đầu bằng chuỗi, 
#ký tự cuối cùng của chuỗi sẽ bị xóa bằng cách sử dụng cắt lát ([:-1]).
#Điều này làm giảm tiền tố tiềm năng một cách hiệu quả.
            if not chuỗi:
                return ""
    return chuỗi
print(question_27(["flower", "flow", "flight"]))
