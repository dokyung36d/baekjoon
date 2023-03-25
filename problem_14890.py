import sys

n,l=map(int, sys.stdin.readline().split())

info_list=[]
for _ in range(n):
    new_list=list(map(int, sys.stdin.readline().split()))
    info_list.append(new_list)

possible_road=0

#처음은 좌우로 긴 도로가 가능한 경우를 탐색
for i in range(n):
    used=[] #만약 경사로의 밑면으로 사용이 되었다면 used에 "열"만을 저장한다.
    for j in range(n): #가능한 경우들을 나열 by using if, 해당 조건맨 아래에 continue를 사용
        if j==n-1: #불가능한 경우가 없는 경우 도달 가능
            possible_road+=1

        if j+1<n: #우측 탐사
            if info_list[i][j]==info_list[i][j+1]:
                continue

            elif info_list[i][j]+1==info_list[i][j+1]: #우측이 더 높은 경우
                if j-l+1>=0: #좌측까지 닿는 경우 가능
                    impossible=0
                    for k in range(j, j-l, -1):
                        if info_list[i][k]!=info_list[i][j+1]-1 or k in used: #경사로를 세우는 것이 불가능한 경우
                            impossible+=1
                        else:
                            used.append(k)
                    
                    if impossible>=1:
                        used=[]
                        break #for j in range(n)을 break한다
                
                else: #경사로를 둘 공간이 없는 경우
                    break
                
            elif info_list[i][j]-1==info_list[i][j+1]: #우측이 더 낮은 경우
                if j+l<n: #우측까지 닿는 경우
                    impossible=0
                    for k in range(j+1, j+l+1):
                        if info_list[i][k]!=info_list[i][j+1] or k in used:
                            impossible+=1
                        else:
                            used.append(k)
                    
                    if impossible>=1:
                        used=[]
                        break
                else:
                    break
            
            else: #차이가 2이상 나는 경우
                break




for j in range(n):
    used=[] #만약 경사로의 밑면으로 사용이 되었다면 used에 "행"만을 저장한다.
    for i in range(n): #가능한 경우들을 나열 by using if, 해당 조건맨 아래에 continue를 사용
        if i==n-1:
            possible_road+=1
        if i+1<n: #아래 탐색
            if info_list[i+1][j]==info_list[i][j]:
                continue
            
            elif info_list[i+1][j]+1==info_list[i][j]: #아래가 1작음
                if i+l<n:
                    impossible=0
                    for k in range(i+1, i+l+1):
                        if info_list[i+1][j]!=info_list[k][j] or k in used:
                            impossible+=1
                        else:
                            used.append(k)

                    if impossible>=1:
                        used=[]
                        break

                else:
                    break #범위 넘어가서 불가능

            elif info_list[i+1][j]-1==info_list[i][j]: #아래가 1크다.
                if i-l+1>=0:
                    impossible=0
                    for k in range(i, i-l, -1):
                        if info_list[k][j]!=info_list[i][j] or k in used:
                            impossible+=1
                        else:
                            used.append(k)
                    
                    if impossible>=1:
                        used=[]
                        break
                else:
                    break

            else: #차이가 2이상 나는 경우
                break




print(possible_road)
