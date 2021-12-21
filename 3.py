# by the authority of GOD     author: manhar singh sachdev #

import os,sys
from io import BytesIO,IOBase
import __pypy__
from types import GeneratorType

def bootstrap(f,stack=[]):
    def wrappedfunc(*args,**kwargs):
        if stack:
            return f(*args,**kwargs)
        else:
            to = f(*args,**kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc

int_add = __pypy__.intop.int_add
int_sub = __pypy__.intop.int_sub
int_mul = __pypy__.intop.int_mul

def make_mod_mul(mod=10**9+7):
    fmod_inv = 1.0 / mod
    def mod_mul(a, b, c=0):
        res = int_sub(int_add(int_mul(a, b), c), int_mul(mod,int(fmod_inv * a * b + fmod_inv * c)))
        if res >= mod:
            return res - mod
        elif res < 0:
            return res + mod
        else:
            return res
    return mod_mul

mod_mul = make_mod_mul()

def mod_pow(x,y):
    if y == 0:
        return 1
    res = 1
    while y > 1:
        if y & 1 == 1:
            res = mod_mul(res, x)
        x = mod_mul(x, x)
        y >>= 1
    return mod_mul(res, x)

least_bit = lambda xx: xx & -xx
# Consider pigeonhole
# Consider randomization
# 2D list [[0]*large_index for _ in range(small_index)]
# switch from integers to floats if all integers are ≤ 2^52 and > 32 bit int
# FLOAT : 52 bits
# if numbers bigger than float limit, consdier using Cpython or C++
# for math problems, consider binary search and lpp
# for range query, consider mo's algo and seg tree
# for constructive, consider m-coloring / odd-even
# AVOID calculation in floats
# while dealing with floats, set error
# float calculation: https://codeforces.com/contest/1543/submission/121714077
# for interactive, change IO https://codeforces.com/contest/1543/submission/121781191
# from array import array

def main():
    for _ in range(int(input())):
        pass

#Fast IO Region
BUFSIZE = 8192
class FastIO(IOBase):
    newlines = 0
    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None
    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()
    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()
    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)
class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")
sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")
if __name__ == '__main__':
    main()