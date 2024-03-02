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
    int N, Q;
    cin >> N >> Q;

    vvi a;

    for (int i = 0; i < N; i++)
    {
        int b;
        cin >> b;

        vi tmp;
        for (int i = 0; i < b; i++)
        {
            int c;
            cin >> c;
            tmp.push_back(c);
        }

        a.push_back(tmp);
        
    }
    
    for (int i = 0; i < Q; i++)
    {
        int s, t;
        cin >> s >> t;

        cout << a[s-1][t-1] << "\n";
    }
    
    return 0;
}