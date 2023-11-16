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

    vvi check(N + 4);

    for (int i = 0; i < M; i++)
    {
        int k;
        cin >> k;

        for (int j = 0; j < k; j++)
        {
            int x;
            cin >> x;

            check[x].push_back(x);
        }
        
    }
    
    
    
    return 0;
}