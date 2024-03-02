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
    vector<int> B(N);
    for(int i = 0; i < N; i++) {
        cin >> A[i];
    }
    for(int i = 0; i < N; i++) {
        cin >> B[i];
    }

    int count = 0;
    for (int i = 0; i < N; i++)
    {
        count += A[i] * B[i];
    }

    if (count == 0) 
    {
        cout << "Yes" << "\n";
    } else
    {
        cout << "No" << "\n";
    }
    
    return 0;
}