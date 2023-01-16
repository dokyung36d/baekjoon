import sys

n=int(sys.stdin.readline())

info_list=list(map(int, sys.stdin.readline().split()))
#되도록이면 시간복잡도는 O(n)으로?
#stack의 제일 윗부분은 list의 제일 마지막으로 설정
info_dict={}
for i, value in enumerate(info_list):
    info_dict[i] = value

info_list=[n-i-1 for i in range(n)] #info_list에는 info_dict의 key를 저장, [5, 4, 3, 2, 1, 0]

#제일 뒤에 수가 스택의 제일 아래로?
#스택을 2개 설정, 다른 하나는 기존 스택에서 뽑아서 push, if 새로 들어온 값이 더 크면 pop?

stack_list=[]
output_list=[0] * n

for i in range(n):
    key=info_list.pop(-1)

    while True: 
        if len(stack_list) >= 1: #스택에 적어도 하나가 있는 경우
            if info_dict[stack_list[-1]] < info_dict[key]:
                stack_out=stack_list.pop(-1) #stack_list에서 탈출
                output_list[stack_out] = info_dict[key]
            
            else: #더 이상 stack에서 뽑아낼 수가 없는 경우
                break
        
        else: #stack_list가 텅 빈 경우
            break

    stack_list.append(key)

for i in range(len(stack_list)):
    output_list[stack_list[i]] = -1

for i in range(n):
    print(output_list[i], end=' ')