#include <cstdio>
#include <deque>
#include <vector>

using namespace std;

int main()
{
    int n, m, answer = 0;
    deque<int> deq;
    scanf("%d %d", &n, &m);
    deq.resize(n);
    for (int i = 1; i <= n; i++)
        deq[i - 1] = i;

    while (m--)
    {
        int target;
        scanf("%d", &target);

        int idx = 0;
        while (deq[idx] != target)
            idx++;

        int left = idx, right = deq.size() - idx;
        if (left <= right)
        {
            answer += left;
            while (left--)
            {
                int temp = deq.front();
                deq.pop_front();
                deq.push_back(temp);
            }
        }
        else
        {
            answer += right;
            while (right--)
            {
                int temp = deq.back();
                deq.pop_back();
                deq.push_front(temp);
            }
        }
        deq.pop_front();
    }

    printf("%d", answer);
}