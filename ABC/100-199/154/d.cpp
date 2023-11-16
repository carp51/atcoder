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

double f(int n) {
    double tmp = n * (1 + n) / 2;
    return tmp;
}

int main() {
    int N, K;
    cin >> N >> K;
    vector<double> p(N);
    for(int i = 0; i < N; i++) {
        cin >> p[i];
    }

    vector<double> check;
    for (int i = 0; i < N; i++)
    {
        double k = f(p[i]) / p[i];
        check.push_back(k);
    }

    double ans = -10.0;

    vector<double> csc(N + 1);
    csc[0] = 0;
    for (int i = 0; i < N; i++)
        csc[i + 1] = csc[i] + check[i];
    
    for (int i = 0; i <= N - K; i++)
    {
        ans = max(ans, csc[i + K] - csc[i]);
    }
    
    cout << fixed << setprecision(10);
    cout << ans << "\n";
    
    return 0;
}