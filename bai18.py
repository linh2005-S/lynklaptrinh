# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 09:39:02 2024

@author: linh
"""

#bài 18: Viết một hàm để loại bỏ tất cả khoảng trắng thừa trong một chuỗi, bao gồm:
#Loại bỏ khoảng trắng ở đầu và cuối chuỗi.
#Loại bỏ các khoảng trắng dư thừa giữa các từ (chỉ giữ lại một khoảng trắng giữa các từ)
# string.strip():Được sử dụng để loại bỏ các ký tự trắng (hoặc ký tự khác) ở đầu và cuối chuỗi.
# separator.join(danh sách, tuple, set...): Một phương thức được sử dụng để nối các phần tử trong một iterable (danh sách, tuple, set, v.v.) thành một chuỗi.
# string.split(): Dùng để tách chuỗi 
def question_18(s: str) -> str:
    s = s.strip()
    s = " ".join(s.split())
    return s
print(question_18("   Hello   World   "))