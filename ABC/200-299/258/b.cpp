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
    vector<vector<char>> A(N, vector<char>(N));
    for(int i = 0; i < N; i++) {
        for(int j = 0; j < N; j++) {
            cin >> A[i][j];
        }
    }

    vvi d = {{0, 1}, {1, 1}, {1, 0}, {1, -1}, {0, -1}, {-1, -1}, {-1, 0}, {-1, 1}};

    ll ans = -10;

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {   
            ll ans_tmp = -10;
            
            for (int k = 0; k < 8; k++)
            {   
                string tmp;
                int di = i;
                int dj = j;

                for (int n = 0; n < N; n++)
                {   
                    tmp.push_back(A[(di + 10000 * N) % N][(dj + 10000 * N) % N]);
                    di += d[k][0];
                    dj += d[k][1];
                }

                ans_tmp = max(ans_tmp, stoll(tmp));
                
            }
            
            ans = max(ans, ans_tmp);

        }
        
    }
    
    cout << ans << "\n";
    
    return 0;
}