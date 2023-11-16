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

    vvi check(N + 10);
    
    for (int i = 0; i < M; i++)
    {
        int A, B;
        cin >> A >> B;

        check[A].push_back(B);
        check[B].push_back(A);
    }
    
    for (int i = 0; i < N; i++)
    {
        sort(check[i + 1].begin(),check[i + 1].end(),std::greater{});

        cout << check[i + 1].size() << " ";

        for (int i = 1; i < check[i + 1].size(); i++) {
           cout << check[i + 1][i];
           if (i < check[i + 1].size())cout << " ";
           else cout << endl;
           }
    }
    
    return 0;
}