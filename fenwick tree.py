# by the authority of GOD     author: manhar singh sachdev #

import os,sys
from io import BytesIO, IOBase

# BIT always 1 based
# store a copy of original array, will require it in update
# pass n+1 length array

new = lambda xx: (xx|xx-1)+1
def buildBIT(bit,n):
    for i in range(1,n+1):
        x = new(i)
        if x <= n:
            bit[x] += bit[i]

def pointUpdate(bit,point,n,diff):
    while point <= n:
        bit[point] += diff
        point = new(point)

def calculatePrefix(bit,point):
    su = 0
    while point:
        su += bit[point]
        point &= point-1
    return su

def rangeQuery(bit,start,stop):
    # [start,stop]
    return calculatePrefix(bit,stop)-calculatePrefix(bit,start-1)

def findkth(bit,k,n):
    # returns the first index where prefix sum equals/exceeds k
    idx,ans = 0,0
    for d in reversed(range(n.bit_length())):
        right = idx+(1<<d)
        if right <= n:
            if k > bit[right]:
                idx = right
                k -= bit[right]
            else:
                ans = right
    return ans

def main():
    n,Q = map(int,input().split())
    x = [0]+list(map(int,input().split()))
    bit = x[:]
    buildBIT(bit,n)
    for _ in range(Q):
        op = list(map(int,input().split()))
        if op[0] == 1:
            pointUpdate(bit,op[1],n,op[2]-x[op[1]])
            x[op[1]] = op[2]
        else:
            print(rangeQuery(bit,op[1],op[2]))

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