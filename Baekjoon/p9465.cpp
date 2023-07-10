// https://www.acmicpc.net/problem/9465
#include <vector>
#include <cstdio>

using namespace std;

void sticker()
{
    int n, i, j;
    scanf("%d", &n);
    vector<vector<int>> board(2, vector<int>(n + 1));
    for (i = 0; i < 2; i++)
    {
        for (j = 1; j < n + 1; j++)
        {
            scanf("%d", &board[i][j]);
        }
    }

    for (j = 2; j < n + 1; j++)
    {
        for (i = 0; i < 2; i++)
        {
            board[i][j] += max(board[(i + 1) % 2][j - 1], board[(i + 1) % 2][j - 2]);
        }
    }

    printf("%d\n", max(board[0][n], board[1][n]));
}

int main()
{
    int T;
    scanf("%d", &T);
    while (T--)
    {
        sticker();
    }
    return 0;
}