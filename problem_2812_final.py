import sys

n, k = map(int, sys.stdin.readline().split())
stack_length = n-k
info = list(sys.stdin.readline())

stack = []

for i in range(n):
    while k > 0 and stack:
        if stack[-1] < info[i]:
            stack.pop()
            k -= 1

        else:
            break

    stack.append(info[i])

if k != 0:
    stack = stack[:stack_length]

for i in range(len(stack)):
    print(int(stack[i]), end = "")