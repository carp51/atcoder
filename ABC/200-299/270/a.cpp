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
    int A, B;
    cin >> A >> B;

    vi num = {1, 2, 4};
    vector<bool> check = {false, false, false};

    if (A == 1)
    {
        check[0] = true;
    } else if (A == 2)
    {
        check[1] = true;
    } else if (A == 3)
    {
        check[1] = true;
        check[0] = true;
    } else if (A == 4)
    {
        check[2] = true;
    } else if (A == 5)
    {
        check[0] = true;
        check[2] = true;
    } else if (A == 6)
    {
        check[1] = true;
        check[2] = true;
    } else if (A == 7)
    {
        check[0] = true;
        check[1] = true;
        check[2] = true;
    }
    
    if (B == 1)
    {
        check[0] = true;
    } else if (B == 2)
    {
        check[1] = true;
    } else if (B == 3)
    {
        check[1] = true;
        check[0] = true;
    } else if (B == 4)
    {
        check[2] = true;
    } else if (B == 5)
    {
        check[0] = true;
        check[2] = true;
    } else if (B == 6)
    {
        check[1] = true;
        check[2] = true;
    } else if (B == 7)
    {
        check[0] = true;
        check[1] = true;
        check[2] = true;
    }
    
    int ans = 0;

    for (int i = 0; i < 3; i++)
    {
        if (check[i])
        {
            ans += num[i];
        }
        
    }
    
    cout << ans << "\n";
    return 0;
}