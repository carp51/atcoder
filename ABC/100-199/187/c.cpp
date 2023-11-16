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
    vector<string> S(N);
    for (int i = 0; i < N; i++)
    {
        cin >> S[i];
    }

    map<string, int> dic;

    for (int i = 0; i < N; i++)
    {
        if (dic[S[i]] == 0)
        {
            cout << S[i] << "\n";
            dic[S[i]] += 1;
        }
        else
        {
            cout << "!" + S[i] << "\n";
            dic[S[i]] += 1;
        }
    }
    return 0;
}