// https://www.acmicpc.net/problem/11057
#include <cstdio>
#include <vector>

typedef long long ll;

using namespace std;

int main()
{
    vector<vector<ll>> memo;
    int n, i, j, k;
    scanf("%d", &n);
    memo.resize(10, vector<ll>(n + 1));

    for (k = 0; k <= 9; k++)
        memo[k][1] = k + 1;

    for (i = 2; i <= n; i++)
    {
        for (j = 0; j <= 9; j++)
        {
            if (j == 0)
                memo[j][i] += memo[j][i - 1];
            else
                memo[j][i] += memo[j][i - 1] + memo[j - 1][i];
            memo[j][i] %= 10007;
        }
    }

    printf("%d\n", memo[9][n]);
}