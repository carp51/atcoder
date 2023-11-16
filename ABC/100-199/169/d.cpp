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

ll f(int n) {
    return n * (n + 1) / 2;
}

int main() {
    ll N;
    cin >> N;

    vll check = factorize(N);
    ll ans = 0;

    map<string, int> dic;
    for (int i = 0; i < check.size(); i++){dic[to_string(check[i])] = 0;}
    for (int i = 0; i < check.size(); i++){dic[to_string(check[i])] += 1;}
    
    for(auto i = dic.begin(); i != dic.end(); ++i){
        string k = i->first;
        int v = i->second;

        for (int j = 0; j < 100000000; j++)
        {
            if (f(j) < v and v <= f(j + 1) and k != "1")
            {
                if (v == f(j + 1))
                {
                    ans += j + 1;
                } else
                {
                    ans += j;
                }
                break;
            } 
        }
    }

    cout << ans << "\n";
    
    return 0;
}