import sys

n,m=sys.stdin.readline().split(" ")
n=int(n)
m=int(m)
num_chicken=0
chicken_locations=[]
home_locations=[]
chicken_dict={}

info_list=[]
for i in range(n):
    new_list=list(sys.stdin.readline().split(" "))
    for j in range(n):
        new_list[j] = int(new_list[j])
        if new_list[j] == 2:
            num_chicken+=1
            new_list[j] = 0 #치킨집을 전부 삭제한 후, 나중에 추가하는 형식으로 진행
            chicken_locations.append([i, j])
            chicken_dict[(i, j)] =num_chicken
        
        elif new_list[j] == 1:
            home_locations.append([i, j])
    info_list.append(new_list)


num_haveto_delete_chicken=num_chicken-m


#단순히 best인 것만을 선택-> greedy 알고리즘 -> 추후에 문제가 생길수도 있음
#일단 dfs로 결과값을 하나 구한 다음, 브루트포스로 가다가 이미 값이 좋지 않으면 바로 손절
#치킨집이 줄어들수록 거리는 계속해서 증가함
#현재 우리는 거리의 최솟값을 구하고 싶음

#개선 point: 현재 방법론은 치킨집을 추가하는 순서에 중점을 둠 ->만약 현재 상태가 이전에 찾은 치킨집과 그대로임-> 결과는 완벽히 동일

def find_total_distance(home_location_list, chicken_location_list): #나중에 delete_chicken제거
    total_distance=0                                                #ex1 case에 너무 복잡해짐

    for home_location in home_location_list:
        home_chicken_distance_list=[]

        for chicken_location in chicken_location_list:
            home_chicken_distance_list.append(abs(home_location[0]-chicken_location[0]) + abs(home_location[1]-chicken_location[1]))
        total_distance += min(home_chicken_distance_list)

    return total_distance

current_distance = find_total_distance(home_locations, chicken_locations) #문제 없음
min_distance=10**10

visited_dict={}

    #현재 치킨 갯수, 
def dfs(num_chicken, previous_distance, map, will_plus_chicken, chicken_location_list, possible_chicken_locations):
    global min_distance

    if num_chicken==m:
        return previous_distance

    current_map=map.copy()
    current_map[will_plus_chicken[0]][will_plus_chicken[1]]=2 #빈 곳을 치킨집을 변경시킴
    chicken_location_list.append(will_plus_chicken)
    current_distance=find_total_distance(home_locations, chicken_location_list)
    chicken_location_set=[]

    for chicken_location in chicken_location_list:
        chicken_location_set.append(chicken_dict[(chicken_location[0], chicken_location[1])])
    chicken_location_set.sort()
    if tuple(chicken_location_set) in visited_dict: #우리가 이전에 이미 방문한 경우와 동일한 경우
        return visited_dict[set(chicken_location_set)]

    visited_dict[tuple(chicken_location_set)] = current_distance
    #set(tuple(chicken_location_tuple))에서는 에러가 발생하지 않음


    if previous_distance == current_distance: #치킨집을 추가하더라도 결과의 차이가 없는 경우
        return previous_distance #해당 치킨집 추가 경로는 의미가 없음 -> 오히려 낭비가 발생했다고 봐야 함

    if current_distance > min_distance:
        return previous_distance

    for possible_chicken in possible_chicken_locations:
        new_chicken_location_list=chicken_location_list.copy()
        new_chicken_location_list.append(possible_chicken)

        new_possible_chicken_locations=possible_chicken_locations.copy()
        new_possible_chicken_locations.remove(possible_chicken)

        new_result = dfs(num_chicken+1, current_distance, current_map, possible_chicken, new_chicken_location_list, new_possible_chicken_locations)
        if new_result < min_distance:
            min_distance=new_result

    return min_distance

min_candidate=[]

for chicken_location in chicken_locations: #시작 포인트를 각각 설정
    one_minus_chicken=chicken_locations.copy()
    one_minus_chicken.remove(chicken_location)
    result=dfs(0, 10**5, info_list, chicken_location, [], one_minus_chicken)
    if result < min_distance:
        min_distance=result

print(min_distance)
