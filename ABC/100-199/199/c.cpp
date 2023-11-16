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
    int N;
    cin >> N;
    string S;
    cin >> S;
    int Q;
    cin >> Q;

    bool flag = true;

    for (int i = 0; i < Q; i++)
    {
        int T, A, B;
        cin >> T >> A >> B;

        if (T == 1)
        {
            if (flag)
            {
                swap(S[A - 1], S[B - 1]);
            } else
            {
                swap(S[(A - 1 + N) % (2 * N)], S[(B - 1 + N) % (2 * N)]);
            } 
        }else if (T == 2)
        {
            if (flag)
            {
                flag = false;   
            } else
            {
                flag = true;
            }     
        }   
    }
    
    if (flag)
    {
        cout << S << "\n";
    } else
    {
        for (int i = N; i < 2 * N; i++) {
           cout << S[i];
           }
        for (int i = 0; i < N; i++) {
           cout << S[i];
           }
    }
    
    
    
    return 0;
}