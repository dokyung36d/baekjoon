import sys

n, k =map(int, sys.stdin.readline().split())
info_list=[]
info_dict={}

for i in range(n):
    new_info=list(map(int, sys.stdin.readline().split()))
    info_list.append(new_info) #(무게, 가치)
    info_dict[i] = new_info

#info_list.sort(key= lambda x: x[0])

dynamic_programming_list=[[0]*(k+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        if info_list[i-1][0] > j:
            dynamic_programming_list[i][j] = dynamic_programming_list[i-1][j]
        
        else:
            dynamic_programming_list[i][j] = max(dynamic_programming_list[i-1][j], 
            dynamic_programming_list[i-1][j-info_list[i-1][0]] + info_list[i-1][1])

print(dynamic_programming_list[-1][-1])