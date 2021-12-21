# by the authority of GOD     author: manhar singh sachdev #

import os,sys
from io import BytesIO, IOBase
import __pypy__

int_add = __pypy__.intop.int_add
int_sub = __pypy__.intop.int_sub
int_mul = __pypy__.intop.int_mul
mod = 1000000007

def make_mod_mul():
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

fac = [1]
for ii in range(1,10**6+1):
    fac.append(mod_mul(fac[-1],ii))
facInv = [pow(fac[-1],mod-2,mod)]
for ii in range(10**6,0,-1):
    facInv.append(mod_mul(facInv[-1],ii))
facInv.reverse()

def comb(a,b):
    if a < b:
        return 0
    return mod_mul(mod_mul(fac[a],facInv[a-b]),facInv[b])

# fac = [1]
# for ii in range(1,10**6+1):
#     fac.append((fac[-1]*ii)%mod)
# facInv = [pow(fac[-1],mod-2,mod)]
# for ii in range(10**6,0,-1):
#     facInv.append((facInv[-1]*ii)%mod)
# facInv.reverse()
#
# def comb(a,b):
#     if a < b:
#         return 0
#     return (fac[a]*facInv[a-b]*facInv[b])%mod

# combination using dp
# comb = [[0]*(n+1) for _ in range(n+1)]
# comb[0][0] = 1
# for i in range(1,n+1):
#     for j in range(i+1):
#         comb[i][j] = (comb[i-1][j]+comb[i-1][j-1])%mod

def main():
    for _ in range(int(input())):
        a,b = map(int,input().split())
        print(comb(a,b))

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