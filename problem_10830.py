import sys
import math

n,b=map(int, sys.stdin.readline().split())

original_matrix=[]

for _ in range(n):
    original_matrix.append(list(map(int, sys.stdin.readline().split())))

exponential_2_list=[]
exponential_2_list.append(original_matrix)

def multiply_matrix(a, b):
    result=[[0]*n for _ in range(n)]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]

    return result

def remain_1000(a):
    for i in range(n):
        for j in range(n):
            a[i][j] = a[i][j] % 1000

    return a

while 2**(len(exponential_2_list)-1) <= b:
    exponential_2_list.append(remain_1000(multiply_matrix(exponential_2_list[-1], exponential_2_list[-1])))
exponential_2_list=exponential_2_list[:-1] #넘어선 것은 삭제

total_result=[[0]*n for _ in range(n)]
for i in range(n):
    total_result[i][i]=1 #identiy matrix를 생성

while b>0:
    b_log=int(math.log2(b))
    total_result=remain_1000(multiply_matrix(total_result, exponential_2_list[b_log]))
    b -= 2**b_log
    

for i in range(n):
    for j in range(n):
        total_result[i][j] = total_result[i][j] % 1000
        print(total_result[i][j], end= " ")
    print()