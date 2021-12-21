# by the authority of GOD     author: manhar singh sachdev #

import os,sys
from io import BytesIO, IOBase

def find(parent,x):
    if x == parent[x]:
        return x
    parent[x] = find(parent,parent[x])
    return parent[x]

def union(parent,a,b,rank):
    a,b = find(parent,a),find(parent,b)
    if a != b:
        if rank[a] < rank[b]:
            a,b = b,a
        parent[b] = a
        if rank[a] == rank[b]:
            rank[a] += 1
        return 1
    return 0

def main():
    n,m = map(int,input().split())
    edg = [tuple(map(int,input().split())) for _ in range(m)]
    edg.sort(key=lambda xx:xx[2])
    parent = [i for i in range(n)]
    rank = [0]*n
    ans,cou = 0,0
    for i in edg:
        a,b,c = i
        if union(parent,a-1,b-1,rank):
            ans += c
            cou += 1
        if cou == n-1:
            break
    if cou != n-1:
        print('IMPOSSIBLE')
    else:
        print(ans)

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