# python 2
# AC using PyPy 2.6
# 2.5 seconds

from array import array
from Queue import Queue
 
INF = int('0x3f3f3f3f', 16)
 
for _ in range(int(raw_input())):
    n, m = map(int, raw_input().split())
    n += 1
    grafo = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, raw_input().split())
        grafo[a].append(b)
        grafo[b].append(a)
    fila = Queue()
    marked = array('i', (0,)) * n
    dists = array('i', (INF,)) * n
    added = array('i', (0,)) * n
    dists[1] = 0
    fila.put(1)
    while not fila.empty():
        topo = fila.get()
        if not marked[topo]:
            marked[topo] = 1
            for vizinho in grafo[topo]:
                if dists[vizinho] > dists[topo] + 1:
                    dists[vizinho] = dists[topo] + 1
                    if not added[vizinho]:
                        fila.put(vizinho)
                        added[vizinho] = 1
    print dists[-1]
 
