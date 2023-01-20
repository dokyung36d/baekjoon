import sys

n=sys.stdin.readline()[:-1]
info_list=[]

bracket_pair_dict={}
bracket_stack=[]
for i in range(len(n)): #이 부분에서 미리 괄호 쌍을 미리 지정 -> 나중에 필요하면 가져다 쓰기
    info_list.append(n[i])

    if n[i] == "(": #문자열의 왼쪽부터 탐색 -> stack에는 항상 "(" 만이 남아 있음
        bracket_stack.append(i)
    
    elif n[i] == ")":
        bracket_pair = bracket_stack.pop(-1)
        bracket_pair_dict[i] = bracket_pair #[")"] : ["("] 의 형태로 되어 있음


def find_pair(x : list):
    func_stack = []
    func_dictionary = {}
    for i in range(len(x)):
        if x[i] == "(":
            func_stack.append(i)
        
        elif x[i] == ")":
            func_bracket_pair = func_stack.pop(-1)
            func_dictionary[func_bracket_pair] = i
    
    return func_dictionary


stack=[]
#일단 동일한 우선순위를 가지는 경우, 왼쪽에 있는 연산자를 우선적으로 처리한다. --> 왼쪽에 있는 연산자를 스택의 제일 아래로
#if 스택에 새로 들어오기로 한 것이 우선순위가 더 높다면 바로 나가고 동일하면 일단 들어간다.

priority_dict = {"*" : 1, "/" : 1, "+" : 2, "-" : 2} #괄호는 재귀함수로 처리

#()를 처리하기 위해서는 재귀함수를 활용? --> 최종적으로 ()는 하나의 operand로 취급하기
#괄호 쌍을 확인하는 방법으로는 스택을 활용

def stack_func(information: list):
    stack_list = []
    func_dict = {}
    dict_stack=[]


    for i in range(len(information)):
        if information[i] == "(":
            dict_stack.append(i)

        elif information[i] == ")":
            information_pair_bracket_pair = dict_stack.pop(-1)
            func_dict[information_pair_bracket_pair] = i # dict["("] = ")" 형태


        
    if information[0] == "(": #시작하자마자 (로 시작하는 경우
        if func_dict[0] == len(information) -1:
            return stack_func(information[1: -1])
        left_operand = stack_func(information[1:func_dict[0]])
        information = information[func_dict[0] + 1:]
    else:
        left_operand=information.pop(0)
    stack_list.append(left_operand)


    operator=information.pop(0)
    stack_list.append(operator)


    if information[0] == "(":
        func_dict = find_pair(information)
        right_operand = stack_func(information[1:func_dict[0]]) #오류 가능성 : 연산자 전후로 모두 괄호가 있을 경우 index가 일치 X
        information = information[func_dict[0] + 1:]
    else:
        right_operand=information.pop(0)
    stack_list.append(right_operand)

    while len(information) >= 2: #총 스택의 길이는 3이 되도록 유지 --> X:
        right_operator = information.pop(0)
        left_operator = stack_list[-2] #기존에 스택에 들어있던 것

        if information[0] == "(":
            func_dict = find_pair(information)
            new_right_operand = stack_func(information[1:func_dict[0]])
            information = information[func_dict[0] + 1:]
        
        else:
            new_right_operand = information.pop(0)

        # if new_left_operand == ")": #괄호가 시작되는 경우
        #     bracket_info = information.copy()
        #     bracket_stack = []
        #     for i in range(len(bracket_info) -1, -1, -1):
        #         if bracket_info[i] == ")":
        #             bracket_stack.append(")")
                
        #         elif bracket_info[i] == "(":
        #             if len(bracket_stack) == 0:
        #                 print("gi")
        #                 print(bracket_info[i+1:])
        #                 return stack_func(bracket_info[i+1:])
        #             elif bracket_stack[-1] == ")":
        #                 bracket_stack.pop(-1)

        if priority_dict[left_operator] <= priority_dict[right_operator]: #기존 스택에 들어있던 연산자의 우선순위가 동일하거나 같은 경우
            old_left_operand = stack_list.pop(0)
            old_operator = stack_list.pop(0)
            old_right_operand = stack_list.pop(0)

            new_operand = str(old_left_operand) + str(old_right_operand) + str(old_operator)
            stack_list.append(new_operand)
            stack_list.append(right_operator)
            stack_list.append(new_right_operand)

        elif priority_dict[left_operator] > priority_dict[right_operator]: #기존 스택에 있는 연산자의 우선순위가 더 높은 경우
            new_operand = str(stack_list[-1]) + str(new_right_operand) + str(right_operator)
            stack_list.pop(-1)
            stack_list.append(new_operand)

    stack_list = str(stack_list[0]) + str(stack_list[2])  + str(stack_list[1])
    return stack_list

print(stack_func(info_list))