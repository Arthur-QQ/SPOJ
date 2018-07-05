def getpoints(word):
    if len(word) <= 4:
        return 1
    if len(word) <= 5:
        return 2
    if len(word) <= 6:
        return 3
    if len(word) <= 7:
        return 5
    return 11
 
n = int(input())
 
ents = [set(input().split()) for _ in range(n)]
tudo = set()
repetidas = set()
 
pontos = [0 for _ in range(n)]
 
for e1 in ents:
    for e2 in e1:
        if e2 not in tudo:
            tudo.add(e2)
        else:
            repetidas.add(e2)
 
for i in range(n):
    at = ents[i]
    for j in at:
        if j not in repetidas:
            pontos[i] += getpoints(j)
 
print(max(pontos)) 
