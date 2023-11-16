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

int ctoi(char c) {
   if (c >= '0' && c <= '9') {
	   return c - '0';
   }
   return 0;
}

int main() {
    string N;
	cin >> N;

	string check = N;
	int ans = 1000;

    // {0, 1, ..., n-1} の部分集合の全探索
    for (int bit = 0; bit < (1<<N.size()); ++bit) {
        int S = 0;

		for (int i = 0; i < check.size(); i++)
		{
			S += ctoi(check[i]);
		}
		

		int count = 0;
        for (int i = 0; i < N.size(); ++i) {
            if (bit & (1<<i)) { // 列挙に i が含まれるか
                S -= ctoi(check[i]);
				count += 1;
            }	
        }

		if (S % 3 == 0 and count != check.size())
		{
			ans = min(ans, count);
		}
		
	}

	if (ans != 1000)
	{
		cout << ans << "\n";
	} else
	{
		cout << -1 << "\n";
	}
	
	
    return 0;
}