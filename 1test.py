from random import *

n = 10
print(n,flush=1)
# arr = list(range(1,n+1))
# shuffle(arr)
arr = list(range(1,11))

while 1:
    ls = input().split()
    if ls[0] == '?':
        xx = list(map(int,ls[1:]))
        if len(xx) != n:
            exit(f" length problem {ls} {n}")
        dct = {}
        for i in range(n):
            x = arr[i]+xx[i]
            if dct.get(x):
                print(dct[x],flush=1)
                break
            dct[x] = i+1
        else:
            print(0,flush=1)
    else:
        if arr == list(map(int,ls[1:])):
            exit("OP")
        else:
            exit(f"maa chuda {arr}")