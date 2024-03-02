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
    int N, S, D;
    cin >> N >> S >> D;
    bool flag = false;
    for(int i = 0; i < N; i++) {
        int X, Y;
        cin >> X >> Y;

        if (X < S and Y > D)
        {
            flag = true;
            break;
        }
        
    };

    if (flag)
    {
        cout << "Yes" << "\n";
    } else
    {
        cout << "No" << "\n";
    }
    
    return 0;
}