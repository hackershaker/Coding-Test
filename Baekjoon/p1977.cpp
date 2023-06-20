// https://www.acmicpc.net/problem/1977
#include <cmath>
#include <cstdio>
#include <algorithm>

using namespace std;

int main()
{
    int m, n, sum = 0, maxValue = 10001;
    scanf("%d", &m);
    scanf("%d", &n);
    for (int i = ceil(sqrt(m)); i < floor(sqrt(n)) + 1; i++)
    {
        sum += i * i;
        maxValue = min(maxValue, i * i);
    }
    if (!sum)
    {
        printf("-1");
        return 0;
    }
    printf("%d\n", sum);
    printf("%d\n", maxValue);
    return 0;
}