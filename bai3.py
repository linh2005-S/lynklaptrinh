# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 22:53:24 2024

@author: linh
"""
#bài 3: Viết một hàm nhận vào một chuỗi, 
#sau đó đếm và in ra số lượng ký tự viết hoa và ký tự viết thường trong chuỗi đó.def question_3(s: str) -> (int, int):
def question_3(s: str) -> (int, int):
    return len([i for i in s if i.isupper()]), len([i for i in s if i.islower()])
#isupper :Danh sách chứa các chữ cái in hoa trong chuỗi
#islower :Danh sách chứa các chữ cái in thường trong chuỗi s
#len() được sử dụng để lấy độ dài của mỗi danh sách, tương ứng với số lượng chữ cái in hoa và in thường. Cuối cùng, hàm trả về một tuple gồm hai số lượng này.
print(question_3("Hello World"))