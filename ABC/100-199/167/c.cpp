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
    int N, M, X;
    cin >> N >> M >> X;
    vector<vector<ll>> CA(N, vector<ll>(M + 1));
    for(int i = 0; i < N; i++) {
        for(int j = 0; j < M + 1; j++) {
            cin >> CA[i][j];
        }
    }

    ll ans = 1000000000000;
    
    // {0, 1, ..., n-1} の部分集合の全探索
    for (int bit = 0; bit < (1<<N); ++bit) {
        vector<int> S;
        vll check;
        ll sum_n = 0;
        for (int j = 0; j < M; j++){check.push_back(0);}

        for (int i = 0; i < N; ++i) {
            
            if (bit & (1<<i)) { // 列挙に i が含まれるか
                sum_n += CA[i][0];
                for (int k = 1; k < M + 1; k++)
                {
                    if (check[k - 1] > X)
                    {
                        continue;
                    }
                    
                    check[k - 1] += CA[i][k];
                }

        bool flag = true;
        for (int k = 0; k < M; k++)
        {
            if (check[k] < X)
            {
                flag = false;
            }
                    
        }

        if (flag)
        {
            ans = min(ans, sum_n);
        }
                        
        }
        } 
    }

    if (ans != 1000000000000)
    {
        cout << ans << "\n";
    } else
    {
        cout << -1 << "\n";
    }
    
    
    return 0;
}