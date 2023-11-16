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
    int h_1, h_2, h_3, w_1, w_2, w_3;
    cin >> h_1 >> h_2 >> h_3 >> w_1 >> w_2 >> w_3;

    int ans = 0;

    for (int lu = 1; lu < 29; lu++)
    {
        for (int ru = 1; ru < 29; ru++)
        {
            for (int lb = 1; lb < 29; lb++)
            {
                for (int rb = 1; rb < 29; rb++)
                {
                    int a, b, c, d;
                    a = w_1 - lu - lb;
                    b = w_2 - ru - rb;
                    c = h_2 - lb - rb;
                    d = h_1 - lu - ru;

                    if (a > 0 and b > 0 and c > 0 and d > 0)
                    {
                        if (((h_3 - a - b) == (w_3 - c - d)) and h_3 - a - b > 0 and w_3 - c - d > 0)
                        {
                            ans += 1;
                        }
                    }
                }
            }
        }
    }

    cout << ans << "\n";

    return 0;
}