#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 17829                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: skaigroove <boj.kr/u/skaigroove>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/17829                          #+#        #+#      #+#     #
#    Solved: 2025/01/10 14:19:57 by skaigroove    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

def pooling(n, neural_network):
    # 2*2 커널을 기준
    kernel_size = 2
    
    # 메모이제이션
    dp = [[0] * (n // kernel_size) for _ in range(n // kernel_size)]
     
    # 커널로 나누기 위해 슬라이싱
    # 슬라이싱된 subarray의 2번째로 큰 값을 temp에 추가
    for i in range(0, n, kernel_size):  # 행
        for j in range(0, n, kernel_size):  # 열
            # 서브 배열 슬라이싱
            subarray = [row[j:j+kernel_size] for row in neural_network[i:i+kernel_size]]
            flattened = [value for row in subarray for value in row]  # 1차원으로 변환
            flattened.sort()  # 정렬
            second_largest = flattened[-2]  # 두 번째로 큰 값
            dp[i // kernel_size][j // kernel_size] = second_largest # dp에 넣어줌
    
    # Base Case
    if n == 2:
        return dp[0][0]
    
    # Recursive Case
    return pooling(n // 2, dp)

while 1:
    try:
        # 입력 받기
        n = int(input())  # 첫 번째 줄에서 크기 n을 받음
        neural_network = []

        # 2차원 배열 입력 받기
        for _ in range(n):
            row = list(map(int, input().split()))  # 각 줄을 공백 기준으로 나누어 정수로 변환
            neural_network.append(row)

        # 풀링 결과 출력
        print(pooling(n, neural_network))
    except EOFError:
        break
