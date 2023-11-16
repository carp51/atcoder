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
    ll N, K;
    cin >> N >> K;
    vector<ll> A(N);
    for(int i = 0; i < N; i++) {
        cin >> A[i];
    }
    
    vector<ll> csA(N + 1);
    csA[0] = 0;
    for (int i = 0; i < N; i++)
        csA[i + 1] = csA[i] + A[i];
    
    map<ll, ll> dic;
    for (int i = 0; i < N + 1; i++){dic[csA[i]] += 1;}

    ll ans = 0;

    for (int i = 0; i < N + 1; i++)
    {
        dic[csA[i]] -= 1;
        ans += dic[K + csA[i]];
        
    }
    
    cout << ans << "\n";
    return 0;
}