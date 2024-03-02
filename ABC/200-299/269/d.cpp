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

int ctoi(char c) {
   if (c >= '0' && c <= '9') {
       return c - '0';
   }
   return 0;
}

map<string, int> all_dic;

int BFS(string X, string Y, map<string, int> dic) {
    if (all_dic[X + '_' + Y] == 0)
    {
        return 0;
    }

    queue<string> que;

    vvi d = {{-1, -1}, {-1, 0}, {0, -1}, {0, 1}, {1, 0}, {1, 1}};

    que.push(X + '_' + Y);
    dic[X + '_' + Y] = 0;

    int count = 1;

    
    

    while (not que.empty())
    {
        string now_city = que.front();
        que.pop();

        for (int i = 0; i < d.size(); i++)
        {
            string n_X;
            string n_Y;

            int to;

            for (int j = 0; j < 10000; j++)
            {
                if (now_city[j] == '_')
                {
                    to = j + 1;
                    break;
                }
                n_X.push_back(now_city[j]);
            }

            for (int j = to; j < 10000; j++)
            {
                if (now_city[j] == '_')
                {
                    break;
                }
                n_Y.push_back(now_city[j]);
            }
            
            int new_X = stoi(n_X);
            int new_Y = stoi(n_Y);

            new_X += d[i][0];
            new_Y += d[i][1];
            if (dic[to_string(new_X) + "_" + to_string(new_Y)] == 1)
            {
                que.push(to_string(new_X) + "_" + to_string(new_Y));
                dic[to_string(new_X) + "_" + to_string(new_Y)] = 0;
                all_dic[to_string(new_X) + "_" + to_string(new_Y)] = 0;
            }
        }
    }

    return count;
    
}

int main() {
    int N;
    cin >> N;

    map<string, int> dic;
    vvi XY;

    for (int i = 0; i < N; i++)
    {
        string X, Y;   
        cin >> X >> Y;

        dic[X + '_' + Y] = 1;
        XY.push_back({stoi(X), stoi(Y)});
    }
    
    
    int ans = 0;

    all_dic = dic;
    
    for (int i = 0; i < N; i++)
    {
       ans += BFS(to_string(XY[i][0]), to_string(XY[i][1]), dic);
    }
    
    cout << ans << "\n";
    
    
    return 0;
}