#include <iostream>
 
using namespace std;
 
string reverter(string s) {
    string ans = "";
    for (int i = 0; i < s.size(); i++) {
        ans += s[s.size() - i - 1];
    }
    return ans;
}
 
int main() {
    int t;
    string al, bl;
    cin >> t;
    for (int i = 0; i < t; i++) {
        cin >> al >> bl;
        int rev_a = stoi(reverter(al).c_str());
        int rev_b = stoi(reverter(bl).c_str());
        int soma = rev_a + rev_b;
        cout << stoi(reverter(to_string(soma)).c_str()) << "\n";
    }
} 
