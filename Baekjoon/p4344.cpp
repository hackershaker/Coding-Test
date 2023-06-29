#include <cstdio>
#include <iostream>
#include <sstream>
#include <vector>

using namespace std;

int main()
{
    int C;
    scanf("%d\n", &C);
    for (int i = 0; i < C; i++)
    {
        string s;
        getline(cin, s);
        istringstream iss(s);
        vector<float> students;
        float sum = 0, n = 0, avg;
        string word;
        while (iss >> word)
        {
            if (n == 0)
                n = (float)stoi(word);
            else
            {
                float score = (float)stoi(word);
                sum += score;
                students.push_back(score);
            }
        }

        avg = sum / n;
        float upAvg = 0;
        for (auto student : students)
        {
            if (student > avg)
                upAvg += 1;
        }
        printf("%.3f%\n", (upAvg / n) * 100);
    }
    return 0;
}