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
    ll N, P, Q, R;
    cin >> N >> P >> Q >> R;
    
    vector<ll> A(N);
    for(int i = 0; i < N; i++) {
        cin >> A[i];
    }
    
    vector<ll> csA(N + 1);
    csA[0] = 0;
    for (int i = 0; i < N; i++)
        csA[i + 1] = csA[i] + A[i];
    

    map<ll, ll> dic;
    for (int i = 1; i < N + 1; i++){dic[csA[i]] = i;}

    vvll range;
    for (int i = 0; i < N + 1; i++){
        if (dic[P + Q + R + csA[i]] != 0)
        {
            range.push_back({i, dic[P + Q + R + csA[i]]});
        }
    }

    for (ll i = 0; i < range.size(); i++)
    {
        vll check;
        int count = 0;
        ll sum = 0;
        for (ll j = range[i][0]; j < range[i][1]; j++)
        {
            sum += A[j];
            if (count == 0)
            {
                if (sum == P)
                {
                    check.push_back(sum);
                    sum = 0;
                    count += 1;
                }
                
            } else if (count == 1)
            {
                if (sum == Q)
                {
                    check.push_back(sum);
                    sum = 0;
                    count += 1;
                }
            }     
        }
        check.push_back(sum);

        if (check.size() == 3)
        {
            if (check[0] == P and check[1] == Q and check[2] == R)
            {
                cout << "Yes" << "\n";
                exit(0);
            }
            
        }
        
        
    }
    
    cout << "No" << "\n";
    return 0;
}