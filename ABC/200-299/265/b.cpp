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
    ll N, M, T;
    cin >> N >> M >> T;
    vector<ll> A(N - 1);
    for(int i = 0; i < N - 1; i++) {
        cin >> A[i];
    }
    
    map<ll, ll> dic;
    for (int i = 0; i < M; i++){
        ll X, Y;
        cin >> X >> Y;
        dic[X] = Y;}

    bool flag = false;
    ll i = 0;

    while (T > 0)
    {
        T -= A[i];
        if (T <= 0)
        {
            break;
        }
        
        i += 1;
        T += dic[i + 1];

        if (i + 1 == N)
        {
            flag = true;
            break;
        }      
    }
    
    if (flag)
    {
        cout << "Yes" << "\n";  
    } else
    {
        cout << "No" << "\n";
    }
        
    return 0;
}