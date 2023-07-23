// https://www.acmicpc.net/problem/9093
#include <cstdio>

using namespace std;

void reverse()
{
    char str[1000] = {
        '\0',
    };
    scanf("%[^\n]s", str);
    getchar();

    int start = 0, end = 0, idx = 0;
    while (true)
    {
        if (str[idx] == ' ' or str[idx] == '\0')
        {
            end = idx - 1;
            for (int i = end; i >= start; i--)
                printf("%c", str[i]);
            printf(" ");
            if (str[idx] == '\0')
                return;
            start = idx + 1;
            idx += 1;
        }
        else
            idx++;
    }
}

int main()
{
    int t;
    scanf("%d", &t);
    getchar();
    while (t > 0)
    {
        reverse();
        t -= 1;
    }
}