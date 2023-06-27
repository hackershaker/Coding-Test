// https://www.acmicpc.net/problem/2163
#include <unordered_map>
#include <cstdio>
#include <algorithm>
using namespace std;

int memo[301][301];

int divide(int n, int m)
{
    if (memo[n][m] >= 0)
        return memo[n][m];
    if (n == 1 || m == 1)
    {
        memo[n][m] = n * m - 1;
        return memo[n][m];
    }

    int answer = 100000;
    for (int i = 1; i < n; i++)
    {
        answer = min(answer, divide(i, m) + divide(n - i, m) + 1);
    }
    for (int j = 1; j < m; j++)
    {
        answer = min(answer, divide(n, j) + divide(n, m - j) + 1);
    }
    memo[n][m] = answer;
    return answer;
}

int main()
{
    fill(memo[0], memo[301], -1);
    memo[0][0] = 1;
    int n, m;
    scanf("%d %d", &n, &m);
    printf("%d", divide(n, m));
}