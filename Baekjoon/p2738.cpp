// https://www.acmicpc.net/problem/2738
#include <vector>
#include <cstdio>
#include <iostream>
#include <istream>
#include <sstream>

using namespace std;

int main()
{
    int n, m, i, j, temp;
    string s;
    scanf("%d %d\n", &n, &m);

    vector<vector<int>> matrix(n, vector<int>(m, 0));
    for (i = 0; i < n; i++)
    {
        getline(cin, s);
        istringstream iss(s);
        for (j = 0; j < m; j++)
        {
            iss >> temp;
            matrix[i][j] += temp;
        }
    }
    for (i = 0; i < n; i++)
    {
        getline(cin, s);
        istringstream iss(s);
        for (j = 0; j < m; j++)
        {
            iss >> temp;
            matrix[i][j] += temp;
        }
    }

    for (i = 0; i < n; i++)
    {
        for (j = 0; j < m; j++)
        {
            if (j < m - 1)
                printf("%d ", matrix[i][j]);
            else
                printf("%d\n", matrix[i][j]);
        }
    }
}