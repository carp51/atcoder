#include <bits/stdc++.h>
using namespace std;

using ull = unsigned long long;
using ll = long long;
using vi = vector<int>;
using vl = vector<long>;
using vll = vector<long long>;
using vvi = vector<vi>;
using vvl = vector<vl>;
using vvll = vector<vll>;
using vs = vector<string>;
using pii = pair<int, int>;

int main() {
    int N;
    cin >> N;
    vector<int> A(N);
    for(int i = 0; i < N; i++) {
        cin >> A[i];
    }

    vi g;
    vi k;

    for (int i = 0; i < N; i++)
    {
        if (A[i] % 2 == 0)
        {
            g.push_back(A[i]);
        } else
        {
            k.push_back(A[i]);
        }
    }
    
    sort(g.begin(),g.end(),std::greater{});
    sort(k.begin(),k.end(),std::greater{});

    if (g.size() == 1 and k.size() == 1)
    {
        cout << -1 << "\n";
    } else if (k.size() == 0)
    {
        cout << g[0] + g[1] << "\n";
    } else if (g.size() == 0)
    {
        cout << k[0] + k[1] << "\n";
    } else if (k.size() == 1) {
        cout << g[0] + g[1] << "\n";
    } else if (g.size() == 1) {
        cout << k[0] + k[1] << "\n";
    } else
    {
        cout << max(g[0] + g[1], k[0] + k[1]) << "\n";
    }
    
    
    
    
    return 0;
}