#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 9184                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: skaigroove <boj.kr/u/skaigroove>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/9184                           #+#        #+#      #+#     #
#    Solved: 2025/01/09 14:15:29 by skaigroove    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

def w(a,b,c):
    # a,b,c의 값의 크기를 제한해주고 있음
    if a <= 0 or b <= 0 or c <= 0 :
        return 1
    if a > 20 or b > 20 or c > 20 :
        return w(20, 20, 20)
    # 메모이제이션을 사용
    if dp[a][b][c]:
        return dp[a][b][c]
    if a<b<c:
        dp[a][b][c] = w(a,b,c-1)+w(a,b-1,c-1)-w(a, b-1, c)
        return dp[a][b][c] 
    # 위의 경우들이 아니면 default로 실행
    dp[a][b][c] = w(a-1, b, c)+w(a-1,b-1,c)+w(a-1,b,c-1)-w(a-1,b-1,c-1)
    return dp[a][b][c]

# dynamic programming 배열을 초기화 
dp = [[[0]*(21) for _ in range(21)] for _ in range(21)]

while 1:
    a, b, c = map(int, input().split()) # 리스트의 각 요소를 int로 변환하면서 받는다
    if a==-1 and b==-1 and c==-1:
        break
    print(f'w({a}, {b}, {c}) = {w(a,b,c)}')