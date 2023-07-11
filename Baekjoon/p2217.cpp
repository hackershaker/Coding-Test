#include <vector>
#include <cstdio>
#include <algorithm>

using namespace std;

int main()
{
    int i, n, answer = 0;
    vector<int> rope;
    scanf("%d", &n);
    for (i = 0; i < n; i++)
    {
        int temp;
        scanf("%d", &temp);
        rope.push_back(temp);
    }
    sort(rope.begin(), rope.end());

    for (i = 0; i < n; i++)
    {
        answer = max(answer, rope[i] * (n - i));
    }

    printf("%d\n", answer);
    return 0;
}