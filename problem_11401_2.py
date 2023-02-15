import math
import sys

n, k = map(int, sys.stdin.readline().split())

factorial_list = [1]
i = 1

brand_new = factorial_list[-1]
p = 1000000007

while i != n:
    i += 1
    new_thing = ((brand_new % p) * (i % p)) % p
    factorial_list.append(new_thing)
    brand_new = new_thing

under = factorial_list[k - 1] * factorial_list[n - k -1]
i = 1
under_square_list = [under]
while i < p - 2:
    new_under = (under_square_list[-1] ** 2) % p
    under_square_list.append(new_under)
    i *= 2

now = p - 2
now_value = 1

while now > 0:
    log2_value = int(math.log2(now))
    now -= 2 ** log2_value
    now_value *= under_square_list[log2_value]

total = ((factorial_list[-1] % p) * (now_value % p) % p)

if  k == 0:
    print(1)
else:
    print(total)