# by the authority of GOD     author: manhar singh sachdev #

import os,sys
from io import BytesIO, IOBase

# TIME
# n = q = 10^5 : 1600ms

block = 350
class Query:
    def __init__(self,l,r,idx):
        self.l = l
        self.r = r
        self.idx = idx

    def __lt__(self, other):
        z,z1 = self.l//block,other.l//block
        if z == z1:
            if z&1:
                return self.r > other.r
            return self.r < other.r
        return z < z1

    def __str__(self):
        return "l = {}\nr = {}\nidx = {}\n".format(self.l,self.r,self.idx)

def main():
    # change const int block to sqrt(n)
    # check struct query once as well
    # prefer C++
    # struct query slow ; multiple lists fast
    n,m,K = map(int,input().split())
    arr = [0]+list(map(int,input().split()))
    for i in range(1,n+1):
        arr[i] ^= arr[i-1]
    queries = []
    for i in range(m):
        l,r = map(int,input().split())
        queries.append(Query(l,r,i))

    queries.sort()
    freq = [0]*1048576
    answer = [0]*m
    l,r,su = 1,-1,0
    for q in queries:
        while l > q.l:
            l -= 1
            su += freq[arr[l-1]^K]
            freq[arr[l-1]] += 1
        while r < q.r:
            r += 1
            su += freq[arr[r]^K]
            freq[arr[r]] += 1
        while l < q.l:
            su -= freq[arr[l-1]^K]
            if not K:
                su += 1
            freq[arr[l-1]] -= 1
            l += 1
        while r > q.r:
            su -= freq[arr[r]^K]
            if not K:
                su += 1
            freq[arr[r]] -= 1
            r -= 1
        answer[q.idx] = su
    print(*answer,sep='\n')

# Fast IO Region
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
if __name__ == "__main__":
    main()