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

    if (S[0] == 'M')
    {
        cout << 5 << "\n";
    } else if (S[0] == 'T')
    {
        if (S[1] == 'u')
        {
            cout << 4 << "\n";
        } else {
            cout << 2 << "\n";
        }
        
    } else if (S[0] == 'W')
    {
        
        cout << 3 << "\n";
    } else {
        cout << 1 << "\n";
    }
    
    
    
    return 0;
}