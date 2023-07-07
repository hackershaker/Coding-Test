#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    int maxConsecutiveAnswers(string answerKey, int k)
    {
        int start = 0, end = 0, t = 0, f = 0, answer = 0;
        for (end = 0; end < answerKey.size(); end++)
        {
            (answerKey[end] == 'T') ? t += 1 : f += 1;
            if (t <= k || f <= k)
                answer = max(answer, t + f);
            else
            {
                while (t > k && f > k)
                {
                    (answerKey[start] == 'T') ? t -= 1 : f -= 1;
                    start++;
                }
            }
        }
        return answer;
    }
};