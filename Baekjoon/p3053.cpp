#include <iostream>
#include <cmath>

using namespace std;

const double PI = acos(-1);

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    double r;
    cin >> r;

    cout.precision(6);
    cout << fixed;
    cout << PI * r * r << "\n";
    cout << 2 * r * r << "\n";
    return 0;
}