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
    string S;
    cin >> S;
    
    int count = -1;

    for (int i = 0; i < S.size(); i++)
    {
        if (S[i] == 'a') {
            count = i + 1;
        }
    }
    
    if (count == -1)
    {
        cout << -1 << "\n";
    } else
    {
        cout << count << "\n";
    }
    
    
    return 0;
}