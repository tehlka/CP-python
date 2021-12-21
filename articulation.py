# by the authority of GOD     author: manhar singh sachdev #

import os,sys
from io import BytesIO, IOBase

def articulation(n,path):
    ans,poi,st,visi = [0]*n,[0]*n,[0],[1]+[0]*(n-1)
    low,start,time,par = [0]*n,[0]*n,0,[-1]*n
    while len(st):
        x,y = st[-1],path[st[-1]]
        if poi[x] != len(y) and y[poi[x]] == par[x]:
            poi[x] += 1
            continue
        while poi[x] != len(y) and visi[y[poi[x]]]:
            low[x] = min(low[x],start[y[poi[x]]])
            poi[x] += 1
        if poi[x] == len(y):
            st.pop()
            if len(st):
                low[st[-1]] = min(low[st[-1]],low[x])
                if low[x] >= start[st[-1]] and st[-1]:
                    ans[st[-1]] = 1
        else:
            i = y[poi[x]]
            poi[x] += 1
            time += 1
            st.append(i)
            start[i],visi[i],par[i],low[i] = time,1,x,time
    if par.count(0) > 1:
        ans[0] = 1
    return ans

def main():
    n,m = map(int,input().split())
    path = [[] for _ in range(n)]
    for _ in range(m):
        u1,v1 = map(lambda xx:int(xx)-1,input().split())
        path[u1].append(v1)
        path[v1].append(u1)
    print(articulation(n,path).count(1))

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