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

string f(string a) {
    sort(a.begin(),a.end(),std::greater{});
    int max_num = stoi(a);
    sort(a.begin(),a.end());
    int min_num = stoi(a);

    string tmp = to_string(max_num - min_num);
    return tmp;
}

int main() {
    string N;
    cin >> N;
    int K;
    cin >> K;

    for (int i = 0; i < K; i++)
    {
        N = f(N);
    }

    cout << N << "\n";

    return 0;
}