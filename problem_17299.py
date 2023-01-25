import sys

n = int(sys.stdin.readline())
info_list = list(map(int, sys.stdin.readline().split()))

f_list=[0] * 1000001

for i in range(n):
    f_list[info_list[i] - 1] += 1
#제일 오른쪽에 있는 값부터 처리한 다음 점차 왼쪽으로 이동시키기, 일단 빈 리스트에서 하나씩 추가, 맨 마지막에서는 리스트 뒤집기

answer_list=[]
stack=[] #stack에는 info_dict의 키를 저장, key는 index, stack 왼쪽이 bottom임, 항상 정렬되있는 상태이여야 함
         #stack은 bottom의 값이 제일 커야함, 이후 점점 작아짐
info_dict={}
for i in range(1000000):
    info_dict[i+1] = f_list[i]


for i in range(n-1, -1, -1):

    if len(stack) == 0:       #stack이 텅 빈 경우
        answer_list.append(-1)
        stack.append(i)
    
    else:
        flag = 0

        while info_dict[info_list[i]] >= info_dict[info_list[stack[-1]]]: #실패한 경우
            stack.pop(-1) #새로 들어올 값이 더 크므로
            
            if len(stack) == 0: #최종적으로 탐색에 실패한 경우
                answer_list.append(-1)
                stack.append(i)
                flag = 1
                break

        if flag == 0: #값이 -1이 아닌 경우
            answer_list.append(info_list[stack[-1]])
            stack.append(i)

answer_list = answer_list[::-1]

for i in range(n):
    print(answer_list[i], end=" ")