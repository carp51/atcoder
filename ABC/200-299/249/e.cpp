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
    vi check = {1,3,4,5,6,7,7,8,346,36,3,65,6345,6,3456,3456,43};
    for (int i = 0; i < check.size(); i++) {
       cout << check[i];
       if (i < check.size())cout << " ";
       else cout << endl;
       }
    
    return 0;
}