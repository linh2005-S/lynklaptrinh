# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 21:49:35 2024

@author: linh
"""

#bai 38:  Giả sử bạn đang đứng trước cầu thang có hoặc 2 bậc
#. Viết một hàm để tính số cách bạn có thể leo hết bậc thang.
#n bậc thang. Mỗi lần bạn có thể bước lên 1 bậc
def question_38(n: int) -> int:
    if n == 0:
        return 1  
    elif n == 1:
        return 1  
    bậc_thang = [0] * (n + 1)
    bậc_thang[0] = 1 
    bậc_thang[1] = 1  
    for i in range(2, n + 1):
        bậc_thang[i] = bậc_thang[i - 1] + bậc_thang[i - 2]
    return bậc_thang[n]
n = 2
print(question_38(n))  