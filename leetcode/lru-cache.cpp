// https://leetcode.com/problems/lru-cache/
#include <bits/stdc++.h>
using namespace std;

class Node
{
public:
    int key, val;
    Node *prev, *next;

    Node(){};
    Node(int x, int y)
    {
        key = x;
        val = y;
        prev = next = nullptr;
    };
    Node(int x, int y, Node *p, Node *n)
    {
        key = x;
        val = y;
        prev = p;
        next = n;
    };
};

class DLL
{
public:
    Node *startDummy = new Node(-1, -1);
    Node *endDummy = new Node(-1, -1);
    unordered_map<int, Node *> dict;

    Node *getHead()
    {
        return startDummy->next;
    }
    Node *getTail()
    {
        return endDummy->prev;
    }
    void addFront(int key, int value)
    {
        Node *node = new Node(key, value, nullptr, nullptr);
        if (!dict.size())
        {
            node->next = endDummy;
            node->prev = startDummy;
            startDummy->next = node;
            endDummy->prev = node;
            dict[key] = node;
        }
        else if (dict.count(key))
        {
            findKey(key);
            auto head = getHead();
            head->val = value;
        }
        else
        {
            auto head = getHead();
            node->next = head;
            node->prev = startDummy;
            head->prev = node;
            startDummy->next = node;
            dict[key] = node;
        }
    }
    Node *deleteNode(int key)
    {
        if (!dict.count(key))
            return nullptr;
        auto node = dict[key];
        node->next->prev = node->prev;
        node->prev->next = node->next;
        dict.erase(node->key);
        return node;
    }
    int size() { return dict.size(); }
    int findKey(int key)
    {
        if (!dict.count(key))
            return -1;
        auto node = deleteNode(key);
        addFront(node->key, node->val);
        return dict[node->key]->val;
    }
};

class LRUCache
{
public:
    int maxSize;
    DLL dll;

    LRUCache(int capacity)
    {
        maxSize = capacity;
    }

    int get(int key)
    {
        return dll.findKey(key);
    }

    void put(int key, int value)
    {
        dll.addFront(key, value);
        if (dll.size() > maxSize)
            dll.deleteNode(dll.getTail()->key);
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */