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
result_matrix[0].append([0, memory_list[0], cost_list[0]]) #sorting 기준은 memory 크기대로
result_matrix[0].append([memory_list[0], m, float("inf")])

def find_location(previous_row, location):
    if location < 0:
        return -1

    for i in range(len(previous_row)):
        if previous_row[i][0] < location <= previous_row[i][1]:
            return i



for i in range(1, n):
    memory = memory_list[i]
    cost = cost_list[i]
    previous_row = result_matrix[i - 1]
    for j in range(len(result_matrix[i - 1])):
        previous = previous_row[j]

        left = previous[0] - memory
        right = previous[1] - memory

        left_index = find_location(previous_row, left)
        right_index = find_location(previous_row , right)


        if left_index == right_index: #뺀 경우가 동일한 구간에 해당하는 경우 -> 해당 구간을 split할 필요없음
            # print(result_matrix[i - 1])
            # print(left_index)
            if result_matrix[i - 1][left_index][-1] + cost < previous[-1]: #새로운 경우가 더 좋은 경우
                result_matrix[i].append([previous[0], previous[1], result_matrix[i - 1][left_index][-1] + cost])

            else:
                result_matrix[i].append(previous) #기존의 것 그대로 넣기

        
        else: #구간을 쪼개야 하는 경우 #여기서 우리는 시작과 끝은 기존과 동일해야 함 #문제 발생 point
            if left_index < 0: #index_right의 index는 0보타 커야함
                if cost < previous[-1]:
                    result_matrix[i].append([previous[0], memory, cost])
                    result_matrix[i].append([memory, previous[1], previous[-1]])
                else:
                    result_matrix[i].append(previous) #오히려 더 별로면 그대로 삽입하기

            
            else:
                left_plus = [previous[0], memory + previous_row[left_index][0], min(previous[-1], previous_row[left_index][-1] + cost)]
                right_plus = [memory + previous_row[left_index][0], previous[1], min(previous[-1], previous_row[right_index][-1] + cost)]
                
                result_matrix[i].append(left_plus)
                result_matrix[i].append(right_plus)


print(result_matrix[-1][-1][-1])