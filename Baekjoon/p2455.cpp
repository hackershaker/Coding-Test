#include <cstdio>
#include <vector>

using namespace std;

int main()
{
    vector<pair<int, int>> train;
    int people = 0, answer = 0;

    for (int i = 0; i < 4; i++)
    {
        pair<int, int> p;
        scanf("%d %d", &p.first, &p.second);
        train.push_back(p);
    }

    for (auto t : train)
    {
        people = people - t.first + t.second;
        answer = max(answer, people);
    }
    printf("%d\n", answer);
    return 0;
}