# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 09:00:56 2024

@author: linh
"""

# bài 10: Viết một hàm nhập vào một danh sách số nguyên từ bàn phím các số nguyên này được
#phân cách bằng khoảng trắng và trả về None nếu danh sách đó trống.
# split là tách chuỗi 
def question_10() -> None:
    danh_sách = input("Nhập vào danh sách số nguyên: ")
    if not danh_sách:
        return None
    danh_sách_số_nguyên = [int(i) for i in danh_sách.split()]
    return danh_sách_số_nguyên
print(question_10())