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
    vector<int> p(N);
    for (int i = 0; i < N; i++)
    {
        cin >> p[i];
    }

    map<int, int> pos;

    for (int i = 0; i < N; i++)
    {
        pos[p[i]] = i;
    }

    vvi LR;

    for (int i = 0; i < N; i++)
    {
        int L = 0;
        int R = 0;
        L += N - 1 + i;
        R += N - 1 + i;

        

        vi tmp = {0, 0};
    
        if (i == pos[i])
        {
            LR.push_back({N - 1, N - 1});
            
            tmp = {0, 1};
            
        } else if (i - pos[i] == -1)
        {
            LR.push_back({0, 0});
            
            tmp = {N - 2, N - 1};
        } else if (i - pos[i] == 1)
        {
            tmp = {0, 2};
        } else if (i > pos[i])
        {
            tmp = {i - 1 - pos[i], i - 1 - pos[i] + 2};
        } else if (i < pos[i])
        {
            tmp = {i + N - 1 - pos[i], i + N - 1 - pos[i] + 2};
        } 

        LR.push_back(tmp);
    }

    int ans = -10;

    vi check_i(N, 0);
    vi tmp(N, 0);

    for (int i = 0; i < LR.size(); i++)
    {
        int L = LR[i][0];
        int R = LR[i][1];

        tmp[L] += 1;
        if (R < N)
        {
            tmp[R + 1] -= 1;
        } 
    }
    
    check_i[0] = tmp[0];
    for (int i = 1; i < N; i++)
    {
        check_i[i] += check_i[i - 1] + tmp[i];
        ans = max(ans, check_i[i]);
    }
    
    cout << ans << "\n";
    return 0;
}