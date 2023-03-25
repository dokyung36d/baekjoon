import sys

n=int(sys.stdin.readline())

info=[]

for _ in range(n):
    new_info=(list(sys.stdin.readline()[:-1].split(" ")))
    for i in range(len(new_info)):
        new_info[i]=int(new_info[i])
    info.append(new_info)
#드래곤 커브를 한 단계씩 업그레이드 할 때마다 길이가 두배가 되는 특성이 존재함
#idea: 회전의 기준이 되는 point를 설정한 다음 함수를 제작? ->회전 행렬을 이용하여 해결?

#기준점을 원점으로 이동, 회전행렬 적용, 기준점을 본래의 위치로 이동시킴

def subtract_list(list1, list2):
    subtracted = list()
    for item1, item2 in zip(list1, list2):
        item = item1 - item2
        subtracted.append(item)
    
    return subtracted

def rotate_vector_clock_90(vector_list): #vector_list는 일종의 행렬 형태, 각 행벡터의 크기는 4: (시작 x, 시작 y, 도착 x, 도착 y)
    standard_x, standard_y= vector_list[-1][2], vector_list[-1][3]
    minus_list=[standard_x, standard_y, standard_x, standard_y]
    n=len(vector_list)
    for i in range(n):
        new_vector = subtract_list(vector_list[n-i-1], minus_list)
        new_vector = [-new_vector[3], new_vector[2],-new_vector[1], new_vector[0]] #회전시킨 뒤 벡터 방향을 바꿈
        new_vector = subtract_list(new_vector, [item*(-1) for item in minus_list])
        vector_list.append(new_vector)
    return vector_list

def find_dragon_curve(information):
    start_x, start_y = information[0], information[1]
    direction=information[2]
    generation=information[3]
    vectors=[]
    if direction==0:
        vectors.append([start_x, start_y, start_x+1, start_y])
    
    elif direction==1:
        vectors.append([start_x, start_y, start_x, start_y-1])
    
    elif direction==2:
        vectors.append([start_x, start_y, start_x-1, start_y])
    
    elif direction==3:
        vectors.append([start_x, start_y, start_x, start_y+1])


    for i in range(int(generation)):
        vectors=rotate_vector_clock_90(vectors)

    return vectors

#한 선분은 최대 2개의 정사각형의 한 변을 구성할 수 있음 ->트리 구조를 통해 해결?
#길이가 1인 벡터를 중점을 통해 표현

total_vector_list=[]
for i in range(len(info)):
    dragon_vector_list=find_dragon_curve(info[i])
    for j in range(len(dragon_vector_list)):
        total_vector_list.append(list(dragon_vector_list[j][0:2]))
        total_vector_list.append(list(dragon_vector_list[j][2:4]))

total_vector_list.sort(key= lambda x: (x[1], x[0]))
res = []
[res.append(x) for x in total_vector_list if x not in res]
y_list=[]
[y_list.append(x[1]) for x in res if x[1] not in y_list]
#각 점의 y좌표마다 리스트를 따로 만들면 괜찮을 것 같음

total_point_list=[[] for _ in range(101)]

for re in res:
    if re[1]<0 or re[1]>100 or re[0]<0 or re[0]>100:
        continue
    total_point_list[re[1]].append(re)

verified_rectangle_list=[]

#탐색할 때 무조건 오른쪽, 아래에 있는 정사각형만을 탐색함(중복 탐색을 방지하기 위해)
for y in y_list:
    point_list=total_point_list[y]
    for point in point_list:
        if point[0]==100 or point[1]==100:
            continue
        if (([point[0]+1, point[1]] in point_list) and ([point[0], point[1]+1] in total_point_list[y+1])
        and ([point[0]+1, point[1]+1] in total_point_list[y+1])):
            verified_rectangle_list.append(point)

print(len(verified_rectangle_list))
