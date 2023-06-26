// https://www.acmicpc.net/problem/18870

#include <vector>
#include <queue>
#include <cstdio>
#include <algorithm>
#include <unordered_map>

#define MAXNUM 1000000000
using namespace std;

int main()
{
    int n, comp = 0;
    int cur = MAXNUM + 1;
    vector<int> ords;
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        int temp;
        scanf("%d", &temp);
        ords.push_back(temp);
    }

    vector<int> orderedOrds(ords.size());
    unordered_map<int, int> dict;
    copy(ords.begin(), ords.end(), orderedOrds.begin());
    sort(orderedOrds.begin(), orderedOrds.end());

    for (auto k : orderedOrds)
    {
        if (cur > MAXNUM)
        {
            dict[k] = comp;
        }
        else if (k != cur)
        {
            comp += 1;
            dict[k] = comp;
        }
        cur = k;
    }

    for (auto ord : ords)
    {
        printf("%d ", dict[ord]);
    }
    return 0;
}