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

int factorial1(int n)
{
    int ret = 1;
    while (n > 1)
        ret *= n--;
    return ret;
}

int main() {
    int n;
    cin >> n;
    cout << factorial1(n) << "\n";
    
    return 0;
}