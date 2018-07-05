MAXN = 10 ** 6 * 2 + 5
MOD = 10 ** 9 + 7

dp = [-1 for _ in range(MAXN)]
dp[0] = dp[1] = 1

for i in range(2, MAXN):
    dp[i] = i * dp[i-1] % MOD

for _ in range(int(input())):
    a, b = map(int, input().split())
    num = dp[a + b]
    den = (dp[a] * dp[b]) % MOD
    denmodminusone = pow(den, MOD - 2, MOD)
    print(num * denmodminusone % MOD)
