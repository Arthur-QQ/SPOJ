#include <iostream>
#include <vector>

#define MAXN 10100
#define MAXL 15

using namespace std;

int n, q;
vector<int> grafo[MAXN];
int pai[MAXN];
int niveis[MAXN];
int ancest[MAXN][MAXL];

void DFS(int v) {
    for (int i = 0; i < grafo[v].size(); i++) {
        int viz = grafo[v][i];
        if (niveis[viz] != -1) {
            continue;
        }
        niveis[viz] = niveis[v] + 1;
        pai[viz] = v;
        DFS(viz);
    }
}

int LCA(int u, int v) {
    // niveis[u] >= niveis[v]
    if (niveis[u] < niveis[v]) {
        return LCA(v, u);
    }
    // u vai subir na arvore ate chegar no nivel de v
    // cout << u << " " << v << "\n";
    // cout << niveis[u] << " " << niveis[v] << "\n";
    for (int i = MAXL - 1; i >= 0; i--) {
        if (niveis[u] - (1 << i) >= niveis[v]) {
            u = ancest[u][i];
            // cout << u << "\n";
        }
    }
    // cout << u << " " << v << "\n";
    if (u == v) {
        return u;
    }
    for (int i = MAXL - 1; i >= 0; i--) {
        if (ancest[u][i] != ancest[v][i] && ancest[u][i] != -1 && ancest[v][i] != -1) {
            u = ancest[u][i];
            v = ancest[v][i];
        }
    }
    return pai[u];
}

int main() {
    cin >> n;
    int a, b;
    for (int i = 1; i < n; i++) {
        cin >> a >> b;
        a--;
        b--;
        grafo[a].push_back(b);
        grafo[b].push_back(a);
    }
    for (int i = 0; i < n; i++) {
        niveis[i] = -1;
    }
    pai[0] = 0;
    niveis[0] = 0;
    DFS(0);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < MAXL; j++) {
            ancest[i][j] = -1;
        }
    }
    for (int i = 0; i < n; i++) {
        ancest[i][0] = pai[i];
    }
    for (int i = 1; i < MAXL; i++) {
        for (int j = 0; j < n; j++) {
            ancest[j][i] = ancest[ancest[j][i-1]][i-1];
        }
    }
    cin >> q;
    int ladrao, pol;
    for (int i = 0; i < q; i++) {
        cin >> ladrao >> pol;
        ladrao--;
        pol--;
        if (niveis[ladrao] < niveis[pol]) {
            cout << "NO\n";
        } else {
            cout << "YES " << LCA(pol, ladrao) + 1 << "\n";
        }
    }
}
