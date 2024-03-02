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
    vi check;
    int H, W;
    cin >> H >> W;

    vector<vector<int>> A(H, vector<int>(W));
    for (int i = 0; i < H; i++)
    {
        for (int j = 0; j < W; j++)
        {
            cin >> A[i][j];
        }
    }

    int H_sec, W_sec;
    cin >> H_sec >> W_sec;
    vector<vector<int>> B(H_sec, vector<int>(W_sec));
    for (int i = 0; i < H_sec; i++)
    {
        for (int j = 0; j < W_sec; j++)
        {
            cin >> B[i][j];
        }
    }

    bool flag = false;

    // {0, 1, ..., n-1} の部分集合の全探索
    for (int bit = 0; bit < (1 << H); ++bit)
    {
        for (int bit_w = 0; bit_w < (1 << W); ++bit_w)
        {
            vvi S;
            for (int i = 0; i < H; ++i)
            {
                vi tmp;
                for (int j = 0; j < W; ++j)
                {
                    if ((bit & (1 << i)) and (bit_w & (1 << j)))
                    { // 列挙に i が含まれるか
                        tmp.push_back(A[i][j]);
                    }
                }
                if (tmp.size() != 0)
                {
                    S.push_back(tmp);
                }
            }

            if (S.size() == H_sec and S[0].size() == W_sec)
            {
                if (B == S)
                {
                    flag = true;
                }
            }
        }
    }

    if (flag)
    {
        cout << "Yes"
             << "\n";
    }
    else
    {
        cout << "No"
             << "\n";
    }

    return 0;
}