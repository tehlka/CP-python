# by the authority of GOD     author: manhar singh sachdev #

import os,sys
from io import BytesIO,IOBase

# binary lifting
def pre(n,path,lim):
    # lim = n.bit_length()
    up = [[-1]*(lim+1) for _ in range(n)]
    st,visi = [0],[1]+[0]*(n-1)
    start,finish,time = [0]*n,[0]*n,0
    while len(st):
        x = st[-1]
        y,j = up[x][0],0
        while y != -1:
            up[x][j] = y
            y = up[y][j]
            j += 1
        while len(path[x]) and visi[path[x][-1]]:
            path[x].pop()
        if not len(path[x]):
            time += 1
            finish[x] = time
            st.pop()
        else:
            i = path[x].pop()
            st.append(i)
            time += 1
            visi[i],start[i],up[i][0] = 1,time,x
    return start,finish,up

def is_ancestor(u,v,start,finish):
    # is u the ansector of v
    return start[u] <= start[v] and finish[u] >= finish[v]

def lca1(u,v,up,start,finish,lim):
    # lim = n.bit_lenght()
    if is_ancestor(u,v,start,finish):
        return u
    if is_ancestor(v,u,start,finish):
        return v
    for i in range(lim,-1,-1):
        if up[u][i] != -1 and not is_ancestor(up[u][i],v,start,finish):
            u = up[u][i]
    return up[u][0]

# euler path
def euler_path(n,path):
    height = [0]*n+[10**10]
    euler,st,visi,he,poi = [],[0],[1]+[0]*(n-1),0,[0]*n
    first = [-1]*n
    while len(st):
        x,y = st[-1],path[st[-1]]
        euler.append(x)
        if first[x] == -1:
            first[x] = len(euler)-1
        while poi[x] != len(y) and visi[y[poi[x]]]:
            poi[x] += 1
        if poi[x] == len(y):
            he -= 1
            st.pop()
        else:
            i = y[poi[x]]
            poi[x] += 1
            he += 1
            st.append(i)
            height[i],visi[i] = he,1
    return height,euler,first

def cons(euler,height):
    n = len(euler)
    xx = n.bit_length()
    dp = [[n]*n for _ in range(xx)]
    dp[0] = euler
    for i in range(1,xx):
        for j in range(n-(1<<i)+1):
            a,b = dp[i-1][j],dp[i-1][j+(1<<(i-1))]
            dp[i][j] = a if height[a] < height[b] else b
    return dp

def lca(l,r,dp,height,first):
    l,r = first[l],first[r]
    if l > r:
        l,r = r,l
    xx1 = (r-l+1).bit_length()-1
    a,b = dp[xx1][l],dp[xx1][r-(1<<xx1)+1]
    return a if height[a] < height[b] else b

def main():
    pass

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