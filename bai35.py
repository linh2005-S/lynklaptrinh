# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 21:37:03 2024

@author: linh
"""

#bai 35: Cho một chuỗi đầu vào, tìm chuỗi con lặp lại dài nhất trong chuỗi. Chuỗi con lặp lại là một
# chuỗi xuất hiện ít nhất hai lần và không được chồng chéo nhau.
# chuỗi_con = s[i:i+độ_dài] : Câu lệnh này có nghĩa là cú pháp để cắt một phần con từ chuỗi s, bắt đầu từ chỉ số i và kéo dài đến một khoảng bằng i + độ_dài 
def question_35(s: str) -> str:
    chuoi_con_dai_nhat = ""
    n = len(s)
    for i in range(1, n // 2 + 1):
        chuoi_con_da_gap = set()
        for m in range(n - i + 1):
            chuoi_con = s[m:m + i]
            if chuoi_con in chuoi_con_da_gap:
                if len(chuoi_con) > len(chuoi_con_dai_nhat):
                    chuoi_con_dai_nhat = chuoi_con
            else:
                chuoi_con_da_gap.add(chuoi_con)
    return chuoi_con_dai_nhat
s = "aabcdeaabcd"
print(question_35(s))  

