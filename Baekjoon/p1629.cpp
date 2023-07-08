// https://www.acmicpc.net/problem/1629
#include <cstdio>
typedef long long int int64_t;

using namespace std;

int64_t remainder(int64_t x, int64_t y, int64_t m)
{
    if (y == 1)
        return x % m;
    int64_t result = remainder(x, y / 2, m);
    x %= m;
    if (y % 2 == 0)
    {
        return (result * result) % m;
    }
    else
    {
        return (((result * result) % m) * x) % m;
    }
}

int main()
{
    int64_t a, b, c, temp = 1;
    scanf("%llu", &a);
    scanf("%llu", &b);
    scanf("%llu", &c);

    printf("%llu\n", remainder(a, b, c));
    return 0;
}

/*
3 12 7
1
3 5 7
5
2 45 1327
419
10 10 3
0
9 10 4
1
9 10 5
1
9 10 6
3
1 1 4
1
2 3 8
2147483647 2147483647 100001
7569
2147483646 2147483646 2147483647
7569
2147483645 3 2147483647
2147483639
*/