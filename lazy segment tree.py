# by the authority of GOD   author: manhar singh sachdev #

import os,sys
from io import BytesIO,IOBase

# TIME
# 2*10^6 addition update min query 1700ms

# addition update, minimum query
# https://codeforces.com/edu/course/2/lesson/5/2/practice/contest/279653/submission/117071214
# addition query, multiplication update
# https://codeforces.com/edu/course/2/lesson/5/2/practice/contest/279653/submission/117086524
# addition query, addition update (used float because values > 32bit int)
# https://codeforces.com/edu/course/2/lesson/5/2/practice/contest/279653/submission/117291191
# and query, or update
# https://codeforces.com/edu/course/2/lesson/5/2/practice/contest/279653/submission/117288634
# sum query, assignment update
# https://codeforces.com/edu/course/2/lesson/5/2/practice/contest/279653/submission/117306434
# min query, assignment update
# https://codeforces.com/edu/course/2/lesson/5/2/practice/contest/279653/submission/117306688
# best subarray query, assignment update (prefer C++)
# https://codeforces.com/edu/course/2/lesson/5/3/practice/contest/280799/submission/117856288
# C++ link
# inverse the segment and find kth one
# https://codeforces.com/edu/course/2/lesson/5/3/practice/contest/280799/submission/117862811
# addition on segment and minimum index greater than i and value greater than x
# https://codeforces.com/edu/course/2/lesson/5/3/practice/contest/280799/submission/117870637

# h = n.bit_length()-(not n&n-1)
# si = 1<<h
# tree = [0]*(si<<1)
# lazy = [0]*si
def build(tree,lazy,pos):
    pos >>= 1
    while pos:
        tree[pos] = min(tree[pos<<1],tree[pos<<1|1])+lazy[pos]
        pos >>= 1

def apply(tree,lazy,pos,val):
    tree[pos] += val
    if pos < len(lazy):
        lazy[pos] += val

def push(tree,lazy,pos,h):
    for s in range(h,0,-1):
        ne = pos>>s
        if lazy[ne]:
            apply(tree,lazy,ne<<1,lazy[ne])
            apply(tree,lazy,ne<<1|1,lazy[ne])
            lazy[ne] = 0

def update(tree,lazy,l,r,val,si):
    l,r = l+si-1,r+si-1
    l0,r0 = l,r
    # push updates for operations in which order matters
    while l < r:
        if l&1:
            apply(tree,lazy,l,val)
            l += 1
        if not r&1:
            apply(tree,lazy,r,val)
            r -= 1
        l,r = l>>1,r>>1
    if l == r:
        apply(tree,lazy,l,val)
    build(tree,lazy,l0)
    build(tree,lazy,r0)

def query(tree,lazy,l,r,si,h):
    l,r,ans = l+si-1,r+si-1,float("inf")
    push(tree,lazy,l,h)
    push(tree,lazy,r,h)
    while l < r:
        if l&1:
            ans = min(ans,tree[l])
            l += 1
        if not r&1:
            ans = min(ans,tree[r])
            r -= 1
        l,r = l>>1,r>>1
    if l == r:
        return min(ans,tree[l])
    return ans

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