// https://www.acmicpc.net/problem/2468
#include <iostream>
#include <vector>
// https://www.acmicpc.net/problem/2468
#include <unordered_set>
#include <deque>

using namespace std;

int explore(vector<vector<int>> &board, int h)
{
    unordered_set<int> visited;
    vector<vector<int>> next = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
    int i, j, answer = 0;
    int n = board.size();
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < n; j++)
        {
            if (visited.find(i * n + j) != visited.end() || board[i][j] <= h)
                continue;
            deque<pair<int, int>> q = {{i, j}};
            while (!q.empty())
            {
                auto temp = q.front();
                q.pop_front();

                for (auto nx : next)
                {
                    int x = temp.first + nx[0], y = temp.second + nx[1];
                    if (0 <= x && x < n && 0 <= y && y < n && board[x][y] > h && visited.find(x * n + y) == visited.end())
                    {
                        visited.insert(x * n + y);
                        q.push_back(make_pair(x, y));
                    }
                }
            }
            answer += 1;
        }
    }
    return answer;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n, h, i, j, maxH = 0;
    cin >> n;
    vector<vector<int>> board(n, vector<int>(n, 0));
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < n; j++)
        {
            cin >> board[i][j];
            maxH = (maxH < board[i][j]) ? board[i][j] : maxH;
        }
    }
    int answer = 0;
    while (maxH--)
    {
        answer = max(answer, explore(board, maxH));
    }
    printf("%d\n", answer);
    return 0;
}