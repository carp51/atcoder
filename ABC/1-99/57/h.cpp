#include <bits/stdc++.h>
using namespace std;

using ull = unsigned long long;
using ll = long long;
using vi = vector<ll>;
using vl = vector<long>;
using vll = vector<long long>;
using vvi = vector<vi>;
using vvl = vector<vl>;
using vvll = vector<vll>;
using vs = vector<string>;
using pii = pair<ll, ll>;

//素数ならばtrueを返す      
bool is_prime(long long n){
    if (n==1) return false;
    long long i=2;
    while (i*i<=n){
        if (n%i==0) return false;
        i++;
    }
    return true;
}

int main() {
    ll N;
    cin >> N;
    vector<ll> A(N);
    for(ll i = 0; i < N; i++) {
        cin >> A[i];
    }

    vll sosuu;

    for (ll i = 2; i < 1300; i++)
    {
        if (is_prime(i))
        {
            sosuu.push_back(i);
        }
        
    }

    ll ans = N + 100;

    for (ll i = 0; i < sosuu.size(); i++)
    {
        map<ll, ll> dic;
        ll count = 0;

        for (ll j = 0; j < N; j++)
        {
            if (dic[A[j] % sosuu[i]] == 0)
            {
                count += 1;
                dic[A[j] % sosuu[i]] = 1;
            } else
            {
                continue;
            }
            
        }
        
        ans = min(ans, count);

        if (ans == 1)
        {
            cout << 1 << "\n";
            exit(0);
        }
        
    }
    
    cout << ans << "\n";
    return 0;
}