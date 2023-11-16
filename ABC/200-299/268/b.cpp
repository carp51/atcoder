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
    string S, T;
    cin >> S >> T;

    if (S.size() <= T.size())
    {
        for (int i = 0; i < S.size(); i++)
        {
            if (S[i] != T[i])
            {
                cout << "No" << "\n";
                exit(0);
            }
            
        }

        cout << "Yes" << "\n";
        
    } else
    {
        cout << "No" << "\n";
    }
    
    
    
    return 0;
}