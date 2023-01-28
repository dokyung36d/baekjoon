import sys

n, k = map(int, sys.stdin.readline().split())
#일단 stack에 n-k의 개의 수를 넣어둠, 맨 마지막 n-k개를

info = list(sys.stdin.readline())[:-1]

#큰 수에 제일 큰 영향을 미치는 수는 왼쪽에 있는 수 ->제일 오른쪽 수를 스택에 제일 아래
#감소하다 증가하는 지점을 stack에서 제거하기
stack = info[k:]
ascend_stack=[] #요거를 아예 스택으로 하기

for i in range(n-k-1):
    if stack[i] < stack[i + 1]:
        ascend_stack.append(i) #ascend_stack의 길이는 진행이 될수록 짧아질 것임

front_value=stack[0]

for i in range(k-1, -1, -1):
    new_candidate = info[i]

    if new_candidate >= front_value: #새로 들어올 제일 앞자리 수가 이전 제일 앞자리수보다 커 갱신해야 하는 경우
        #for j in range(len(ascend_stack)):
            #if stack[ascend_stack[j]] < stack[ascend_stack[j] + 1]:

        point = ascend_stack[0]
        stack.remove(stack[point])
        ascend_stack.remove(point)
        stack = [new_candidate] + stack
        front_value = new_candidate

        if stack[point] < stack[point + 1]:
            ascend_stack = [point] + ascend_stack

for i in range(n-k):
    print(stack[i], end = "")