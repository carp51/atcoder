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
    int N, M;
    cin >> N >> M;

    int n, r;
    
    n = M;
    r = N;
    
    vector<bool> v(n);
    fill(v.begin(), v.begin() + r, true);
    
    do {
       for (int i = 0; i < n; ++i) {
           if (v[i]) {
               cout << (i + 1) << " ";
           }
       }
       cout << "\n";
    } while (prev_permutation(v.begin(), v.end()));
       
    return 0;
}