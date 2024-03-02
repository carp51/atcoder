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
    vector<pair<int,string>> check(N);
    for (int i = 0; i < N; i++)
    {
        cin >> check[i].second >> check[i].first;
    }

    sort(check.begin(),check.end(),std::greater{});

    cout << check[1].second << "\n";
    return 0;
}