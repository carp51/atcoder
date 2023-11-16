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

int bubblesort(int *array,int size){
    int count = 0;
	for(int i = 0; i < size; i++){
		for(int j = i + 1; j < size; j++){
			if(array[i] > array[j]){
				int number = array[i];
				array[i] = array[j];
				array[j] = number;
                count += 1;
			}
		}
	}
    return count;
}

int main() {
    string S;
    cin >> S;

    map<char, int> dic;
    for (int i = 0; i < S.size(); i++){dic[S[i]] = 0;}
    for (int i = 0; i < S.size(); i++){dic[S[i]] = i;}

    int check[S.size()];
    string At = "atcoder";

    for (int i = 0; i < S.size(); i++)
    {
        check[i] = dic[At[i]];
    }

    cout << bubblesort(check, S.size()) << "\n";
    
    return 0;
}