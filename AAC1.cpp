// AC in C++ 4.3.2
// 2.21 seconds

#include <iostream>
#include <vector>
#include <queue>
 
#define INF 999999999
#define MAXN 10005
 
using namespace std;
 
vector<int> grafo[MAXN];
int distancias[MAXN], marcados[MAXN];
 
int main() {
    int t; cin >> t;
    for (int i = 0; i < t; i++) {
        int n, m;
        cin >> n >> m;
        for (int i = 0; i < n; i++) {
            marcados[i] = 0;
            distancias[i] = INF;
            grafo[i].clear();
        }
        int a, b;
        for (int i = 0; i < m; i++) {
            cin >> a >> b; a--; b--;
            grafo[a].push_back(b);
            grafo[b].push_back(a);
        }
        queue<int> s;
        s.push(0);
        distancias[0] = 0;
        while (true) {
            int davez = -1;
            while (!s.empty()) {
                int topo = s.front(); s.pop();
                if (!marcados[topo]) {
                    davez = topo;
                    break;
                }
            }
            if (davez == -1) {
                break;
            }
            marcados[davez] = 1;
            for (int i = 0; i < grafo[davez].size(); i++) {
                int viz = grafo[davez][i];
                if (distancias[viz] > distancias[davez] + 1) {
                    distancias[viz] = distancias[davez] + 1;
                    s.push(viz);
                }
            }
        }
        cout << distancias[n - 1] << "\n";
    }
}
 
