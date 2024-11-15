# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 21:32:49 2024

@author: linh
"""

#bai 34: Viết một hàm để tìm chuỗi con dài nhất trong chuỗi đầu 
#vào mà không chứa bất kỳ ký tự nào bị lặp lại.
# list.remove(): Xóa phần tử ra khỏi danh sách 
# set.add(): Thêm phần tử vào danh sách 
def question_34(s: str) -> int:
    bộ_ký_tự = set()
    bắt_đầu = 0  
    chuỗi_max = 0  
    for kết_thúc in range(len(s)):
        while s[kết_thúc] in bộ_ký_tự:
            bộ_ký_tự.remove(s[bắt_đầu])
            bắt_đầu += 1
        bộ_ký_tự.add(s[kết_thúc])
        chuỗi_max = max(chuỗi_max, kết_thúc - bắt_đầu + 1)
    return chuỗi_max
s = "abcabcbb"
print(question_34(s))  
