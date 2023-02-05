import sys

#bfs로 진해하되, 더 큰 수가 나오는 경우에 한해서만 candidate리스트에 추가하기
#pop을 할 때마다 지금까지 제일 작은 수인지 확인 -> 내림차순인가? , 만약 정렬되어있는 상태이고 k가 남아 있으면 추가적으로 고려

n, k = map(int, sys.stdin.readline().split())


length = len(str(n))
candidate_list = []
candidate_list.append([n, k])

max_num = candidate_list[0]


while candidate_list:
    info = candidate_list.pop(0)
    prev_num = str(info[0])

    for i in range(length - 1):
        search_list = prev_num[i + 1:]
        a = [i[0] for i in sorted(enumerate(search_list), key=lambda x:x[1])]
        while a: #오른쪽 것을 탐색할 때 큰 순서가 먼저 하도록 하면 개선의 여지가 큼
            max_index = i + 1 + max(enumerate(a), key=lambda x: (x[1], x[0]))[0]
            prev_max_value = search_list[max(enumerate(a), key=lambda x: (x[1], x[0]))[0]]
            a.pop(max_index - i - 1) #만약 제일 큰 수가 2개 이상 존재하면 오류가 발생할 수 있음
                                     #동일한 순서로 처리되어야 하지만 앞에 있는 것이 우선시 탐색됨 ->해결해야함

            curr_num = int(prev_num[:i] + prev_num[max_index] + prev_num[i + 1:max_index] + prev_num[i] + prev_num[max_index + 1:])
            plus_candidate_list = []

            if curr_num <= int(prev_num) or str(curr_num)[:i] < str(max_num[0])[:i]: #바꾼 경우가 오히려 더 좋지 않은 경우
                pass
                
            else:
                if curr_num > int(max_num[0]):
                    max_num = [curr_num, info[1] - 1]
                if info[1] > 1:
                    candidate_list.append([curr_num, info[1] - 1])
                    # while a and search_list[max(enumerate(a), key=lambda x: (x[1], x[0]))[0]] == prev_max_value:
                    #     new_max_index = i + 1 + max(enumerate(a), key=lambda x: (x[1], x[0]))[0]
                    #     new_max_value = a[max(enumerate(a), key=lambda x: (x[1], x[0]))[0]]
                    #     a.pop(new_max_index - i - 1)

                    #     new_curr_num = int(prev_num[:i] + prev_num[new_max_index] + prev_num[i + 1:new_max_index] + prev_num[i] + prev_num[new_max_index + 1:])

                    #     plus_candidate_list.append([new_curr_num, info[1] - 1])
                    # candidate_list.extend(plus_candidate_list)
                        

max_num[0] = str(max_num[0])

if len(max_num[0]) == 1:
    print(-1)

elif len(max_num[0]) == 2 and max_num[0][1] == "0":
    print(-1)

else:
    if max_num[1] != 0:
        if max_num[1] % 2 == 0:
            print(int(max_num[0]))
        
        else:
            flag = 0

            for i in range(len(max_num[0]) - 1):
                if max_num[0][i] == max_num[0][i + 1]:
                    flag += 1
                    break
            
            if flag == 0:
                print(int(max_num[0][:-2] + max_num[0][-1] + max_num[0][-2]))

            else:
                print(int(max_num[0]))
    else:
        print(int(max_num[0]))