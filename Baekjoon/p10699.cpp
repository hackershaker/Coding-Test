#include <iostream>
#include <ctime>
#include <iomanip>

using namespace std;

int main()
{
    time_t currentTime = time(nullptr);
    struct tm *t = localtime(&currentTime);
    cout << t->tm_year + 1900 << "-";
    cout << setfill('0') << setw(2) << t->tm_mon + 1;
    cout << "-" << t->tm_mday;
    return 0;
}