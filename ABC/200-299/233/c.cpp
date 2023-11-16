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
    ll N, X;
    cin >> N >> X;

    vvll check = {{1}};

    for (int i = 0; i < N; i++)
    {
        int L;
        cin >> L;

        vll tmp;

        for (int j = 1; j < L + 1; j++)
        {
            int a;
            cin >> a;
            for (int k = 0; k < check.back().size(); k++)
            {
                if (check.back()[k] > X / a + 10)
                {
                    continue;
                }
                tmp.push_back(check.back()[k] * a);
            }
            
        }
        check.push_back(tmp);
        
    }
    
    ll ans = 0;
    for (int i = 0; i < check.back().size(); i++)
    {
        if (check.back()[i] == X)
        {
            ans += 1;
        }
        
    }
    
    cout << ans << "\n";
    return 0;
}