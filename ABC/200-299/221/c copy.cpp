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
    string S;
    cin >> S;
    vector<int> v(S.size());
    iota(v.begin(), v.end(), 1);  
    
    ll ans = -10;
    do {
        for (int i = 1; i < S.size(); i++)
        {
            string first, second;
            for (int j = 0; j < S.size(); j++)
            {
                if (j < i)
                {
                    first += S[v[j] - 1];
                } else
                {
                    second += S[v[j] - 1];
                }
            }

            if (first[0] == '0' or second[0] == '0')
            {
                continue;
            }
            
            ans = max(ans, stoll(first) * stoll(second));
        }
            // v の要素を表示
    } while( next_permutation(v.begin(), v.end()) );     // 次の順列を生成
    
    if (S.size() == 1)
    {
        cout << S << "\n";
    } else {
        cout << ans << "\n";
    }
    
    return 0;
}