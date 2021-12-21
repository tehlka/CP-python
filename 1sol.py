## IO starts (Thanks pajenegod)
import sys
from sys import stdout
import os

ii = 0
_inp = b""

def getchar():
    global ii,_inp
    if ii >= len(_inp):
        _inp = os.read(0,4096)
        ii = 0
    if not _inp:
        return b" "[0]
    ii += 1
    return _inp[ii-1]

def input():
    c = getchar()
    if c == b"-"[0]:
        x = 0
        sign = 1
    else:
        x = c-b"0"[0]
        sign = 0
    c = getchar()
    while c >= b"0"[0]:
        x = 10*x+c-b"0"[0]
        c = getchar()
    if c == b"\r"[0]:
        getchar()
    return -x if sign else x

## IO ends
# reference https://codeforces.com/contest/1543/submission/121781191

def main():
    for _ in range(int(input())):
        print('?',10**18+1,flush=1)
        print('?',10**18-int(input()),flush=1)
        print('!',int(input())+1,flush=1)

if __name__ == "__main__":
    main()