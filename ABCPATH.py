xs = [0, 0, -1, -1, -1, 1, 1, 1]
ys = [1, -1, -1, 1, 0, -1, 1, 0]

from sys import version_info

if version_info[0] < 3:
    input = raw_input

from array import array
from itertools import count

def pairing_function(a, b):
    return C * a + b

def maior_path(v):
    if mp[v] != -1:
        return mp[v]
    if len(grafo[v]) == 0:
        mp[v] = 1
    else:
        mviz = max(maior_path(i) for i in grafo[v])
        mp[v] = mviz + 1
    return mp[v]

for testcase in count(1):
    L, C = map(int, input().split())
    if L == C == 0:
        break
    matriz = [input() for _ in range(L)]
    grafo = [[] for _ in range(L * C)]
    mp = array('i', (-1,)) * (L * C)
    count_a = 0
    for i in range(L):
        for j in range(C):
            if matriz[i][j] == 'A':
                count_a += 1
            for k in range(8):
                nx = xs[k] + i
                ny = ys[k] + j
                if 0 <= nx < L and 0 <= ny < C and ord(matriz[nx][ny]) - ord(matriz[i][j]) == 1:
                    grafo[pairing_function(i, j)].append(pairing_function(nx, ny))
    ans = 0 if count_a == 0 else max(maior_path(i) for i in range(L * C) if matriz[i // C][i % C] == 'A')
    print('Case {}: {}'.format(testcase, ans))
