# by the authority of GOD     author: manhar singh sachdev #

import os,sys
from io import BytesIO,IOBase

#https://github.com/cheran-senthil/PyRival/blob/master/pyrival/data_structures/Trie.py
# use array if memory limit is large and length of strings is small
class Trie:
    def __init__(self, *words):
        self.root = dict()
        for word in words:
            self.add(word)

    def add(self, word):
        current_dict = self.root
        for letter in word:
            current_dict = current_dict.setdefault(letter, dict())
        current_dict["_end_"] = True

    def __contains__(self, word):
        current_dict = self.root
        for letter in word:
            if letter not in current_dict:
                return False
            current_dict = current_dict[letter]
        return "_end_" in current_dict

    def __delitem__(self, word):
        current_dict = self.root
        nodes = [current_dict]
        for letter in word:
            current_dict = current_dict[letter]
            nodes.append(current_dict)
        del current_dict["_end_"]

# for binary problems
class Node:
    def __init__(self):
        self.zero = None
        self.one = None
        self.onpath = 0

class Trie1:
    def __init__(self, node):
        self.root = node

    def add(self, num):
        curr = self.root
        for bit in num:
            if bit == '1':
                if not curr.one:
                    curr.one = Node()
                curr = curr.one
            else:
                if not curr.zero:
                    curr.zero = Node()
                curr = curr.zero
            curr.onpath += 1

    def findmaxxor(self, num):
        curr,val = self.root,0
        for i in num:
            if not curr:
                val *= 2
                continue
            z = '0' if i == '1' else '1'
            if z == '1':
                if curr.one:
                    curr = curr.one
                    val = val*2+1
                else:
                    curr = curr.zero
                    val *= 2
            else:
                if curr.zero:
                    curr = curr.zero
                    val = val*2+1
                else:
                    curr = curr.one
                    val *= 2
        return val

    def __delitem__(self, num):
        curr = self.root
        for bit in num:
            if bit == '1':
                if curr.one.onpath == 1:
                    curr.one = None
                    break
                curr = curr.one
            else:
                if curr.zero.onpath == 1:
                    curr.zero = None
                    break
                curr = curr.zero
            curr.onpath -= 1

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