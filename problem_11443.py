import sys
import math


n=int(sys.stdin.readline())

if n % 2 == 0:
    n += 1

original_matrix=[[1, 1], [1, 0]]

def multiply_matrix(a, b):
    result=[[0]*2 for _ in range(2)]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]

    return result

def remain_1000000007(a):
    for i in range(2):
        for j in range(2):
            a[i][j] = a[i][j] % 1000000007

    return a

exponential_2_list=[]
exponential_2_list.append(original_matrix)

while 2**(len(exponential_2_list)-1) <= n:
    exponential_2_list.append(remain_1000000007(multiply_matrix(exponential_2_list[-1], exponential_2_list[-1])))
exponential_2_list=exponential_2_list[:-1] #넘어선 것은 삭제

total_result=[[0]*2 for _ in range(2)]
for i in range(2):
    total_result[i][i]=1 #identiy matrix를 생성

while n>0:
    b_log=int(math.log2(n))
    total_result=remain_1000000007(multiply_matrix(total_result, exponential_2_list[b_log]))
    n -= 2**b_log


# if n % 2 == 1: #n이 홀수인 경우
#     print(total_result[1][0]) - 1

# else:
print(total_result[1][0] - 1)
