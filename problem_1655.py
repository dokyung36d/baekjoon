from queue import PriorityQueue
import sys

n=int(sys.stdin.readline())
info_list=[]

for _ in range(n):
    info_list.append(int(sys.stdin.readline()))

min_heap=PriorityQueue() #default는 min_heap임
max_heap=PriorityQueue() #삽입할 때는 -를 붙여 해결

#작은 것들은 max_heap에, 큰 것들은 min_heap에 삽입
max_heap.put(-min(info_list[0], info_list[1]))
min_heap.put(max(info_list[0], info_list[1]))

print(info_list[0])
print(min(info_list[0], info_list[1]))

for i in range(2, n):

    max_heap_max_value=-max_heap.queue[0] #1
    min_heap_min_value=min_heap.queue[0]  #5

    if info_list[i] <= max_heap_max_value:
        max_heap.put( - info_list[i])

    elif info_list[i] > min_heap_min_value:
        min_heap.put(info_list[i])

    else: #사잇값인 경우
        max_heap.put(-info_list[i])

    max_heap_size=max_heap.qsize()
    min_heap_size=min_heap.qsize()
    
    if max_heap_size > min_heap_size + 1:
        change_value= - max_heap.get()
        min_heap.put(change_value)

    elif min_heap_size > max_heap_size + 1:
        change_value = min_heap.get()
        max_heap.put(-change_value)


    if max_heap_size +1 == min_heap_size:
        print_value=min_heap.queue[0]
        print(print_value)

    else:
        print_value = -max_heap.queue[0]
        print(print_value)


