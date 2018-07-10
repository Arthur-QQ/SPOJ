from ctypes import c_int
from sys import setrecursionlimit

MAXN = 10 ** 4 + 100
MAXL = 15
NIVEIS = (c_int * MAXN)() # int niveis[MAXN];
PAIS = (c_int * MAXN)() # int pais[MAXN];
ANCEST = (c_int * MAXL * MAXN)() # int acnest[MAXN][MAXL];
GRAFO = [[] for _ in range(MAXN)]
setrecursionlimit(MAXN)
def DFS(v):
    for viz in GRAFO[v]:
        if NIVEIS[viz] != -1:
            continue
        NIVEIS[viz] = NIVEIS[v] + 1
        PAIS[viz] = v
        DFS(viz)

def LCA(u, v):
    # assume que n[u] >= n[v]
    for i in range(MAXL - 1, -1, -1): # MAXL - 1 até 0
        if NIVEIS[u] - 2 ** i >= NIVEIS[v]:
            u = ANCEST[u][i]
    # agora n[u] = n[v]
    if u == v:
        return u
    for i in range(MAXL - 1, -1, -1):
        if ANCEST[u][i] != -1 and ANCEST[u][i] != ANCEST[v][i]:
            u = ANCEST[u][i]
            v = ANCEST[v][i]
    return PAIS[u]

n = int(input())
for i in range(n - 1):
    a, b = map(lambda x: int(x) - 1, input().split()) # Pegar 'a' e 'b' separados por espaço e subtrair 1
    GRAFO[a].append(b)
    GRAFO[b].append(a)

for i in range(n):
    PAIS[i] = -1
    NIVEIS[i] = -1
    for j in range(MAXL):
        try:
            ANCEST[i][j] = -1
        except Exception as e:
            print(i, j)
            print(e)
            exit()

PAIS[0] = 0
NIVEIS[0] = 0
DFS(0)

for i in range(n):
    ANCEST[i][0] = PAIS[i]

for i in range(1, MAXL):
    for j in range(n):
        ANCEST[j][i] = ANCEST[ANCEST[j][i-1]][i-1]

q = int(input())
for i in range(q):
    lad, pol = map(lambda x: int(x) - 1, input().split())
    if NIVEIS[lad] < NIVEIS[pol]:
        print('NO')
    else:
        print('YES', LCA(lad, pol) + 1)
