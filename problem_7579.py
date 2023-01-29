import sys

n, m = map(int, sys.stdin.readline().split())

memory_list = list(map(int, sys.stdin.readline().split()))
cost_list = list(map(int, sys.stdin.readline().split()))

pass_list = []

remove_list = []
for i in range(n):
    if cost_list[i] == 0:
        remove_list.append(i)
        m -= memory_list[i]

for i in reversed(remove_list):
    del cost_list[i]
    del memory_list[i]
n -= len(remove_list)


result_matrix = [[float("inf")] * (m + 1) for _ in range(n)] #이러한 방식 -> 메모리 과다 사용, 일정 포인트만을 저장하기

result_matrix[0][:(memory_list[0]+1)] = [cost_list[0]] * (memory_list[0] + 1) #첫번째의 cost가 0이면 오류 가능성

for i in range(1, n):
    # if i in pass_list: # -> 문제: 해당 행은 다 inf로 채워짐
    #     continue
    memory = memory_list[i]
    cost = cost_list[i]

    for j in range(0, m + 1):
        if j < memory: #초기 경우
            value = min(result_matrix[i - 1][j], cost)
            result_matrix[i][j] = value

        else:
            value = min(result_matrix[i - 1][j], result_matrix[i - 1][j - memory] + cost)
            result_matrix[i][j] = value


print(result_matrix[-1][-1])