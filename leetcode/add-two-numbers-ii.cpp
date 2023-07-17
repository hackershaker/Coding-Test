/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
#include <bits/stdc++.h>

using namespace std;

struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution
{
public:
    ListNode *addTwoNumbers(ListNode *l1, ListNode *l2)
    {
        vector<ListNode *> stack1, stack2;
        ListNode *head = nullptr;
        int carry = 0;
        while (l1 != nullptr)
        {
            stack1.push_back(l1);
            l1 = l1->next;
        }
        while (l2 != nullptr)
        {
            stack2.push_back(l2);
            l2 = l2->next;
        }

        while (true)
        {
            ListNode *node1 = nullptr, *node2 = nullptr;
            if (!stack1.empty())
            {
                node1 = stack1.back();
                stack1.pop_back();
            }
            if (!stack2.empty())
            {
                node2 = stack2.back();
                stack2.pop_back();
            }

            ListNode *l = new ListNode(0);
            if (node1 && node2)
            {
                l->val = (node1->val + node2->val + carry) % 10;
                l->next = head;
                carry = (node1->val + node2->val + carry) / 10;
                head = l;
            }
            else if (node1)
            {
                l->val = (node1->val + carry) % 10;
                l->next = head;
                carry = (node1->val + carry) / 10;
                head = l;
            }
            else if (node2)
            {
                l->val = (node2->val + carry) % 10;
                l->next = head;
                carry = (node2->val + carry) / 10;
                head = l;
            }
            else
                break;
        }

        if (carry)
        {
            ListNode *l = new ListNode(carry, head);
            head = l;
        }

        return head;
    }
};