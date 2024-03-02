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
    ll N;
    cin >> N;

    int count = 0;
    vll check;

    for (int a = 2; a < 100000 + 100; a++)
    {
        for (int b = 2; b < 40; b++)
        {
            if (pow(a, b) <= N)
            {
                check.push_back(pow(a, b));
            } else
            {
                break;
            }
        }
    }

    //std::vector<int> v = { 5, 2, 1, 3, 4, 2, 2, 4, 5, 5 };
     
    sort(check.begin(), check.end());
    check.erase(unique(check.begin(), check.end()), check.end());

    cout << N - check.size() << "\n";
    
    return 0;
}