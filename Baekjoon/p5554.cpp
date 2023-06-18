// https://www.acmicpc.net/problem/5554
#include <iostream>

using namespace std;

int main()
{
    int a, b, c, d = 0;
    cin >> a;
    cin >> b;
    cin >> c;
    cin >> d;
    cout << (a + b + c + d) / 60 << endl;
    cout << (a + b + c + d) % 60 << endl;
}