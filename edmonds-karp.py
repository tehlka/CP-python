# by the authority of GOD     author: manhar singh sachdev #

import os,sys
from io import BytesIO,IOBase
from collections import deque

def maxflow(n,path,cap):
    # edmonds-karp algorithm O(VE^2)
    tot,inc = 0,1
    while inc:
        curr,par,mini,inc = deque([0]),[-2]+[-1]*(n-1),[10**20]*n,0
        while len(curr):
            x = curr.popleft()
            if x == n-1:
                inc = mini[x]
                while par[x] != -2:
                    cap[par[x]][x] -= inc
                    cap[x][par[x]] += inc
                    x = par[x]
                break
            for y in path[x]:
                if cap[x][y] and par[y] == -1:
                    par[y] = x
                    mini[y] = min(mini[x],cap[x][y])
                    curr.append(y)
        tot += inc
    return tot

def main():
    n,m = map(int,input().split())
    path = [[] for _ in range(n)]
    cap = [[0]*n for _ in range(n)]
    for _ in range(m):
        a,b,c = map(int,input().split())
        path[a-1].append(b-1)
        path[b-1].append(a-1)
        cap[(a-1,b-1)] += c
        # to account for multiple edges
    print(maxflow(n,path,cap))

# Fast IO Region
BUFSIZE = 8192
class FastIO(IOBase):
    newlines = 0
    def __init__(self,file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None
    def read(self):
        while True:
            b = os.read(self._fd,max(os.fstat(self._fd).st_size,BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0,2),self.buffer.write(b),self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()
    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd,max(os.fstat(self._fd).st_size,BUFSIZE))
            self.newlines = b.count(b"\n")+(not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0,2),self.buffer.write(b),self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()
    def flush(self):
        if self.writable:
            os.write(self._fd,self.buffer.getvalue())
            self.buffer.truncate(0),self.buffer.seek(0)
class IOWrapper(IOBase):
    def __init__(self,file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s:self.buffer.write(s.encode("ascii"))
        self.read = lambda:self.buffer.read().decode("ascii")
        self.readline = lambda:self.buffer.readline().decode("ascii")
sys.stdin,sys.stdout = IOWrapper(sys.stdin),IOWrapper(sys.stdout)
input = lambda:sys.stdin.readline().rstrip("\r\n")
if __name__ == "__main__":
    main()