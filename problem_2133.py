import sys

n=int(sys.stdin.readline())

dynamic_list=[]
dynamic_list.append(0) #총 길이가 1인 경우
dynamic_list.append(3) #총 길이가 2인 경우
dynamic_list.append(0) #총 길이가 3인 경우
dynamic_list.append(11) #총 길이가 4인 경우

if n>=5:
    while len(dynamic_list) != n:
        i=2
        new_value = 3 * dynamic_list[-2] 
        while True:
            try:
                new_value += 2 * dynamic_list[-2*i]
                i+=1
            except IndexError:
                if len(dynamic_list) % 2 == 1:
                    new_value+=2
                break
        dynamic_list.append(new_value)
    print(dynamic_list[-1])

else:
    print(dynamic_list[n-1])
