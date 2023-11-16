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
    vector<ll> A(N);
    for(int i = 0; i < N; i++) {
        cin >> A[i];
    }

    ll ans = -10;

    for (int l = 0; l < N; l++)
    {   ll tmp = -10;
        ll min_num = A[l];
        ll count = 0;
        for (int r = l ; r < N; r++)
        {
            count += 1;
            min_num = min(min_num, A[r]);
            tmp = max(tmp, min_num * count);
        }

        ans = max(ans, tmp);
        
    }
    
    cout << ans << "\n";
    return 0;
}