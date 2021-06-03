import math 
from collections import Counter, defaultdict
import sys, resource
# resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
# sys.setrecursionlimit(10**6)

"""
# Template Designed By: Shivshanker Singh
# Note: If you find this template useful and want to use it then please don't just copy paste it 
        you can take ideas from this and make your own.
        because if you copy paste as it is then there are high chances that both of us will be plagiarized
        (because most of code will be same for small problems).
        So to avoid this please dont copy paste.
"""

mod       = 10**9 + 7
input     = sys.stdin.readline
readInt   = lambda : int(input().strip())
readfloat = lambda : float(input().strip())
readStr   = lambda : input().strip()
intList   = lambda : list(map(int, input().strip().split()))
intMap    = lambda : map(int, input().strip().split())
floatList = lambda : list(map(float, input().strip().split()))
floatMap  = lambda : map(float, input().strip().split())
strList   = lambda : list(input().strip().split())


def print(*args, end='\n', sep=' '):
    for i in args:
        sys.stdout.write(str(i))
        sys.stdout.write(sep)
    sys.stdout.write(end)

    
def generate_segment(arr):
    n = len(arr)
    n = 2**math.ceil(math.log2(n))
    seg = [0]*(2*n)
    for i in range(len(arr)):
        seg[n+i] = arr[i]
    for k in range(n-1, 0, -1):
        seg[k] = seg[2*k] + seg[2*k+1]
    
    return seg

def update(idx, val):
    n = 2**math.ceil(math.log2(len(arr)))
    idx += n
    seg[idx] = val
    idx //= 2
    while idx > 0:
        seg[idx] = seg[2*idx] + seg[2*idx + 1]
        idx //= 2



def solve():
    pass
    
# if __name__ == '__main__':
for _ in range(readInt()):
    # n = readInt()
    n, k = intMap()
    s = list(input().strip())
    qrr = intList()
    arr = [0]*n
    for i in range(1, n):
        if s[i] == s[i-1]:
            arr[i] = 2
        else:
            arr[i] = 1
    seg = generate_segment(arr)
    for q in qrr:
        q -= 1
        if s[q] == '0':
            s[q] = '1'
        else:
            s[q] = '0'
        if q!= 0:
            if (s[q] == s[q-1]):
                update(q, 2)
            else:
                update(q, 1)
        if q != n-1:
            if s[q+1] == s[q]:
                update(q+1, 2)
            else:
                update(q+1, 1)
        print(seg[1])