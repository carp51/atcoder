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
    int N, K;
    cin >> N >> K;
    vector<string> S(N);
    for(int i = 0; i < N; i++) {
        cin >> S[i];
    }

    int ans = -10;
    
    // {0, 1, ..., n-1} の部分集合の全探索
    for (int bit = 0; bit < (1<<N); ++bit) {
        map<char, int> dic;
        for (int i = 0; i < N; ++i) {
            if (bit & (1<<i)) { // 列挙に i が含まれるか
                for (int j = 0; j < S[i].size(); j++){dic[S[i][j]] += 1;}
            }
        }

        if (dic.size() == 0){continue;}

        int tmp = 0;

        for(auto i = dic.begin(); i != dic.end(); ++i){
            int v = i->second;
            if (v == K)
            {
                tmp += 1;
            }
        }

        ans = max(ans, tmp);
    }

    cout << ans << "\n";
    
    return 0;
}