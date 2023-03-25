from collections import deque
import sys

n, m=map(int, sys.stdin.readline().split())
info_list=[]

virus_list=[]
safe_list=[]
total=n*m-3 #처음의 안전구역, 3을 뺀 이유는 울타리 공간을 제외시키기 위해
for i in range(n):
    new_list=list(map(int, sys.stdin.readline().split()))
    for j in range(m):
        if new_list[j]==2:
            virus_list.append([i, j])
            total-=1
        
        elif new_list[j]==1:
            total-=1

        elif new_list[j]==0:
            safe_list.append([i, j])

    info_list.append(new_list)


d_row=[-1, 1, 0, 0]
d_col=[0, 0, -1, 1]

def view_result(info: list)->int:
    global total
    information=[]
    for _ in range(n):
        information.append(info[_].copy())

    visited=[]
    queue=deque()
    for virus in virus_list:
        queue.append(virus)
    
    current=total

    while queue:
        row, col=queue.popleft()
        if [row, col] in visited:
            continue
        visited.append([row, col])

        for i in range(4):
            delta_row, delta_col=row+d_row[i], col+d_col[i]
            if 0<=delta_row<n and 0<=delta_col<m:
                if information[delta_row][delta_col]==0 and [delta_row, delta_col] not in visited:
                    information[delta_row][delta_col]=2
                    queue.append([delta_row, delta_col])
                    current-=1

    return current #current는 남은 안전 구역의  갯수를 의미

max_value=0
result=[]
for i in range(total+1): 
    for j in range(i+1, total+2):  #브루트 포스 알고리즘
        for k in range(j+1, total+3):
            copied_list=[]
            for _ in range(n):
                copied_list.append(info_list[_].copy())
            
            copied_list[safe_list[i][0]][safe_list[i][1]]=1
            copied_list[safe_list[j][0]][safe_list[j][1]]=1
            copied_list[safe_list[k][0]][safe_list[k][1]]=1

            safe_result=view_result(copied_list)
            if safe_result>=max_value:
                max_value=safe_result
                result=copied_list

print(max_value)
