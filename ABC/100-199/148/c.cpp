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

//値が大きそうならll
ll gcd(ll a, ll b){
  if(a%b == 0){
    return b;
  }else{
    return gcd(b, a%b);
  }
}

ll lcm(ll a, ll b){
  return a*b / gcd(a, b);
}
        
        

int main() {
    ll A, B;
    cin >> A >> B;

    cout << lcm(A, B) << "\n";
        
    return 0;
}