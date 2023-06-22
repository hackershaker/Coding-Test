// https://www.acmicpc.net/problem/1655
#include <stdio.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <cmath>
#include <string>

using namespace std;

void printpq(priority_queue<int> pq)
{
    if (pq.empty())
    {
        printf("EMPTY\n");
        return;
    }

    priority_queue<int> tmp = pq;
    while (!tmp.empty())
    {
        printf("%d ", tmp.top());
        tmp.pop();
    }
    printf("\n");
}

int main()
{
    int n, u, target, temp;
    int *mid = nullptr;
    scanf("%d", &n);
    priority_queue<int, vector<int>> leftHeap, rightHeap;
    for (u = 1; u < n + 1; u++)
    {
        scanf("%d", &target);
        // 지금까지 말한 수가 짝수일 때
        if (mid == nullptr)
        {
            mid = new int(target);
            if (!leftHeap.empty() && *mid < leftHeap.top())
            {
                temp = leftHeap.top();
                leftHeap.pop();
                leftHeap.push(*mid);
                *mid = temp;
            }
            if (!rightHeap.empty() && *mid > -rightHeap.top())
            {
                temp = -rightHeap.top();
                rightHeap.pop();
                rightHeap.push(-*mid);
                *mid = temp;
            }
            printf("%d\n", *mid);
        }
        // 지금까지 말한 수가 홀수일 때
        else
        {
            if (*mid <= target)
            {
                leftHeap.push(*mid);
                rightHeap.push(-target);
            }
            else
            {
                rightHeap.push(-*mid);
                leftHeap.push(target);
            }
            mid = nullptr;
            printf("%d\n", leftHeap.top());
        }
        /*
        printf("leftheap: ");
        printpq(leftHeap);
        printf("mid: %s\n", (mid == nullptr) ? "null" : to_string(*mid).c_str());
        printf("rightheap: ");
        printpq(rightHeap);
        */
    }
    return 0;
}

/*
6
3
3
3
4
4
4
*/
/*
3
-1
-2
-1
*/