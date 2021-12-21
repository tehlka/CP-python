# by the authority of GOD     author: manhar singh sachdev #

import os,sys
from io import BytesIO, IOBase
# frequency of minimum
# https://codeforces.com/edu/course/2/lesson/4/1/practice/contest/273169/submission/116487771
# segment with maximum sum (prefer C++)
# https://codeforces.com/edu/course/2/lesson/4/2/practice/contest/273278/submission/116492358
# https://codeforces.com/edu/course/2/lesson/4/2/practice/contest/273278/submission/116544663
# kth one in a segment tree
# https://codeforces.com/edu/course/2/lesson/4/2/practice/contest/273278/submission/116531715
# minimum index with element greater than X
# https://codeforces.com/edu/course/2/lesson/4/2/practice/contest/273278/submission/116532179
# minimum index greater than l and element greater than X
# https://codeforces.com/edu/course/2/lesson/4/2/practice/contest/273278/submission/116535836
# inversions for each element
# https://codeforces.com/edu/course/2/lesson/4/3/practice/contest/274545/submission/116541833
# find out array from inversion array
# https://codeforces.com/edu/course/2/lesson/4/3/practice/contest/274545/submission/116543168
# number of segments nested inside each segment
# https://codeforces.com/edu/course/2/lesson/4/3/practice/contest/274545/submission/116557940
# number of segments intersecting with each segment
# https://codeforces.com/edu/course/2/lesson/4/3/practice/contest/274545/submission/116559223
# range sum update using normal segment tree
# https://codeforces.com/edu/course/2/lesson/4/3/practice/contest/274545/submission/116560399
# range sum with alternating signs
# https://codeforces.com/edu/course/2/lesson/4/4/practice/contest/274684/submission/116574849
# number of different values on a segment (a[i]<=40)
# https://codeforces.com/edu/course/2/lesson/4/4/practice/contest/274684/submission/116705531
# https://codeforces.com/edu/course/2/lesson/4/4/practice/contest/274684/submission/116617325
# product of range of 2x2 matrices (prefer C++)
# https://codeforces.com/edu/course/2/lesson/4/4/practice/contest/274684/submission/116630305
# https://codeforces.com/edu/course/2/lesson/4/4/practice/contest/274684/submission/116644126
# number of inversions in a range (a[i]<=40) (prefer C++)
# https://codeforces.com/edu/course/2/lesson/4/4/practice/contest/274684/submission/116716056
# number of values less than x in a range
# https://codeforces.com/edu/course/2/lesson/4/4/practice/contest/274684/submission/116720998
# max prefix sum in range l to r
# https://cses.fi/problemset/result/2215279/
# swaps to make two strings equal (code written for 4 characters but will work anyway)
# https://codeforces.com/contest/1526/submission/117666107
# mode in a segment with frequency (C++)
# https://codeforces.com/contest/1514/submission/119636715
# longest correct bracketed subsequence (no update)
# https://codeforces.com/contest/380/submission/120344465
# coordinate compression
# https://cses.fi/problemset/result/2424047/
# distinct values in a range (can also be done using mo's algo)
# https://cses.fi/problemset/result/2424371/

# 1 based normal segment tree
# pass all parameters 1 based
# si = 1<<n.bit_length()-(not n&n-1)
def construct(n,x,si):
    tree = [0]*(si<<1)
    for i in range(si,si+n):
        tree[i] = x[i-si]
    a,b = si>>1,si
    while a:
        for i in range(a,b):
            tree[i] = tree[i<<1]+tree[i<<1|1]
        a,b = a>>1,b>>1
    return tree

def update(tree,pos,value,si):
    pos += si-1
    diff = value-tree[pos]
    while pos:
        tree[pos] += diff
        pos >>= 1

def query(tree,l,r,si):
    # l and r inclusive
    ans,l,r = 0,l+si-1,r+si-1
    while l < r:
        if l&1:
            ans += tree[l]
            l += 1
        if not r&1:
            ans += tree[r]
            r -= 1
        l,r = l>>1,r>>1
    return ans+(0 if l != r else tree[l])

def combine(a,b):
    # some non commutative combine function
    return a+b

def query2(tree,l,r,si):
    # use query1 or query2 when combine function not commutative
    ans,ans1,l,r = 0,0,l+si-1,r+si-1
    while l < r:
        if l&1:
            ans = combine(ans,tree[l])
            l += 1
        if not r&1:
            ans1 += combine(tree[r],ans1)
            r -= 1
        l,r = l>>1,r>>1
    if l == r:
        ans = combine(ans,tree[l])
    return combine(ans,ans1)

def query1(tree,pos,tl,tr,l,r):
    # tl = 1 ; tr = si
    if l <= tl <= tr <= r:
        return tree[pos]
    if tl > r or tr < l:
        return 0
    tm = (tl+tr)//2
    return query1(tree,pos*2,tl,tm,l,r)+query1(tree,pos*2+1,tm+1,tr,l,r)

def main():
    pass

#Fast IO Region
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
if __name__ == '__main__':
    main()