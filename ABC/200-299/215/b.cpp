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

ll powll(ll n, ll x) {
    ll tmp = 1;
    for (ll i = 0; i < x; i++){tmp *= n;}
    return tmp;
}

int main()
{
    ll N;
    cin >> N;

    for (ll i = 0; i < 100000000000000; i++)
    {
        if (powll(2, i) <= N and N < powll(2, i + 1))
        {
            cout << i << "\n";
            exit(0);
        }
    }

    return 0;
}