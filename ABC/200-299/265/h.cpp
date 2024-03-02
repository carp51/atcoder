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
    int N, X, Y;
    cin >> N >> X >> Y;

    for (int i = 1; i < N + 1; i++)
    {
        if (i % X == 0 and i % Y == 0)
        {
            cout << "AB"
                 << "\n";
        }
        else if (i % X == 0)
        {
            cout << "A"
                 << "\n";
        }
        else if (i % Y == 0)
        {
            cout << "B"
                 << "\n";
        }
        else
        {
            cout << "N"
                 << "\n";
        }
    }

    return 0;
}