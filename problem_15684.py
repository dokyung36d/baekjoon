from collections import deque
import sys

n, m, h=map(int, sys.stdin.readline().split())

width_list=[[0]*(n-1) for _ in range(h)] #h*(n-1) 행렬

for _ in range(m):
    w_row, w_col=map(int, sys.stdin.readline().split())
    width_list[w_row-1][w_col-1]=1 #가로선이 들어있는 부분은 1, 아니면 0
#결국 내려가는 횟수는 h로 동일하다.

def find_result(information: list):
    falsed=0
    result_list=[]
    for j in range(n): #여기서 j는 col을 의미, 시작 지점
        current_col=j

        for i in range(h):
            if 0<=current_col<n-1: 
                if information[i][current_col]==1:
                    current_col+=1
                    continue

            if current_col-1>=0:
                if information[i][current_col-1]==1:
                    current_col-=1
                    continue
            
            else: #좌우로 이동하는 것이 불가능
                pass


        result_list.append(current_col)
        if current_col!=j:
            falsed+=1
    
    if falsed==0:
        return 1 #성공을 의미
    else:
        return result_list


def right_okay(info, row, col): #여기서의 information은 위에서의 width_list와 같이 처리한다.

    if col<0 or col>=n-1:
        return False
    
    if row<0 or row>=h:
        return False

    if 0<=col<n-1:
        if info[row][col]==1: #이미 가로선이 존재하는 경우
            return False 

    if 0<=col-1<n-1: #왼쪽 확인
        if info[row][col-1]==1:
            return False
    
    if col+1<n-1: #우측에 추가하였을 때 한 칸 더 오른쪽에 있는 것과 겹칠 때
        if info[row][col+1]==1:
            return False
    
    return True

min_value=5

success=0

queue=deque()
queue.append([width_list, [0, 0], 0]) #중간에 list는 지금까지 탐색한 위치, 뒤의 0은 총 가로선을 더한 갯수
num=0
while queue:

    x=queue.popleft()

    if x[2]>3:
        continue

    if find_result(x[0])==1:
        if x[2]<min_value:
            min_value=x[2]
        success+=1
        continue

    copied_info=[]
    for i in range(h):
        copied_info.append(x[0][i].copy())
    
    now_row, now_col=x[1][0], x[1][1]


    if now_col==n-2:
        if now_row<h-1:
            queue.append([copied_info, [now_row+1, 0], x[2]]) #가로선을 만들지 않고 넘어가는 경우
    else:
        queue.append([copied_info, [now_row, now_col+1], x[2]])
        

    if right_okay(copied_info, now_row, now_col)==True and x[2]<3:
        copied=[]
        for _ in range(h):
            copied.append(x[0][_].copy())

        copied[now_row][now_col]=1 #우측에 가로선을 만들기 성공
        if now_col!=n-2:
            if now_col==n-3 and now_row<h-1:
                queue.append([copied, [now_row+1, now_col], x[2]+1])
            elif now_col!=n-3:
                queue.append([copied, [now_row, now_col+2], x[2]+1])
        
        elif now_col==n-2 and now_row<h-1:
            queue.append([copied, [now_row+1, 0], x[2]+1])


if success==0:
    print(-1)
else:
    print(min_value)
