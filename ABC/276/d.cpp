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

vector<long long> factorize(long long n){
    long long i=2;
    vector<long long> fct;
    while (i*i<=n){
        while (n%i==0){
            n/=i;
            fct.push_back(i);
        }
        i++;
    }
    if (n>1) fct.push_back(n);
    if (fct.size()==0) fct.push_back(1);
    return fct;
}

int vector_finder(std::vector<ll> vec, ll number) {
  auto itr = std::find(vec.begin(), vec.end(), number);
  size_t index = std::distance( vec.begin(), itr );
  if (index != vec.size()) { // 発見できたとき
    return true;
  }
  else { // 発見できなかったとき
    return false;
  }
}

int main() {
    ll N;
    cin >> N;
    vector<ll> a(N);
    for(int i = 0; i < N; i++) {
        cin >> a[i];
    }

    vvll check;

    vector<ll> c;

    vll check_2;

    copy(a.begin(), a.end(), back_inserter(check_2));

    std::sort(check_2.begin(), check_2.end());
    check_2.erase(std::unique(check_2.begin(), check_2.end()), check_2.end());

    if (check_2.size() == 1)
    {
        cout << 0 << "\n";
        exit(0);
    }
    
    for (int i = 0; i < N; i++)
    {
        check.push_back(factorize(a[i]));
    }

    if (vector_finder(a, 1))
    {
        for (int i = 0; i < N; i++)
        {
            check[i].push_back(1);
        }
        
    }
    
    
    for (int i = 0; i < check.size() - 1; i++)
    {
        if (i == 0)
        {
            vll a = check[i];
            vll b = check[i + 1];
            sort(a.begin(),a.end());
            sort(b.begin(),b.end());
            set_intersection(a.begin(), a.end(), b.begin(), b.end(), std::back_inserter(c));
        } else
        {
            vll a = c;
            vll b = check[i + 1];
            sort(a.begin(),a.end());
            sort(b.begin(),b.end());
            c = {};
            set_intersection(a.begin(), a.end(), b.begin(), b.end(), std::back_inserter(c));
        }
    }

    if (c.size() == 0)
    {
        cout << -1 << "\n";
    } else
    {
        int cnt = 0;

        for (int i = 0; i < N; i++)
        {
            cnt += check[i].size() - c.size();
        }

        if (vector_finder(a, 1))
        {
            for (int i = 0; i < N; i++)
            {
                if (a[i] == 1)
            {
                cnt -= 1;
            }
            }
            
            
        }
        
        
        cout << cnt << "\n";
    }
    
    
    
    return 0;
}