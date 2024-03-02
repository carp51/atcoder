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

vvi BFS(vi start, vvi maze, int N, vvll num)
{
    queue<vi> que;

    que.push(start);

    while (not que.empty())
    {
        vi now_city = que.front();
        que.pop();

        for (int j = 0; j < num.size(); j++)
        {
            int a = num[j][0];
            int b = num[j][1];
            vvi d = {{a, b}, {a, -b}, {-a, b}, {-a, -b}, {b, a}, {b, -a}, {-b, a}, {-b, -a}};

            for (int i = 0; i < 8; i++)
            {
                vi next_city = {now_city[0] + d[i][0], now_city[1] + d[i][1]};
                if (0 > next_city[0] or next_city[0] >= N)
                {
                    continue;
                }

                if (0 > next_city[1] or next_city[1] >= N)
                {
                    continue;
                }

                if (maze[next_city[0]][next_city[1]] == -1)
                {
                    maze[next_city[0]][next_city[1]] = maze[now_city[0]][now_city[1]] + 1;
                    que.push(next_city);
                }
            }
        }
    }

    return maze;
}

int main()
{
    int N, M;
    cin >> N >> M;

    vvll num;

    for (ll i = 0; i < 1050; i++)
    {
        for (ll j = i; j < 1050; j++)
        {
            if (i * i + j * j > 10000000)
            {
                break;
            }

            if (i * i + j * j == M)
            {
                num.push_back({i, j});
            }
        }
    }

    vector<vector<int>> maze(N, vector<int>(N));

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            maze[i][j] = -1;
        }
    }
    maze[0][0] = 0;

    if (num.size() == 0)
    {
        for (int i = 0; i < N; i++)
        {
            for (int j = 0; j < N; j++)
            {
                cout << maze[i][j];
                if (j < N - 1)
                    cout << " ";
                else
                    cout << "\n";
            }
        }
        exit(0);
    }

    vvi ans = BFS({0, 0}, maze, N, num);

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            cout << ans[i][j];
            if (j < N - 1)
                cout << " ";
            else
                cout << "\n";
        }
    }

    return 0;
}