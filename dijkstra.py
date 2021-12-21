# by the authority of GOD     author: manhar singh sachdev #

import os,sys
from io import BytesIO, IOBase
from heapq import *

def short(n,path,cost,st,en):
    # 0 based everything
    dist = [float("inf")]*n
    prev = [-1]*n
    dist[st] = 0
    he = [(0,st)]
    while len(he):
        y,x = heappop(he)
        if dist[x] < y:
            continue
        if x == en:
            break
        for i,j in zip(path[x],cost[x]):
            if dist[i] > dist[x]+j:
                dist[i] = dist[x]+j
                heappush(he,(dist[i],i))
                prev[i] = x
    return dist,prev

def main():
    n,m = map(int,input().split())
    path = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for _ in range(m):
        a,b,w = map(int,input().split())
        path[a-1].append(b-1)
        path[b-1].append(a-1)
        cost[a-1].append(w)
        cost[b-1].append(w)
    dist,prev = short(n,path,cost,0,n-1)
    ans = []
    ind = n-1
    while ind != -1:
        ans.append(ind+1)
        ind = prev[ind]
    ans.reverse()
    if ans[0] == 1:
        print(*ans)
    else:
        print(-1)

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