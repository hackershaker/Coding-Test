#include <iostream>
#include <cmath>

using namespace std;

int computer()
{
    int a, b;
    cin >> a >> b;
    int result = 1;
    for (int i = 1; i <= b; i++)
    {
        result = (result * a) % 10;
    }
    return result == 0 ? 10 : result;
}

int main()
{
    int T;
    cin >> T;
    for (int i = 0; i < T; i++)
    {
        cout << computer() << endl;
    }
    return 0;
}
