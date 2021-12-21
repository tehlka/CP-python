# by the authority of GOD     author: manhar singh sachdev #

import os,sys
from io import BytesIO, IOBase

def main():
    # 0 based
    inf = 10**20
    n,m = map(int,input().split())
    edg = []
    for _ in range(m):
        a1,b1,c1 = map(int,input().split())
        edg.append((a1-1,b1-1,c1))
    dis = [0]+[inf]*(n-1)
    pre = [-1]*n
    for i in range(n):
        x = -1
        for j in edg:
            a,b,w = j
            """dis[a] != inf added to not compute for 
            areas that can never be reached
            Remove if want to find negative cycle in whole graph"""
            if dis[a] != inf and dis[b] > dis[a]+w:
                dis[b] = dis[a]+w
                x,pre[b] = b,a
    if x == -1:
        # no cycle
        print(dis[n-1])
    else:
        # there is negative cycle
        for _ in range(n):
            x = pre[x]
        path = [x]
        curr = pre[x]
        while curr != x:
            path.append(curr)
            curr = pre[curr]
        path.append(x)
        path.reverse()
        print(*path)

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