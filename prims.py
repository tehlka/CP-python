# by the authority of GOD     author: manhar singh sachdev #

import os,sys
from io import BytesIO, IOBase
from heapq import *

# for dense graph, use different prims
# https://cp-algorithms.com/graph/mst_prim.html

def prims(n,path):
    # for sparse graph O(ElogV)
    visi = [1]+[0]*(n-1)
    ans,cou = 0,0
    he = [i for i in path[0]]
    while len(he):
        x,y = heappop(he)
        if visi[y]:
            continue
        visi[y] = 1
        ans += x
        cou += 1
        for i,j in path[y]:
            if not visi[j]:
                heappush(he,(i,j))
    if cou != n-1:
        return 'IMPOSSIBLE'
    return ans

def main():
    n,m = map(int,input().split())
    path = [[] for _ in range(n)]
    for _ in range(m):
        a1,b1,c1 = map(int,input().split())
        path[a1-1].append((c1,b1-1))
        path[b1-1].append((c1,a1-1))
    print(prims(n,path))

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