import sys

n=int(sys.stdin.readline())

info_list=[]
for i in range(n):
    info_list.append(list(map(int, sys.stdin.readline().split())))

result_matrix=[[0]*n for _ in range(n)]

for i in range(1, n): #몇번째 대각선 라인?
    for j in range(n-i): #해당 대각선 라인에서 채워야하는 칸의 갯수
        #현재 채울려는 칸의 좌표는 [j][i+j]  --> info_list[j] 부터 info_list[i+j] 까지의 행렬곱
        temp = 2**32
        for k in range(i): #한 칸을 채우기 위해 총 check해야 하는 경우의 수
            new_candidate = (result_matrix[j][i+j-(k+1)] + result_matrix[i+j-k][i+j]
            + info_list[j][0] * info_list[i+j-(k+1)][1] * info_list[i+j][1])
            temp = min(temp, new_candidate)
        result_matrix[j][i+j] = temp

print(result_matrix[0][-1])