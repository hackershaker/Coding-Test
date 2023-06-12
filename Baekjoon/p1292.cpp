#include <iostream>
#include <cmath>

using namespace std;

int powerSum(int k)
{
    return (k * (k + 1) * (2 * k + 1)) / 6;
}

int main()
{
    int a, b;
    scanf("%d %d", &a, &b);
    a = a - 1;

    int a_num = pow(2 * a + 0.25, 0.5) - 0.5;
    int b_num = pow(2 * b + 0.25, 0.5) - 0.5;
    int sum_a = powerSum(a_num) + (a - (a_num * (a_num + 1)) / 2) * (a_num + 1);
    int sum_b = powerSum(b_num) + (b - (b_num * (b_num + 1)) / 2) * (b_num + 1);
    printf("%d", sum_b - sum_a);
}