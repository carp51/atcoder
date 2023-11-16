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

vector<long long> divisor_enumetarion(long long n){
    vector<long long> divisors;
    for(long long i=1 ; i*i<=n ; i++){
        if(n%i == 0){
            divisors.push_back(i);
            if(i != n/i){
                divisors.push_back(n/i);
            }
        }
    }
    sort(divisors.begin(),divisors.end(),std::greater{});
    return divisors;
}
        

int main() {
    ll N;
    cin >> N;

    vll check = divisor_enumetarion(N);

    ll ans = 100000000000000;

    for (int i = 0; i < check.size(); i++)
    {
        ll max_num = max(to_string(check[i]).size(), to_string(N / check[i]).size());
        ans = min(ans, max_num);
    }

    cout << ans << "\n";
    
    return 0;
}