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
    vector<int> P(N);
    for(int i = 0; i < N; i++) {
        cin >> P[i];
    }

    int count = 0;
    
    do {
        if (count == 1)
        {
            for (int i = 0; i < N; i++) {
               cout << P[i];
               if (i < N)cout << " ";
               else cout << endl;
               }

            exit(0);
        }
        count += 1;
        
    }while( prev_permutation(P.begin(), P.end()) );
    
    return 0;
}