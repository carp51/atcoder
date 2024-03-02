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

int BFS(int start, int N, vvi connect) {
    vi checked(N + 1, -1);
    queue<int> que;

    que.push(start);
    checked[start] = 1;

    int count = 1;

    while (not que.empty())
    {
        int now_city = que.front();
        que.pop();

        for (int i = 0; i < connect[now_city].size(); i++)
        {
            if (checked[connect[now_city][i]] == -1)
            {
                que.push(connect[now_city][i]);
                count += 1;
                checked[connect[now_city][i]] = 1;
            } 
        }
    }

    return count;
    
}

int main() {
    int N, M;
	cin >> N >> M;
    vvi connect(N + 1);
    for (int i = 0; i < M; ++i) {
		int A, B;
		cin >> A >> B;

		connect[A].push_back(B);
        connect[B].push_back(A);
	}

    int ans = 0;

    for (int i = 0; i < N; i++)
    {
        ans += BFS(i + 1, N, connect);
    }

    cout << ans << "\n";
    
    return 0;
}