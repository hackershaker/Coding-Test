// https://www.acmicpc.net/problem/11279
#include <vector>
#include <cstdio>

using namespace std;

class MaxHeap
{
private:
    vector<int> heap;

public:
    void insert(int x)
    {
        heap.push_back(x);
        int index = heap.size() - 1;
        while (index > 0)
        {
            int parent = (index - 1) / 2;
            if (heap[parent] >= heap[index])
            {
                break;
            }
            swap(heap, parent, index);
            index = parent;
        }
    }

    void pop()
    {
        if (heap.empty())
        {
            printf("0\n");
            return;
        }
        printf("%d\n", heap[0]);
        swap(heap, 0, heap.size() - 1);
        heap.pop_back();
        int index = 0;
        while (index < heap.size())
        {
            int child;
            int left = index * 2 + 1, right = index * 2 + 2;
            if (left < heap.size() && right < heap.size())
            {
                child = (heap[left] <= heap[right]) ? right : left;
            }
            else if (left < heap.size())
            {
                child = left;
            }
            else if (right < heap.size())
            {
                child = right;
            }
            else
            {
                break;
            }
            if (heap[child] <= heap[index])
                break;
            swap(heap, index, child);
            index = child;
        }
    }

    void swap(vector<int> &vec, int x, int y)
    {
        int temp = vec[x];
        vec[x] = vec[y];
        vec[y] = temp;
    }
};

int main()
{
    MaxHeap *heap = new MaxHeap();
    int n, x;
    scanf("%d", &n);
    while (n > 0)
    {
        scanf("%d", &x);
        if (x == 0)
        {
            heap->pop();
        }
        else
        {
            heap->insert(x);
        }
        n--;
    }
    return 0;
}