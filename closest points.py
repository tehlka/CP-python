# by the authority of GOD     author: manhar singh sachdev #

import os,sys
from io import BytesIO, IOBase
from math import sqrt
INF = float("inf")

def dist(a,b):
    return sqrt((a[0]-b[0])*(a[0]-b[0])+
                (a[1]-b[1])*(a[1]-b[1]))

def fun(x,y,n):
    ans = [-1,-1]
    if n <= 3:
        mini = INF
        for i in range(n):
            for j in range(i+1,n):
                if dist(x[i],x[j]) < mini:
                    mini = dist(x[i],x[j])
                    ans = [x[i][2],x[j][2]]
        return mini,ans
    z = n//2
    mid = x[z]
    y1,y2 = [],[]
    dct = {}
    for i in range(n):
        if x[i][0] == mid[0]:
            if i < z:
                dct[x[i][1]] = 0
            else:
                dct[x[i][1]] = 1
    for i in range(n):
        if y[i][0] < mid[0]:
            y1.append(y[i])
        elif y[i][0] > mid[0]:
            y2.append(y[i])
        else:
            if dct[y[i][1]]:
                y2.append(y[i])
            else:
                y1.append(y[i])
    a,ans1 = fun(x[:z],y1,z)
    b,ans2 = fun(x[z:],y2,n-z)
    if a < b:
        ans,d = ans1,a
    else:
        ans,d = ans2,b
    strip = []
    for i in range(n):
        if abs(y[i][0]-mid[0]) < d:
            strip.append(y[i])
    for i in range(len(strip)):
        j = i+1
        while j < len(strip) and (strip[j][1]-strip[i][1]) < d:
            d1 = dist(strip[i],strip[j])
            if d1 < d:
                d = d1
                ans = [strip[i][2],strip[j][2]]
            j += 1
    return d,ans

def main():
    n = int(input())
    x = sorted([list(map(int,input().split()))+[i] for
                i in range(n)],key=lambda xx:xx[0])
    y = sorted(x,key=lambda xx:xx[1])
    d,ans = fun(x,y,n)
    print(min(ans[0],ans[1]),max(ans[0],ans[1]),'%.6f'%round(d,6))

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