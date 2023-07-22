// https://leetcode.com/problems/knight-probability-in-chessboard/
#include <bits/stdc++.h>
using namespace std;

class Solution
{
private:
    vector<vector<int>> next{
        {-1, -2},
        {-2, -1},
        {-2, 1},
        {-1, 2},
        {1, 2},
        {2, 1},
        {2, -1},
        {1, -2},
    };
    int length;

public:
    double knightProbability(int n, int k, int row, int column)
    {
        vector<vector<vector<double>>> memo(k + 1, vector<vector<double>>(n, vector<double>(n, -1.0)));
        length = n;
        if (k == 0)
            return 1.0;
        return remainsProbability(row, column, k, memo);
    }

    double remainsProbability(int r, int c, int move, vector<vector<vector<double>>> &memo)
    {
        if (memo[move][r][c] != -1)
            return memo[move][r][c];
        if (move == 1)
        {
            int possible = 0;
            for (auto n : next)
            {
                int x = r + n[0], y = c + n[1];
                if (0 <= x && x < length && 0 <= y && y < length)
                    possible += 1;
            }
            memo[1][r][c] = possible * 0.125;
            return memo[1][r][c];
        }
        double p = 0.0;
        for (auto n : next)
        {
            int x = r + n[0], y = c + n[1];
            if (0 <= x && x < length && 0 <= y && y < length)
                p += 0.125 * remainsProbability(r + n[0], c + n[1], move - 1, memo);
        }
        memo[move][r][c] = p;
        return p;
    }
};