import sys

n = int(sys.stdin.readline())

info_list = []
for i in range(n):
    new_list = list(map(int, sys.stdin.readline().split()))
    info_list.append(new_list)

def make_descendant(value, index, color): #index는 현재 추가하려고 하는 곳의 index임
    return_list = []
    for i in range(3):
        if i == color:
            new_return = [10 ** 8, i]
            return_list.append(new_return)
            continue

        new_return =  [value + info_list[index][i], i]
        return_list.append(new_return) #2 by 2 행렬
    return sorted(return_list, key = lambda x: x[1])

def take_min_list(list1, list2): #list1, list2 는 각각 (3, 2), return은 (3, 2)
    min_list = []
    for i in range(len(list1)):
        if list1[i][0] < list2[i][0]:
            min_list.append(list1[i])

        else:
            min_list.append(list2[i])

    return min_list

def find_optim(infos): #처음에는 (2, 3, 2)처리, 다음부터는 (3, 3, 2)를 처리, return은 (3, 2)
    optim_list = infos[0]
    for i in range(1, len(infos)):
        optim_list = take_min_list(optim_list, infos[i])

    return optim_list

total_min = 10 ** 10

for i in range(3): #시작하는 경우가 각각 R, G, B임
    dynamic_list = [[[info_list[0][i], i]]] # 0: R, 1: G, 2: B

    new_list = []
    for k in range(3): #2번째 집의 case list
        if k == i:
            new_list.append([10 ** 8, i])
        else:
            new_value = dynamic_list[-1][0][0] + info_list[1][k]
            new_list.append([new_value, k])
    new_list.sort(key= lambda x: x[1]) #rgb 순서대로 정렬 (제일 낮은 값이 제일 먼저가 아님)
    dynamic_list.append(new_list)

    flag = 0
    for k in range(3): #3번째 집의 case list
        if k == i:
            continue

        else:
            if flag == 0:
                flag += 1
                first_list = make_descendant(dynamic_list[-1][k][0], 2, k) #(2, 2)
            else:
                second_list = make_descendant(dynamic_list[-1][k][0], 2, k) #(2, 2)
    result = find_optim([first_list,second_list]) #(3, 2)
    dynamic_list.append(result)

    for j in range(3, n): #4세대부터 generate
        first_list = make_descendant(dynamic_list[-1][0][0], j, 0)
        second_list = make_descendant(dynamic_list[-1][1][0], j, 1)
        third_list = make_descendant(dynamic_list[-1][2][0], j, 2)

        result = find_optim([find_optim([first_list, second_list]), third_list])
        dynamic_list.append(result)
    
    last = dynamic_list[-1]
    last.sort(key= lambda x: x[0])

    
    if last[0][1] == i:
        last.pop(0)
    total_min = min(total_min, last[0][0])


print(total_min)