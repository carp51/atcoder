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

vi BFS(int start, int N, vvi connect)
{
    vi checked(N + 1, -1);
    queue<int> que;

    que.push(start);
    checked[start] = 1;

    vi count(N + 1, 0);

    while (not que.empty())
    {
        int now_city = que.front();
        que.pop();

        for (int i = 0; i < connect[now_city].size(); i++)
        {
            if (checked[connect[now_city][i]] == -1)
            {
                que.push(connect[now_city][i]);
                count[connect[now_city][i]] = count[now_city] + 1;
                checked[connect[now_city][i]] = 1;
            }
        }
    }
    return count;
}

int main()
{
    int N;
    cin >> N;

    vvi connect(N + 1);
    for (int i = 0; i < N; ++i)
    {
        int A, B;
        cin >> A >> B;

        for (int j = 0; j < B; j++)
        {
            int C;
            cin >> C;
            connect[A].push_back(C);
        }
    }

    vi ans = BFS(1, N, connect);

    for (int i = 2; i < N + 1; i++)
    {
        if (ans[i] == 0)
        {
            ans[i] = -1;
        }
        
    }
    

    for (int i = 1; i < N + 1; i++)
    {
        cout << i << " " << ans[i] << "\n";
    }
    return 0;
}