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

int main()
{
    int N;
    cin >> N;
    vector<int> a(N);
    for (int i = 0; i < N; i++)
    {
        cin >> a[i];
    }

    stack<vi> que;
    int count = 0;

    for (int i = 0; i < N; i++)
    {
        if (que.size() == 0)
        {
            que.push({a[i], 1});
            count += 1;
        }
        else
        {
            vi tmp = que.top();
            if (tmp[0] == a[i])
            {
                count += 1;
                tmp[1] += 1;
                que.pop();
                que.push({tmp[0], tmp[1]});

                if (tmp[0] == tmp[1])
                {
                    count -= tmp[1];
                    que.pop();
                }
            }
            else
            {
                que.push({a[i], 1});
                count += 1;
            }
        }

        cout << count << "\n";
    }

    return 0;
}