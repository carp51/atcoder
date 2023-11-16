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
    vector<int> A(N);
    for(int i = 0; i < N; i++) {
        cin >> A[i];
    }

    vi a(N + 100000000, 0);

    for (int i = 0; i < N; i++)
    {
        a[2 * (i + 1)] = a[A[i]] + 1;
        a[2 * (i + 1) + 1] = a[A[i]] + 1;
    }
    
    for (int i = 1; i < 2 * N + 2; i++)
    {
        cout << a[i] << "\n";
    }
    
    return 0;
}