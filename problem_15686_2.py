import sys

n,m=sys.stdin.readline().split(" ")
n=int(n)
m=int(m)

num_chicken=0
chicken_locations=[]
home_locations=[]

info_list=[]
for i in range(n):
    new_list=list(sys.stdin.readline().split(" "))
    for j in range(n):
        new_list[j] = int(new_list[j])
        if new_list[j] == 2:
            num_chicken+=1
            new_list[j] = 0 #치킨집을 전부 삭제한 후, 나중에 추가하는 형식으로 진행
            chicken_locations.append((i, j))
        
        elif new_list[j] == 1:
            home_locations.append((i, j))
    info_list.append(new_list)

final_answer=10**5

visited=[False] * (num_chicken+1)
def dfs(index, chicken_count):
    global m, final_answer, chicken_locations
    if index > len(chicken_locations):
        return 
    final_distace=0
    if chicken_count==m:
        for row1, col1 in home_locations:
            distance=10**5

            for i, chicken_location in enumerate(chicken_locations):
                if visited[i]:
                    row2, col2=chicken_location
                    distance=min(distance, abs(row1 - row2) + abs(col1 - col2))
            final_distace += distance

        final_answer = min(final_answer, final_distace)

    visited[index] = True
    dfs(index+1, chicken_count+1)
    visited[index] = False
    dfs(index+1, chicken_count)

dfs(0, 0)
print(final_answer)
Footer
© 2023 GitHub, Inc.
Footer navigation
Terms
Privacy
Secu
