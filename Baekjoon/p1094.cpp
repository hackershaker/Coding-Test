#include <iostream>
#include <queue>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int x, sum = 64;
    cin >> x;
    priority_queue<int, vector<int>, greater<int>> heap;
    heap.push(64);

    while (sum != x)
    {
        int stick = heap.top();
        int half = stick / 2;
        heap.pop();
        if (sum - half >= x)
        {
            sum -= half;
            heap.push(half);
        }
        else
        {
            heap.push(half);
            heap.push(half);
        }
    }
    cout << heap.size() << "\n";
}