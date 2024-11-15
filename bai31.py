# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 20:55:35 2024

@author: linh
"""

#bài 31:  Cho một đoạn văn là một chuỗi ký tự, 
#viết chương trình tìm ra các từ có tỷ lệ xuất hiện lớn
# hơn 20% trong đoạn văn
from collections import Counter
from typing import List
def question_31(paragraph: str, n: int) -> List[str]:
    các_từ = paragraph.split()
    đếm_từ = Counter(các_từ)
    tổng_các_từ = len(các_từ)
    result = [từ for từ, đếm in đếm_từ.items() if (đếm / tổng_các_từ) * 100 > 20]
#word_counts.items() trả về một danh sách các cặp, 
#mỗi cặp gồm một từ và số lần xuất hiện của từ đó trong đoạn văn bản text.
    return result
paragraph = "apple apple banana orange orange apple"
n = 2
print(question_31(paragraph, n))  