import sys

n = int(sys.stdin.readline())

def plus_two_list(list1, list2):
    plus_list = []
    for i in range(10):
        plus_list.append(list1[i] + list2[i])

    return plus_list

def minus_two_list(list1, list2):
    minus_two_list = []
    for i in range(10):
        minus_two_list.append(list1[i] - list2[i])

    return minus_two_list

num_count = [0] * 10

def recursive(x : int, allow_first_zero : bool):
    global num_count

    left_num = int(str(x)[0])
    length = len(str(x))

    if length == 1:
        if allow_first_zero == True:
            for i in range(left_num + 1):
                num_count[i] += 1
        else:
            for i in range(1, left_num + 1):
                num_count[i] += 1
    
    else:

        if allow_first_zero == True: #재귀함수로 내부에서 호출이 된 경우
            num_count[0] += 10 ** (length - 1)
            recursive(int("9" * (length - 1)), True)

        else:
            recursive(int("9" * (length - 1)), False) #제일 왼쪽수가 0인 경우(자릿수를 하나 줄이는 경우)
    
        for i in range(1, left_num): #완전히 순환되는 경우 ex) 000 ~ 999
            num_count[i] += 10 ** (length - 1)
        if left_num >= 2:
            before = num_count.copy()
            recursive(int("9" * (length - 1)), True) #소요시간 개선의 여지가 있음
            after = num_count.copy()
            delta = minus_two_list(after, before)
            num_count = plus_two_list(num_count, [(left_num - 2) * x for x in delta])


        num_count[left_num] += int(str(x)[1:]) + 1
        i = 1
        while i < length - 1 and str(int(str(x)[i])) == "0": #left_num바로 다음 수가 0이여서 0이 생략된 경우
            num_count[0] += int(str(x)[i:]) + 1
            i += 1
        recursive(int(str(x)[1:]), True) #제일 왼쪽수가 원본과 동일한 경우, 문제 point

recursive(n, False)

for i in range(10):
    print(num_count[i], end = " ")