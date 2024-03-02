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
    vector<int> P(N + 10);
    for(int i = 2; i < N + 1; i++) {
        int x;
        cin >> x;
        P[i] = x;
    }

    int now = N;
    int count = 0;

    while (now != 1)
    {
        count += 1;
        now = P[now];
    }
    
    cout << count << "\n";
    
    return 0;
}