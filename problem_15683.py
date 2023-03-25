from collections import deque
import sys

n, m=map(int, sys.stdin.readline().split())

info_list=[]
cctv_list=[]
num_invisible=n*m

num_cctv=0
num_zero=0
for i in range(n):
    new_list=list(map(int, sys.stdin.readline().split()))
    for j in range(m):
        if new_list[j]!=0 and new_list[j]!=6:
            cctv_list.append([new_list[j], i, j]) #첫 element는 cctv의 종류
            num_cctv+=1
            num_invisible-=1
        if new_list[j]==0:
            num_zero+=1

    info_list.append(new_list)

#상하좌우 순서대로
d_row=[-1, 1, 0, 0]
d_col=[0, 0, -1, 1]

def up(information: list, cctv_position: list, num_special: int):
    copy_list=[]
    for _ in range(n):
        copy_list.append(information[_].copy())
    cctv_row, cctv_col=cctv_position[0], cctv_position[1]

    for i in range(cctv_row-1, -1, -1):
        if copy_list[i][cctv_col]==0:
            num_special+=1
            copy_list[i][cctv_col]='#'

        elif copy_list[i][cctv_col]==6: #벽을 만난 경우
            break
        
        elif copy_list[i][cctv_col]=='#':
            continue #이미 처리가 되어있음

    return [copy_list, num_special]

def down(information: list, cctv_position: list, num_special: int)-> list:
    copy_list=[]
    for _ in range(n):
        copy_list.append(information[_].copy())
    cctv_row, cctv_col=cctv_position[0], cctv_position[1]

    for i in range(cctv_row+1, n):
        if copy_list[i][cctv_col]==0:
            num_special+=1
            copy_list[i][cctv_col]='#'

        elif copy_list[i][cctv_col]==6: #벽을 만난 경우
            break
        
        elif copy_list[i][cctv_col]=='#':
            continue #이미 처리가 되어있음
    
    return [copy_list, num_special]


def left(information: list, cctv_position: list, num_special: int)->list:
    copy_list=[]
    for _ in range(n):
        copy_list.append(information[_].copy())
    cctv_row, cctv_col=cctv_position[0], cctv_position[1]

    for j in range(cctv_col-1, -1, -1):
        if copy_list[cctv_row][j]==0:
            num_special+=1
            copy_list[cctv_row][j]='#'

        elif copy_list[cctv_row][j]==6: #벽을 만난 경우
            break
        
        elif copy_list[cctv_row][j]=='#':
            continue
    
    return [copy_list, num_special]

def right(information: list, cctv_position: list, num_special: int)->list:
    copy_list=[]
    for _ in range(n):
        copy_list.append(information[_].copy())
    cctv_row, cctv_col=cctv_position[0], cctv_position[1]

    for j in range(cctv_col+1, m):
        if information[cctv_row][j]==0:
            num_special+=1
            copy_list[cctv_row][j]='#'

        elif information[cctv_row][j]==6: #벽을 만난 경우
            break
        
        elif information[cctv_row][j]=='#':
            continue

    return [copy_list, num_special]

#1번은 4가지 경우,2번은 2가지, 3번은 4가지, 4번은 4가지
vector_info=[[[up], [down], [left], [right]], [[up, down], [left, right]], 
[[up, right], [right, down], [down, left], [left, up]],
 [[left, up, right], [up, right, down], [right, down, left], [down, left, up]], 
 [up, right, down, left]]


queue=deque()
queue.append([info_list, 0, 0]) #[현재 상황, 사용한 cctv, 현재 감시되고 있는 구역의 갯수]

max_sharp=0
max_info=[]

while queue:
    x=queue.popleft()
    information, num_used, num_sharp=x[0], x[1], x[2] #num_used는 지금까지 사용한 cctv의 갯수
    if num_used==num_cctv:
        continue
    vector=cctv_list[num_used][0] #cctv의 모양
    if vector!=2 and vector!=5:
        for i in range(4):
            if vector==1:
                result=vector_info[vector-1][i][0](information, cctv_list[num_used][1:], num_sharp)
                if result!=False:
                    if result[1]>=max_sharp:
                        max_sharp=result[1]
                        max_info=result[0]
                    queue.append([result[0], num_used+1, result[1]])
                
            elif vector==3:
                num_repeat=0
                result=vector_info[vector-1][i][num_repeat](information, cctv_list[num_used][1:], num_sharp)
                while num_repeat!=1:
                    num_repeat+=1
                    result=vector_info[vector-1][i][num_repeat](result[0], cctv_list[num_used][1:], result[1])
                if result!=False:
                    if result[1]>=max_sharp:
                        max_sharp=result[1]
                        max_info=result[0]
                    queue.append([result[0], num_used+1, result[1]])

            elif vector==4:
                num_repeat=0
                result=vector_info[vector-1][i][num_repeat](information, cctv_list[num_used][1:], num_sharp)
                while num_repeat!=2:
                    num_repeat+=1
                    result=vector_info[vector-1][i][num_repeat](result[0], cctv_list[num_used][1:], result[1])
                if result!=False:
                    if result[1]>=max_sharp:
                        max_sharp=result[1]
                        max_info=result[0]
                    queue.append([result[0], num_used+1, result[1]])
            

    
    elif vector==2: #2번 모양 cctv
        for i in range(2):
            result=vector_info[1][i][0](information, cctv_list[num_used][1:], num_sharp)
            result=vector_info[1][i][1](result[0], cctv_list[num_used][1:], result[1])
            if result!=False:
                if result[1]>=max_sharp:
                    max_sharp=result[1]
                    max_info=result[0]
                queue.append([result[0], num_used+1, result[1]])

    elif vector==5:
        num_repeat=0
        result=vector_info[4][num_repeat](information, cctv_list[num_used][1:], num_sharp)
        
        while num_repeat!=3:
            num_repeat+=1
            result=vector_info[vector-1][num_repeat](result[0], cctv_list[num_used][1:], result[1])
        if result!=False:
            if result[1]>=max_sharp:
                max_sharp=result[1]
                max_info=result[0]
            queue.append([result[0], num_used+1, result[1]])



print(num_zero-max_sharp)
