# by the authority of GOD   author: manhar singh sachdev #

import os,sys
from io import BytesIO,IOBase

def SAIS(A):
    """
    Calculates suffix array in O(len(A) + max(A))
    [ord(i) for i in input().strip()]
    """
    n = len(A)
    buckets = [0] * (max(A) + 2)
    for a in A:
        buckets[a + 1] += 1
    for b in range(1, len(buckets)):
        buckets[b] += buckets[b - 1]
    isL = [1] * n
    for i in reversed(range(n - 1)):
        isL[i] = +(A[i] > A[i + 1]) if A[i] != A[i + 1] else isL[i + 1]

    def induced_sort(LMS):
        SA = [-1]*n
        SA.append(n)
        endpoint = buckets[1:]
        for j in reversed(LMS):
            endpoint[A[j]] -= 1
            SA[endpoint[A[j]]] = j
        startpoint = buckets[:-1]
        for i in range(-1, n):
            j = SA[i] - 1
            if j >= 0 and isL[j]:
                SA[startpoint[A[j]]] = j
                startpoint[A[j]] += 1
        SA.pop()
        endpoint = buckets[1:]
        for i in reversed(range(n)):
            j = SA[i] - 1
            if j >= 0 and not isL[j]:
                endpoint[A[j]] -= 1
                SA[endpoint[A[j]]] = j
        return SA

    isLMS = [+(i and isL[i - 1] and not isL[i]) for i in range(n)]
    isLMS.append(1)
    LMS = [i for i in range(n) if isLMS[i]]
    if len(LMS) > 1:
        SA = induced_sort(LMS)
        LMS2 = [i for i in SA if isLMS[i]]
        prev = -1
        j = 0
        for i in LMS2:
            i1 = prev
            i2 = i
            while prev >= 0 and A[i1] == A[i2]:
                i1 += 1
                i2 += 1
                if isLMS[i1] or isLMS[i2]:
                    j -= isLMS[i1] and isLMS[i2]
                    break
            j += 1
            prev = i
            SA[i] = j
        LMS = [LMS[i] for i in SAIS([SA[i] for i in LMS])]
    return induced_sort(LMS)

def KASAI(A, SA):
    """
    Calculates LCP array in O(n) time
    Input:
    String A and its suffix array SA
    """
    n = len(A)
    rank = [0] * n
    for i in range(n):
        rank[SA[i]] = i
    LCP = [0] * (n - 1)
    k = 0
    for i in range(n):
        SAind = rank[i]
        if SAind == n - 1:
            continue
        j = SA[SAind + 1]
        while i + k < n and A[i + k] == A[j + k]:
            k += 1
        LCP[SAind] = k
        k -= k > 0
    return LCP

def suffixarray(s):
    # O(nlogn)
    n = len(s)
    suffix = sorted(range(n),key=lambda xx:s[xx])
    equi = [0]*n
    for i in range(1,n):
        equi[suffix[i]] = equi[suffix[i-1]]+(s[suffix[i]] != s[suffix[i-1]])
    powe,k = [1<<i for i in range(30)],0
    out = [0]*n
    while powe[k] < n:
        x,y = [equi[i] for i in range(n)],[]
        for i in range(n):
            zz = i+powe[k]
            if zz >= n:
                zz -= n
            y.append(equi[zz])
            suffix[i] -= powe[k]
            if suffix[i] < 0:
                suffix[i] += n

        cnt = [0]*(max(x)+1)
        for i in x:
            cnt[i] += 1
        for i in range(1,len(cnt)):
            cnt[i] += cnt[i-1]
        for z in reversed(suffix):
            cnt[x[z]] -= 1
            out[cnt[x[z]]] = z
        suffix = out[:]

        equi[suffix[0]] = 0
        for i in range(1,n):
            a,b = suffix[i],suffix[i-1]
            equi[a] = equi[b]+(x[a] != x[b] or y[a] != y[b])
        k += 1
    return suffix

def findLCP(s,suffix):
    n = len(s)
    lcp,inde = [0]*(n-1),[0]*n
    for i in range(n):
        inde[suffix[i]] = i
    pr = 0
    for i in range(n):
        x = inde[i]
        if not x:
            continue
        y = suffix[x-1]
        for j in range(pr,n-i):
            if s[i+j] != s[y+j]:
                break
        lcp[x-1] = j
        pr = max(0,j-1)
    return lcp

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