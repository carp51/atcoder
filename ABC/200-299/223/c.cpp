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
    vector<double> A(N);
    vector<double> B(N);
    for(int i = 0; i < N; i++) {
        cin >> A[i];
        cin >> B[i];
    }
    
    double time = 0;
    for (int i = 0; i < N; i++)
    {
        time += A[i] / B [i];
    }

    time /= 2;
    double ans = 0;
    
    for (int i = 0; i < N; i++)
    {
        if (time - (A[i] / B [i]) >= 0)
        {
            ans += A[i];
            time -= A[i] / B [i];
        } else
        {
            ans += time * B[i];
            break;
        }
    }
    
    cout << fixed << setprecision(17);
    cout << ans << "\n";
    return 0;
}