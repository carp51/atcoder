#include <bits/stdc++.h>
using namespace std;

using ull = unsigned long long;
using ll = long long;
using vi = vector<ll>;
using vl = vector<long>;
using vll = vector<long long>;
using vvi = vector<vi>;
using vvl = vector<vl>;
using vvll = vector<vll>;
using vs = vector<string>;
using pii = pair<ll, ll>;

ll ntodec(const char c){
    switch(c){
        case '0': return 0;
        case '1': return 1;
        case '2': return 2;
        case '3': return 3;
        case '4': return 4;
        case '5': return 5;
        case '6': return 6;
        case '7': return 7;
        case '8': return 8;
        case '9': return 9;
        case 'A': return 10;
        case 'B': return 11;
        case 'C': return 12;
        case 'D': return 13;
        case 'E': return 14;
        case 'F': return 15;
        case 'G': return 16;
        case 'H': return 17;
        case 'I': return 18;
        case 'J': return 19;
        case 'K': return 20;
        case 'L': return 21;
        case 'M': return 22;
        case 'N': return 23;
        case 'O': return 24;
        case 'P': return 25;
        case 'Q': return 26;
        case 'R': return 27;
        case 'S': return 28;
        case 'T': return 29;
        case 'U': return 30;
        case 'V': return 31;
        case 'W': return 32;
        case 'X': return 33;
        case 'Y': return 34;
        case 'Z': return 35;
        default : return -1;
    }
}

char decton(const ll n){
    switch(n){
        case 0: return '0';
        case 1: return '1';
        case 2: return '2';
        case 3: return '3';
        case 4: return '4';
        case 5: return '5';
        case 6: return '6';
        case 7: return '7';
        case 8: return '8';
        case 9: return '9';
        case 10: return 'A';
        case 11: return 'B';
        case 12: return 'C';
        case 13: return 'D';
        case 14: return 'E';
        case 15: return 'F';
        case 16: return 'G';
        case 17: return 'H';
        case 18: return 'I';
        case 19: return 'J';
        case 20: return 'K';
        case 21: return 'L';
        case 22: return 'M';
        case 23: return 'N';
        case 24: return 'O';
        case 25: return 'P';
        case 26: return 'Q';
        case 27: return 'R';
        case 28: return 'S';
        case 29: return 'T';
        case 30: return 'U';
        case 31: return 'V';
        case 32: return 'W';
        case 33: return 'X';
        case 34: return 'W';
        case 35: return 'Z';
        default : return '\0';
    }
}

inline long long pow_ll(long long x, long long n){
    long long ret = x;
    if(n==0) return 1;
    for(long long i=1; i<n; i++){
        ret *= x;
    }
    return ret;
}

//n 進数で表現された数値を文字列 str で受け取り、m 進数に直して文字列で出力する。
string n_ary(string str, ll n, ll m){
    unsigned long tmp = 0;
    string ret;

    for(ll i=0; i<str.length(); i++){
        tmp += (unsigned long) ntodec(str[str.length()-1-i]) * pow_ll(n, i);
    }

    if(tmp==0) return "0";
    while(tmp!=0){
        ret = decton(tmp%m) + ret;
        tmp/=m;
    }
    return ret;
}
        

int main() {
    string N;
    cin >> N;

    string nisin = n_ary(N, 10, 2);

    vi check;

    for (ll i = 0; i < nisin.size(); i++)
    {
        if (nisin[i] == '1')
        {
            check.push_back(i);
        }
        
    }

    vll ans = {};
    
    // {0, 1, ..., n-1} の部分集合の全探索
    for (ll bit = 0; bit < (1<<check.size()); ++bit) {
        vector<ll> S;
        string new_nisin = nisin;
        for (ll i = 0; i < check.size(); ++i) {
            if (bit & (1<<i)) { // 列挙に i が含まれるか
                new_nisin.replace(check[i], 1, "0");
                ans.push_back(stoll(n_ary(new_nisin, 2, 10)));
            }
        }
    }

    std::sort(ans.begin(), ans.end());
    ans.erase(std::unique(ans.begin(), ans.end()), ans.end());

    //sort(ans.begin(),ans.end());

    for (ll i = 0; i < ans.size(); i++)
    {
        cout << ans[i] << "\n";
    }
    
    cout << N << "\n";
    return 0;
}