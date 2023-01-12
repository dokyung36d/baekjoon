import sys
import math
#먼저 고윳값 분해를 통해 접근, 1,000,000을 넘어서면 나머지로 처리?

n=int(sys.stdin.readline())

original_matrix=[[1, 1], [1, 0]]

def multiply_matrix(a, b):
    result=[[0]*2 for _ in range(2)]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]

    return result



exponential_2_list=[]
exponential_2_list.append(original_matrix)

while 2**(len(exponential_2_list)-1) <= n:
    exponential_2_list.append(multiply_matrix(exponential_2_list[-1], exponential_2_list[-1]))
exponential_2_list=exponential_2_list[:-1] #넘어선 것은 삭제

total_result=[[0]*2 for _ in range(2)]
for i in range(2):
    total_result[i][i]=1 #identiy matrix를 생성

while n>0:
    b_log=int(math.log2(n))
    total_result=multiply_matrix(total_result, exponential_2_list[b_log])
    n -= 2**b_log

print(total_result[1][0])