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

double f(vi CA, vi CB)
{
    int CA_CB = CA[0] * CB[0] + CA[1] * CB[1];
    double a_CA = sqrt(CA[0] * CA[0] + CA[1] * CA[1]);
    double a_CB = sqrt(CB[0] * CB[0] + CB[1] * CB[1]);

    double cosBCA = CA_CB / (a_CA * a_CB);

    return acos(cosBCA);
}

int g(vi A, vi B, vi C)
{
    return (A[0] * B[1] + B[0] * C[1] + C[0] * A[1] - A[1] * B[0] - B[1] * C[0] - C[1] * A[0]);
}

int main()
{
    vector<vector<int>> c(4, vector<int>(2));
    for (int i = 0; i < 4; i++)
    {
        for (int j = 0; j < 2; j++)
        {
            cin >> c[i][j];
        }
    }

    for (int i = 0; i < 4; i++)
    {
        vi CA, CB;
        int S;
        if (i == 0)
        {
            CA = {c[1][0] - c[0][0], c[1][1] - c[0][1]};
            CB = {c[3][0] - c[0][0], c[3][1] - c[0][1]};
            S = g(c[3], c[0], c[1]);
        }
        else if (i == 1)
        {
            CA = {c[2][0] - c[1][0], c[2][1] - c[1][1]};
            CB = {c[0][0] - c[1][0], c[0][1] - c[1][1]};
            S = g(c[0], c[1], c[2]);
        }
        else if (i == 2)
        {
            CA = {c[3][0] - c[2][0], c[3][1] - c[2][1]};
            CB = {c[1][0] - c[2][0], c[1][1] - c[2][1]};
            S = g(c[1], c[2], c[3]);
        }
        else if (i == 3)
        {
            CA = {c[0][0] - c[3][0], c[0][1] - c[3][1]};
            CB = {c[2][0] - c[3][0], c[2][1] - c[3][1]};
            S = g(c[2], c[3], c[0]);
        }

        if (S < 0)
        {
            cout << "No"<< "\n";
            exit(0);
        }
    }

    cout << "Yes"<< "\n";
    return 0;
}