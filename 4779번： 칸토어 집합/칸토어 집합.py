#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 4779                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: skaigroove <boj.kr/u/skaigroove>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/4779                           #+#        #+#      #+#     #
#    Solved: 2025/01/06 14:12:31 by skaigroove    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
def cantor_set(n):
    if n == 1:
        return "-"
    part = cantor_set(n // 3)
    return part + " " * (n // 3) + part

while True:
    try:
        N = int(input())
        result = cantor_set(3 ** N)
        print(result)
    except:
        break