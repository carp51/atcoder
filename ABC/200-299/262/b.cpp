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
    vector<vector<int>> connect(N, vector<int>(N));
    for(int i = 0; i < M; i++) {
        int U, V;
        cin >> U >> V;

        connect[U - 1][V - 1] = 1;
        connect[V - 1][U - 1] = 1;
    }

    int ans = 0;

    for (int i = 0; i < N; i++)
    {
        for (int j = i + 1; j < N; j++)
        {
            for (int k = j + 1; k < N; k++)
            {
                if (connect[i][j] == 1 and connect[j][k] == 1 and connect[k][i] == 1)
                {
                    ans += 1;
                }
                
            }
            
        }
        
    }

    cout << ans << "\n";
    
    return 0;
}