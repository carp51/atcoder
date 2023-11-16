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
    int N, X;
    cin >> N >> X;

    X *= 100;
    int count = 0;
    int alc = 0;

    for (int i = 0; i < N; i++)
    {
        int V, P;
        cin >> V >> P;

        alc += V * P;
        count += 1;

        if (alc > X)
        {
            cout << count << "\n";
            exit(0);
        } 
    }
    
    cout << -1 << "\n";

    return 0;
}