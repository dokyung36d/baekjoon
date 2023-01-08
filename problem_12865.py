import sys

n, k =map(int, sys.stdin.readline().split())
info_list=[]
info_dict={}

for i in range(n):
    new_info=list(map(int, sys.stdin.readline().split()))
    info_list.append(new_info)
    info_dict[i] = new_info

#info_list.sort(key= lambda x: x[0])

dynamic_list=[]
candidate_list=[[] for _ in range(k+1)]

for i in range(k+1):
    if i==0:
        dynamic_list.append([0, 0,  [info_dict[j] for j in range(n)]]) #[배낭의 무게, 배낭의 가치, [아직 넣지 않은 물건들]]
        #가방의 크기가 0이면 넣을 수 있는 것이 없고 모든 것들은 넣지 않은 상태

    else:
        if len(candidate_list[i]) == 0: #만약 후보가 없을 경우 그 직전의 값을 차용함
            dynamic_list.append(dynamic_list[i-1])

        elif candidate_list[i][0][1] > dynamic_list[i-1][1]:
            dynamic_list.append(candidate_list[i][0])

        else:
            dynamic_list.append(dynamic_list[i-1]) #(무게, 가치)

    for j in range(len(dynamic_list[i][2])): #다른 가능한 후보들을 추가함
        try: #개선 point: 최종적으로 우리는 candidate_list에서 best만을 선택함 ->넣을 때 비교를 통해 항상 비교를 통해 길이를 1로 유지 가능
            if len(candidate_list[dynamic_list[i][0] + dynamic_list[i][2][j][0]]) == 0:
                candidate_list[dynamic_list[i][0] + dynamic_list[i][2][j][0]].append(
                    [dynamic_list[i][0] + dynamic_list[i][2][j][0],
                    dynamic_list[i][1] + dynamic_list[i][2][j][1], dynamic_list[i][2][:j] + dynamic_list[i][2][j+1:]])
            else:
                if (candidate_list[dynamic_list[i][0] + dynamic_list[i][2][j][0]][0][1] <
                 dynamic_list[i][1] + dynamic_list[i][2][j][1]):
                    candidate_list[dynamic_list[i][0] + dynamic_list[i][2][j][0]][0] = [dynamic_list[i][0] + dynamic_list[i][2][j][0],
                    dynamic_list[i][1] + dynamic_list[i][2][j][1], dynamic_list[i][2][:j] + dynamic_list[i][2][j+1:]]

        except IndexError: #배낭의 무게가 한계를 넘어선 경우
            continue


print(dynamic_list[-1][1])