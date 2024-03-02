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

int ctoi(char c)
{
    if (c >= '0' && c <= '9')
    {
        return c - '0';
    }
    return 0;
}

int vector_finder(std::vector<int> vec, int number)
{
    auto itr = std::find(vec.begin(), vec.end(), number);
    size_t index = std::distance(vec.begin(), itr);
    if (index != vec.size())
    { // 発見できたとき
        return true;
    }
    else
    { // 発見できなかったとき
        return false;
    }
}

int main()
{
    string S;
    cin >> S;

    int N = S.size();
    vvi W(N + 1);

    for (int i = 0; i < N; i++)
    {
        if (i == 0)
        {
            W[4].push_back(ctoi(S[i]));
        }
        else if (i == 1)
        {
            W[3].push_back(ctoi(S[i]));
        }
        else if (i == 2)
        {
            W[5].push_back(ctoi(S[i]));
        }
        else if (i == 3)
        {
            W[2].push_back(ctoi(S[i]));
        }
        else if (i == 4)
        {
            W[4].push_back(ctoi(S[i]));
        }
        else if (i == 5)
        {
            W[6].push_back(ctoi(S[i]));
        }
        else if (i == 6)
        {
            W[1].push_back(ctoi(S[i]));
        }
        else if (i == 7)
        {
            W[3].push_back(ctoi(S[i]));
        }
        else if (i == 8)
        {
            W[5].push_back(ctoi(S[i]));
        }
        else if (i == 9)
        {
            W[7].push_back(ctoi(S[i]));
        }
    }

    if (S[0] == '0')
    {
        for (int i = 1; i < 6; i++)
        {
            for (int j = 1; j < 8; j++)
            {
                if (j - i >= 2)
                {
                    if (vector_finder(W[i], 1) and vector_finder(W[j], 1))
                    {
                        for (int k = i + 1; k < j; k++)
                        {
                            if (not vector_finder(W[k], 1))
                            {
                                cout << "Yes"
                                     << "\n";
                                exit(0);
                            }
                        }
                    }
                }
            }
        }
    }

    cout << "No"
         << "\n";

    return 0;
}