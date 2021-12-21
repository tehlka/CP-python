# by the authority of GOD     author: manhar singh sachdev #

import os,sys
from io import BytesIO,IOBase

def eulerian_cycle(n,m,path,deg):
    # works for undirected simple graphs
    if deg.count(1):
        return ['IMPOSSIBLE']
    st,poi,visi = [0],[0]*n,[set() for _ in range(n)]
    ans = []
    while len(st):
        x,y = st[-1],path[st[-1]]
        while poi[x] != len(y) and y[poi[x]] in visi[x]:
            poi[x] += 1
        if poi[x] == len(y):
            ans.append(st.pop()+1)
        else:
            i = y[poi[x]]
            st.append(i)
            visi[i].add(x)
            visi[x].add(i)
            poi[x] += 1
    if len(ans) != m+1:
        return ['IMPOSSIBLE']
    return ans[::-1]

def eulerian_path(n,m,path,indeg,outdeg):
    # works for directed simple graphs
    c,start,end = 0,-1,-1
    for i in range(n):
        if indeg[i] == outdeg[i]+1 and end == -1:
            c += 1
            end = i
        elif outdeg[i] == indeg[i]+1 and start == -1:
            c += 1
            start = i
        elif outdeg[i] != indeg[i]:
            return['IMPOSSIBLE']
    if c != 2:
        return ['IMPOSSIBLE']
    st,poi = [start],[0]*n
    ans = []
    while len(st):
        x,y = st[-1],path[st[-1]]
        if poi[x] == len(y):
            ans.append(st.pop()+1)
        else:
            i = y[poi[x]]
            st.append(i)
            poi[x] += 1
    if len(ans) != m+1:
        return ['IMPOSSIBLE']
    return ans[::-1]

def main():
    n,m = map(int,input().split())
    path = [[] for _ in range(n)]
    deg = [0]*n
    for _ in range(m):
        a1,b1 = map(lambda xx:int(xx)-1,input().split())
        deg[a1] ^= 1
        deg[b1] ^= 1
        path[a1].append(b1)
        path[b1].append(a1)
    print(*eulerian_cycle(n,m,path,deg))

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