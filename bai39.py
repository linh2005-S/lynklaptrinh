# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 21:52:58 2024

@author: linh
"""

#bai 39:Cho một dãy số nằm trong danh sách, đại diện cho giá của một mặt hàng thay đổi qua từng
#ngày. Viết một hàm để tìm ra lợi nhuận lớn nhất có thể đạt được bằng cách thực hiện một
#lần mua và một lần bán, với điều kiện là phải mua mới được bán.
def question_39(prices: list[int]) -> int:
    if not prices or len(prices) < 2:
        return 0 
    giá_ban_đầu = prices[0]  
    lợi_nhuận = 0  
    for giá in prices[1:]:
        lợi_nhuận = max(lợi_nhuận, giá - giá_ban_đầu)
        giá_ban_đầu = min(giá_ban_đầu, giá)
    return lợi_nhuận
prices =  [7, 6, 4, 3, 1]
print(question_39(prices)) 