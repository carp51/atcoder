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
    int A = 100;
    int B = -10;
    int C = 100;
    int D = -10;
    for (int i = 0; i < 10; i++)
    {
        string S;
        cin >> S;

        for (int j = 0; j < 10; j++)
        {
            if (S[j] == '#')
            {
                A = min(A, i + 1);
                B = max(B, i + 1);
                C = min(C, j + 1);
                D = max(D, j + 1);
            }
            
        }
        
    
    }
    
    cout << A <<" " << B << "\n";
    cout << C <<" " << D << "\n";
    return 0;
}