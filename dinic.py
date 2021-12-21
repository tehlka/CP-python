# by the authority of GOD     author: manhar singh sachdev #

import os,sys
from io import BytesIO,IOBase
from collections import deque

def bfs(n,path,cap):
    curr = deque([0])
    level = [0]+[-1]*(n-1)
    while len(curr):
        x = curr.popleft()
        for i in path[x]:
            if cap[x][i] and level[i] == -1:
                level[i] = level[x]+1
                curr.append(i)
    return level

def dinic(n,path,cap):
    # 0 source ; n-1 sink
    flow = 0
    while True:
        level = bfs(n,path,cap)
        if level[n-1] == -1:
            return flow
        isdead,inc = [0]*n,1
        while inc:
            st,poi,visi,mini,inc = [0],[0]*n,[1]+[0]*(n-1),[10**20]+[0]*(n-1),0
            while len(st):
                x,y = st[-1],path[st[-1]]
                while poi[x] != len(y) and (visi[y[poi[x]]] or isdead[y[poi[x]]]
                      or (not cap[x][y[poi[x]]]) or level[y[poi[x]]] <= level[x]):
                    poi[x] += 1
                if poi[x] == len(y):
                    isdead[st.pop()] = 1
                else:
                    i,j = y[poi[x]],cap[x][y[poi[x]]]
                    st.append(i)
                    mini[i] = min(mini[x],j)
                    visi[i] = 1
                    poi[x] += 1
                    if i == n-1:
                        inc = mini[i]
                        flow += inc
                        for x in range(len(st)-2,-1,-1):
                            w,z = st[x],st[x+1]
                            cap[w][z] -= inc
                            cap[z][w] += inc
                        break

def main():
    n, m = map(int, input().split())
    path = [[] for _ in range(n)]
    cap = [[0]*n for _ in range(n)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        path[a-1].append(b-1)
        path[b-1].append(a-1)
        cap[(a-1,b-1)] += c
        # to account for multiple edges
    print(dinic(n,path,cap))

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