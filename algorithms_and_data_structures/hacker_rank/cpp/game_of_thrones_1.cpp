#include <iostream>
using namespace std;

string gameOfThrones(const string &s)
{
    int count[256]{0};

    for (const char &c : s)
        ++count[c];

    int odd = 0;
    for (int i = 0; i < 256; i++)
    {
        if (count[i] % 2 != 0)
            ++odd;

        if (odd > 1)
            return "NO";
    }

    return "YES";
}

int main()
{
    string s;
    cin >> s;
    cout << gameOfThrones(s) << '\n';
    return 0;
}
