for _ in range(int(input())):
    n = int(input())
    lista = list(map(int, input().split()))
    somas = [lista[0]]
    for i in range(n-1):
        somas.append(somas[-1] + lista[i+1])
    ans = 0
    for j in range(1, n):
        ans += lista[-j] * (n - j  + 1) - somas[-j]
    print(ans)
 
