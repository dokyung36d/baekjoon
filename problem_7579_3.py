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

#변화 포인트만을 저장
result_matrix = [[] for _ in range(n)] #시작과 마무리를 저장
result_matrix[0].append([0, min(memory_list[0], m), cost_list[0]]) #sorting 기준은 memory 크기대로
if memory_list[0] < m:
    result_matrix[0].append([memory_list[0], m, float("inf")])

for i in range(1, n):
    memory = memory_list[i]
    cost = cost_list[i]

    previous_row = result_matrix[i - 1]
    current_row = [[0, memory, cost]]

    for j in range(len(previous_row)):
        current_row.append([previous_row[j][0] + memory, previous_row[j][1] + memory, previous_row[j][2] + cost])

    prev_index = 0
    curr_index = 0

    append_list = []

    prev_len = len(previous_row)
    curr_len = prev_len + 1

    while prev_index != prev_len and curr_index != curr_len:
        start_point = max(previous_row[prev_index][0], current_row[curr_index][0])
        end_pint = min(previous_row[prev_index][1], current_row[curr_index][1])
        total_cost = min(previous_row[prev_index][-1], current_row[curr_index][-1])

        try:
            if result_matrix[i][-1][-1] == total_cost: #굳이 해당 구간을 나눌 필요가 없는 경우
                result_matrix[i][-1] = [result_matrix[i][-1][0], end_pint, total_cost]
            else:
                result_matrix[i].append([start_point, end_pint, min(previous_row[prev_index][-1], current_row[curr_index][-1])])
        except IndexError:
            result_matrix[i].append([start_point, end_pint, min(previous_row[prev_index][-1], current_row[curr_index][-1])])

        if previous_row[prev_index][1] > current_row[curr_index][1]: 
            curr_index += 1
        else:
            prev_index += 1
        
print(result_matrix[-1][-1][-1])