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
    string S;
    cin >> S;

    int N = S.size();

    for (int i = 0; i < 8 * N; i++)
    {
        cout << S[i % N];
        if (i == 5)
        {
            break;
        }
    }

    return 0;
}