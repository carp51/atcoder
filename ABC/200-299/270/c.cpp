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

int N, X, Y;
vi ans;

void DFS(int now, int pre, vvi connect, vi to) {
    ans.push_back(now);
    to[now] = 1;

    if (now == Y)
    {
        return;
    }
    
    
    for (int i = 0; i < connect[now].size(); i++)
    {
        if (to[connect[now][i]] == -1)
        {
            to[connect[now][i]] = 1;
            DFS(connect[now][i], now, connect, to);
        }

        
    }

    if (ans[ans.size() - 1] == Y)
    {
        for (int i = 0; i < ans.size(); i++) {
       cout << ans[i];
       if (i < ans.size())cout << " ";
       else cout << endl;
       } 

       exit(0);
    }
    
    ans.pop_back();
}

int main() {
    cin >> N >> X >> Y;
    vvi connect(N + 1);
    vi to(N + 1, -1);
    for (int i = 0; i < N - 1; ++i) {
       int A, B;
       cin >> A >> B;
       connect[A].push_back(B);
       connect[B].push_back(A);
    }
    
    DFS(X, -1, connect, to);

    
    return 0;
}