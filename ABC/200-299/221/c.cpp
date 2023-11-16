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
    vector<char> v(S.size());
    sort(v.begin(),v.end());
    for (int i = 0; i < S.size(); i++)
    {
        v[i] = S[i];
    }

    ll ans = -10;
    do {
        for (int i = 1; i < S.size(); i++)
        {
            string first, second;
            for (int j = 0; j < i; j++)
            {
                first += v[j];
            }  

            for (int j = i; j < S.size(); j++)
            {
                second += v[j];
            }
            

            if (first[0] == '0' || second[0] == '0')
            {
                continue;
            }
            
            ll tmp = stoll(first) * stoll(second);
            ans = max(ans, tmp);
        }
            // v の要素を表示
    } while( next_permutation(v.begin(), v.end()) );     // 次の順列を生成
    
    if (S.size() == 1)
    {
        cout << S << "\n";
    } else
    {
        cout << ans << "\n";
    }
    

    return 0;
}