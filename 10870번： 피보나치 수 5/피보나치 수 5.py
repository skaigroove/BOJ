#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10870                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: skaigroove <boj.kr/u/skaigroove>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10870                          #+#        #+#      #+#     #
#    Solved: 2024/10/31 21:58:45 by skaigroove    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# 똑같은 값을 여러 번 구한다면, 배열에 저장하여 재사용 하는 것이 좋다 (메모이제이션 기법)

# Case 1
# 재귀함수로 구현했지만, 메모이제이션이 없어 중복된 계산이 많이 일어나게 된다.
'''
def fibo(n):
    # base 
    if n == 0:
        return 0
    if n == 1:
        return 1
    # recursive
    return fibo(n-1) + fibo(n-2)

n = int(input())
print(fibo(n))

'''

# Case 2
# 메모이제이션을 사용한 재귀함수 구현
def fibo(n):
    global arr

    # base 
    if arr[n] != -1: # -1이 아니라면, 종료조건! 원하는 값에 다다름!
        return arr[n]
    
    # recursive
    arr[n] = fibo(n-1) + fibo(n-2)
    
    return arr[n]
    
n = int(input())
arr = [-1] * (n + 2) # (n+2)의 크기만큼 배열의 값들을 모두 -1로 초기화
arr[0] = 0
arr[1] = 1

print(fibo(n))