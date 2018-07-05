from array import array
 
UP = 10 ** 4 + 30
 
graph = [[] for _ in range(UP)]
sieve = [1 for _ in range(UP)]
primes = []
 
for i in range(2, UP):
 if sieve[i]:
  primes.append(i)
  for j in range(2,UP // i):
   sieve[i * j] = 0
 
for prime in primes:
 if 10 ** 4 > prime > 10 ** 3:
  p = str(prime)
  for casa in range(4):
   for alg in range(int(casa == 0), 10):
    n = int(p[:casa] + str(alg) + p[casa+1:])
    # if n < 1000:
    # print(p, n, casa, alg, p[:casa], str(alg), p[casa+1:])
    if sieve[n]:
     graph[prime].append(n)
 
def bfs(n1, n2):
 ans = 0
 fila = [n1]
 marcados = array("i", (0,)) * UP
 comeco = 0
 fim = 1
 while True:
  fim = len(fila)
  if comeco == fim:
   break
  for i in range(comeco, fim):
   atual = fila[i]
   if not marcados[atual]:
    marcados[atual] = 1
    if atual == n2:
     return ans
    for viz in graph[atual]:
     if not marcados[viz]:
      fila.append(viz)
  comeco = fim
  ans += 1
 return ans
 
n = int(input())
for _ in range(n):
 a, b = map(int, input().split())
 # print(graph[a])
 print(bfs(a, b)) 
