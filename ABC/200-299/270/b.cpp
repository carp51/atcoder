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
    int X, Y, Z;
    cin >> X >> Y >> Z;

    if ((0 < Y and Y < X) or (0 > Y and Y > X))
    {
        if (Y > 0)
        {
            if (Z < Y and 0 < Z)
            {
                cout << abs(X) << "\n";
            } else if (Z < 0) {
                cout << 2 * abs(Z) + abs(X) << "\n"; 
            } else {
                cout << -1 << "\n";
            }
            
        } else if (Y < 0)
        {
            if (Z > Y and 0 > Z)
            {
                cout << abs(X) << "\n";
            } else if (Z > 0) {
                cout << 2 * abs(Z) + abs(X) << "\n"; 
            } else
            {
                cout << -1 << "\n";
            }
            
        }
        
        
        
    } else
    {
        cout << abs(X) << "\n";
    }
    
    
    
    return 0;
}