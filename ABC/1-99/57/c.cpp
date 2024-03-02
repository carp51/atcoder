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

vector<long long> factorize(long long n){
    long long i=2;
    vector<long long> fct;
    while (i*i<=n){
        while (n%i==0){
            n/=i;
            fct.push_back(i);
        }
        i++;
    }
    if (n>1) fct.push_back(n);
    if (fct.size()==0) fct.push_back(1);
    return fct;
}

int main() {
    ll N;
    cin >> N;
    vll check = factorize(N);

    deque<ll> que;

    for (ll i = 0; i < check.size(); i++)
    {
        que.push_back(check[i]);
    }

    if (check.size() == 1)
    {
        cout << to_string(check[0]).size() << "\n";
        exit(0);
    }
    

    ll L_num = que[0];
    ll R_num = que[que.size() - 1];

    que.pop_front();
    que.pop_back();

    while (que.size() > 0)
    {
        ll L = to_string(L_num).size();
        ll R = to_string(R_num).size();
        if (L_num <= R_num)
        {  
            L_num *= que[0];
            que.pop_front();
            
        } else
        {
            R_num *= que[que.size() - 1];
            que.pop_back();
        }
        
        
    }

    cout << max(to_string(L_num).size(), to_string(R_num).size())<< "\n";
    cout << L_num << "," << R_num << "\n";
    
    return 0;
}