// https://www.acmicpc.net/problem/2493
#include <cstdio>
#include <deque>
#include <vector>

using namespace std;

int main()
{
    int n;
    scanf("%d", &n);
    vector<int> towers(n), answer(n);
    deque<int> stack;
    for (int i = 0; i < n; i++)
        scanf("%d", &towers[i]);

    for (int i = n - 1; i > -1; i--)
    {
        if (stack.empty() || (!stack.empty() && towers[i] < towers[stack.front()]))
            stack.push_front(i);
        else
        {
            while (!stack.empty() && towers[i] >= towers[stack.front()])
            {
                answer[stack.front()] = i + 1;
                stack.pop_front();
            }
            stack.push_front(i);
        }
    }

    for (auto t : answer)
        printf("%d ", t);
    return 0;
}