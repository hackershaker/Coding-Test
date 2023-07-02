// https://www.acmicpc.net/board/view/25973
#include <cstdio>
#include <vector>
#include <unordered_set>
#include <deque>

using namespace std;

void solution(int r, int c)
{
    int board[r][c];
    int answer = 0;
    deque<pair<int, int>> stack;
    vector<pair<int, int>> adjacent = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}, {1, 1}, {1, -1}, {-1, 1}, {-1, -1}};

    for (int i = 0; i < r; i++)
    {
        for (int j = 0; j < c; j++)
        {
            scanf("%d", &board[i][j]);
        }
    }

    for (int i = 0; i < r; i++)
    {
        for (int j = 0; j < c; j++)
        {
            if (board[i][j] == 2 || board[i][j] == 0)
                continue;
            stack = {{i, j}};
            while (!stack.empty())
            {
                auto node = stack.front();
                stack.pop_front();

                for (auto next : adjacent)
                {
                    int x = next.first + node.first;
                    int y = next.second + node.second;
                    if (board[x][y] == 1 && 0 <= x && x < r && 0 <= y && y < c)
                    {
                        board[x][y] = 2;
                        stack.push_back({x, y});
                    }
                }
            }
            answer += 1;
        }
    }

    printf("%d\n", answer);
    return;
}

int main()
{
    while (1)
    {
        int w, h;
        scanf("%d %d", &w, &h);
        if (w == 0 && h == 0)
            break;
        else
        {
            solution(h, w);
        }
    }
    return 0;
}