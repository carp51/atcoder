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

int main() {
    int Y;
    cin >> Y;

    if (Y % 4 == 2)
    {
        cout << Y << "\n";

    } else if (Y % 4 == 1)
    {
        cout << Y + 1 << "\n";

    } else if (Y % 4 == 3)
    {
        cout << Y + 3 << "\n";

    } else
    {
        cout << Y + 2 << "\n";
    }
    
    return 0;
}