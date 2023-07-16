// https://www.acmicpc.net/problem/10798
#include <cstdio>
#include <vector>

using namespace std;

int main()
{
    char str[5][16] = {{
        0,
    }};

    for (int i = 0; i < 5; i++)
        scanf("%s", str[i]);

    vector<char> vertical;

    for (int j = 0; j < 16; j++)
    {
        for (int i = 0; i < 5; i++)
        {
            if (str[i][j] != ' ' && str[i][j] != '\0')
                vertical.push_back(str[i][j]);
        }
    }

    for (auto c : vertical)
        printf("%c", c);

    return 0;
}