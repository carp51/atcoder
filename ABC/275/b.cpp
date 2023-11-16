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
    vector<vector<char>> S(9, vector<char>(9));
    for(int i = 0; i < 9; i++) {
        for(int j = 0; j < 9; j++) {
            cin >> S[i][j];
        }
    }
    
    // {0, 1, ..., n-1} の部分集合の全探索
    for (int bit = 0; bit < (1<<9); ++bit) {
        vector<int> S;
        for (int i = 0; i < 9; ++i) {
            if (bit & (1<<i)) { // 列挙に i が含まれるか
                S.push_back(i);
            }
        }
    }
    
    return 0;
}