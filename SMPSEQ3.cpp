#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int slen, qlen;
    cin >> slen;
    int vs[slen];
    for (int i = 0; i < slen; i++) {
        cin >> vs[i];
    }
    cin >> qlen;
    int vq[qlen];
    for (int i = 0; i < qlen; i++) {
        cin >> vq[i];
    }
    vector<int> resp;
    for (int i = 0; i < slen; i++) {
        int el = vs[i];
        int ini = 0, fim = qlen - 1;
        int meio = (ini + fim) / 2;
        while (ini <= fim) {
            meio = (ini + fim) / 2;
            if (vq[meio] > el) {
                fim = meio - 1;
            } else if (vq[meio] < el) {
                ini = meio + 1;
            } else {
                break;
            }
        }
        if (ini > fim) {
            resp.push_back(el);
        }
    }
    sort(resp.begin(), resp.end());
    for (int i = 0; i < resp.size(); i++) {
        cout << resp[i] << (i + 1 == (int)resp.size() ? "" : " ");
    }
}
