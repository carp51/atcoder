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
    vector<int> a(N);
    for(int i = 0; i < N; i++) {
        cin >> a[i];
    }

    int count = 0;

    //std::vector<int> v = { 5, 2, 1, 3, 4, 2, 2, 4, 5, 5 };
     
    sort(a.begin(), a.end());
    a.erase(unique(a.begin(), a.end()), a.end());

    sort(a.begin(),a.end());

    int trash = N - a.size();

    for (int i = 0; i < trash / 2; i++)
    {
        a.push_back(a.back() + 1);
    }
    

    if (a[0] != 1)
    {
        cout << 0 << "\n";  
        exit(0);
    }

    int dead = N;

    for (int i = 0; i < a.size() - 1; i++)
    {
        if (a[i + 1] - a[i] == 1)
        {
            count += 1;
        } else
        {
            if (2 * (a[i + 1] - a[i] - 1) < dead - i - 2)
            {
                count += a[i + 1] - a[i];
                dead -= 2 * (a[i + 1] - a[i] - 1);
            }
            
        }
        
        
    }
    
    
    cout << count << "\n";
    return 0;
}