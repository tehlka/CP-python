# by the authority of GOD     author: manhar singh sachdev #

import os,sys
from io import BytesIO, IOBase

def kosaraju(n,path,pathr):
    topsort,visi,poi = [],[0]*n,[0]*n
    for i in range(n):
        if visi[i]:
            continue
        st,st1,visi[i] = [i],[],1
        while len(st):
            x,y = st[-1],path[st[-1]]
            while poi[x] != len(y) and visi[y[poi[x]]]:
                poi[x] += 1
            if poi[x] == len(y):
                st1.append(st.pop())
            else:
                i = y[poi[x]]
                poi[x] += 1
                st.append(i)
                visi[i] = 1
        topsort.extend(st1)
    topsort.reverse()
    comp,poi,num = [0]*n,[0]*n,0
    for i in topsort:
        if comp[i]:
            continue
        num += 1
        st,comp[i] = [i],num
        while len(st):
            x,y = st[-1],pathr[st[-1]]
            while poi[x] != len(y) and comp[y[poi[x]]]:
                poi[x] += 1
            if poi[x] == len(y):
                st.pop()
            else:
                i = y[poi[x]]
                poi[x] += 1
                st.append(i)
                comp[i] = num
    return comp

def main():
    pass

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