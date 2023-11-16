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
    int H, W;
    cin >> H >> W;
    vector<vector<char>> G(H, vector<char>(W));
    for(int i = 0; i < H; i++) {
        string RU;
        cin >> RU;
        for(int j = 0; j < W; j++) {
            G[i][j] = RU[j];
        }
    }
    
    int h = 0;
    int w = 0;

    vector<vector<int>> checked(H, vector<int>(W));
    for(int i = 0; i < H; i++) {
        for(int j = 0; j < W; j++) {
            checked[i][j] = -1;
        }
    }

    while (true)
    {
        
        checked[0][0] = 1;
        if (G[h][w] == 'U') {
            if (h == 0)
            {
                break;
            } else
            {
                h -= 1;
                if (checked[h][w] == 1)
                {cout << -1 << "\n"; 
                exit(0);
                }
                checked[h][w] = 1;
            }
        } else if (G[h][w] == 'D')
        {
            if (h == H - 1)
            {
                break;
            } else
            {
                h += 1;
                if (checked[h][w] == 1)
                {cout << -1 << "\n"; 
                exit(0);
                }
                checked[h][w] = 1;      
            }
        } else if (G[h][w] == 'L')
        {
            if (w == 0)
            {
                break;
            } else
            {
                w -= 1;
                if (checked[h][w] == 1)
                {cout << -1 << "\n"; 
                exit(0);
                }
                checked[h][w] = 1;
            }
        } else if (G[h][w] == 'R')
        {
            if (w == W - 1 )
            {
                break;
            } else
            {
                w += 1;
                if (checked[h][w] == 1)
                {cout << -1 << "\n"; 
                exit(0);
                }
                checked[h][w] = 1;
            }
        }
        
    }

    cout << h + 1 << ' ' << w + 1 <<"\n";

    
    return 0;
}