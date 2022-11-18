#include <iostream>
using namespace std;

int alternatingCharacters(string s)
{
    int del = 0;

    for (int i = 0; i < s.length() - 1; i++)
    {
        if (s[i] == s[i + 1])
            ++del;
    }

    return del;
}

int main()
{
    int n;
    cin >> n;

    for (int i = 0; i < n; i++)
    {
        string s;
        cin >> s;
        cout << alternatingCharacters(s) << '\n';
    }

    return 0;
}