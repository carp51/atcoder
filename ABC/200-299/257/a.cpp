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
    int N, K, Q;
    cin >> N >> K >> Q;
    vector<int> A(K);
    vector<int> L(Q);
    
    for(int i = 0; i < K; i++) {
        cin >> A[i];
    }
    for(int i = 0; i < Q; i++) {
        cin >> L[i];
    }

    for (int i = 0; i < Q; i++)
    {
        if (A[L[i] - 1] == N)
        {
            continue;
        } else if (L[i] == K)
        {
            A[L[i] - 1] += 1;
        } else if (A[L[i] - 1] + 1 < A[L[i]])
        {
            A[L[i] - 1] += 1;
        }
        
        
        
    }
    
    for (int i = 0; i < K; i++) {
        cout << A[i];
        if (i < K)cout << " ";
        else cout << endl;
    }

    return 0;
}