# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 10:42:05 2024

@author: linh
"""

#bai 26: Cho một chuỗi s chỉ gồm các chữ cái viết thường và viết hoa. 
#Viết một hàm để trả về độ dài của chuỗi palindrome dài nhất có thể được tạo ra từ các chữ cái đó.
# Các chữ cái có phân biệt chữ hoa và chữ thường (ví dụ: "Aa" không được coi là một palindrome).
# Palindrome là chuỗi đọc giống nhau từ trái sang phải và ngược lại.

def question_26(s: str) -> int:
   dem = {}
   for char in s:
       dem[char]= dem.get(char, 0) + 1
   dodai =0
   for i in dem.values():
        if i%2==0:
            dodai +=i
        else:
            dodai += i -1
   if dodai < len(s):
       dodai +=1
   return dodai
s = "abccccdd"
print(question_26(s))


