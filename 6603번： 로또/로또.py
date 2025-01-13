#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 6603                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: skaigroove <boj.kr/u/skaigroove>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/6603                           #+#        #+#      #+#     #
#    Solved: 2025/01/10 18:15:23 by skaigroove    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
    # 몇 개의 정수 stream이 오던 간에 6개를 뽑아야 함
    # 모든 뽑을 수 있는 모든 경우의 수를 출력해야 함
    # stream에 중복이 있을 수 있기 때문에 고려해 줘야 함

    # 6개를 겹치지 않게 뽑으려면 어떻게 해야할까?
    # DFS를 이용해야한다
    # DFS란? 깊이 우선 탐색
    # 갔던 노드는 다시 안 가도록 하는 방식으로 모든 조합의 방식을 찾는 것   
def dfs(S, start, combination, result):
    # 종료 조건: 길이가 6인 조합을 찾았을 때
    if len(combination) == 6:
        result.append(combination[:])  # 현재 조합을 결과에 추가
        return
    
    # 숫자들을 하나씩 선택하며 탐색
    for i in range(start, len(S)):
        combination.append(S[i])  # 숫자 추가
        dfs(S, i + 1, combination, result)  # 다음 숫자 탐색
        combination.pop()  # 추가했던 숫자를 제거 (백트래킹)
        
# 입력 처리
k, *S = map(int, input().split())
result = []

# DFS로 조합 찾기
dfs(S, 0, [], result)

# 결과 출력
for comb in result:
    print(*comb)