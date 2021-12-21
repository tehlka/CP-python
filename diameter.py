# by the authority of GOD   author: manhar singh sachdev #

import os,sys
from io import BytesIO,IOBase

def main():
    n = int(input())
    path = [[] for _ in range(n)]
    for _ in range(n-1):
        a1,b1 = map(lambda xx:int(xx)-1,input().split())
        path[a1].append(b1)
        path[b1].append(a1)
    st,poi,visi,node,maxi,he = [0],[0]*n,[1]+[0]*(n-1),-1,-1,0
    while len(st):
        x,y = st[-1],path[st[-1]]
        if poi[x] != len(y) and visi[y[poi[x]]]:
            poi[x] += 1
        if poi[x] == len(y):
            st.pop()
            he -= 1
        else:
            he += 1
            i = y[poi[x]]
            if he > maxi:
                node,maxi = i,he
            st.append(i)
            poi[x] += 1
            visi[i] = 1
    st,poi,visi,node1,maxi,he = [node],[0]*n,[0]*n,-1,-1,0
    visi[node] = 1
    while len(st):
        x,y = st[-1],path[st[-1]]
        if poi[x] != len(y) and visi[y[poi[x]]]:
            poi[x] += 1
        if poi[x] == len(y):
            st.pop()
            he -= 1
        else:
            he += 1
            i = y[poi[x]]
            if he > maxi:
                node1,maxi = i,he
            st.append(i)
            poi[x] += 1
            visi[i] = 1
    st,poi,visi = [node],[0]*n,[0]*n
    visi[node] = 1
    while len(st):
        x,y = st[-1],path[st[-1]]
        if poi[x] != len(y) and visi[y[poi[x]]]:
            poi[x] += 1
        if poi[x] == len(y):
            st.pop()
        else:
            i = y[poi[x]]
            st.append(i)
            if i == node1:
                dia = st[:]
                break
            poi[x] += 1
            visi[i] = 1
    print(node,node1,dia)

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