import sys

n, k = map(int, sys.stdin.readline().split())

info_list = [[1, 2 ,1]]

if k > n//2:
    k = n - k # nCk 은 nCn-k와 동일하므로

def find_new_combination(prev_row, r): #r은 현재 조합에서 뒤의 수
    result_num = 0

    if r % 2 == 1: #r이 홀수인 경우
        for i in range(int((r+1) / 2)):
            result_num += 2 * prev_row[i] * prev_row[r - i]
    
    else: #r이 짝수인 경우
        for i in range(int(r / 2)):
            result_num += 2 * prev_row[i] * prev_row[r - i]
        result_num += prev_row[int(r / 2)] ** 2


    return result_num % 1000000007

flag = 0

while 2 ** (len(info_list) + 1) < n:
    length = 2 * len(info_list[-1]) - 1 #이번에 추가할 것의 길이 #An = 2 * An-1 + 1
    new_info = []

    if int((length + 1)/2) > k:
        flag = 1

    if  flag == 0: #아직 길이가 k를 넘지 않는 경우
        for i in range(int((length + 1)/2)):
            new_info.append(find_new_combination(info_list[-1], i))

        new_info.extend(new_info[:-1][::-1])
        info_list.append(new_info)

    else: #length가 k를 넘은 경우
        for i in range(k):
            new_info.append(find_new_combination(info_list[-1], i))
        info_list.append(new_info)



for i in range(len(info_list)):
    print(info_list[i])