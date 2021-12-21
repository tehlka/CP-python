# by the authority of GOD     author: manhar singh sachdev #

import os,sys
from io import BytesIO,IOBase

def matching(n,m,path):
    # https://github.com/cheran-senthil/PyRival/blob/master/pyrival/graphs/hopcroft_karp.py
    # Hopkrocft Karp O(EV^0.5)
    match1 = [-1]*n
    match2 = [-1]*m
    for node in range(n):
        for nei in path[node]:
            if match2[nei] == -1:
                match1[node] = nei
                match2[nei] = node
                break
    while 1:
        bfs = [node for node in range(n) if match1[node] == -1]
        depth = [-1]*n
        for node in bfs:
            depth[node] = 0

        for node in bfs:
            for nei in path[node]:
                next_node = match2[nei]
                if next_node == -1:
                    break
                if depth[next_node] == -1:
                    depth[next_node] = depth[node]+1
                    bfs.append(next_node)
            else:
                continue
            break
        else:
            break
        pointer = [len(c) for c in path]
        dfs = [node for node in range(n) if depth[node] == 0]
        while dfs:
            node = dfs[-1]
            while pointer[node]:
                pointer[node] -= 1
                nei = path[node][pointer[node]]
                next_node = match2[nei]
                if next_node == -1:
                    while nei != -1:
                        node = dfs.pop()
                        match2[nei],match1[node],nei = node,nei,match1[node]
                    break
                elif depth[node]+1 == depth[next_node]:
                    dfs.append(next_node)
                    break
            else:
                dfs.pop()
    return match1,match2

def main():
    n,m,k = map(int,input().split())
    path = [[] for _ in range(n)]
    for _ in range(k):
        a,b = map(lambda xx:int(xx)-1,input().split())
        path[a].append(b)
    match1,match2 = matching(n,m,path)
    print(len(match1)-match1.count(-1))
    for ind,i in enumerate(match1):
        if i == -1:
            continue
        print(ind+1,i+1)

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