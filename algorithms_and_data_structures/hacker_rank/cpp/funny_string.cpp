#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

string funnyString(string s)
{
    string tmp = s;
    reverse(tmp.begin(), tmp.end());

    for (int i = 0; i < s.size() - 1; i++)
    {
        int abs1 = abs(s[i] - s[i + 1]);
        int abs2 = abs(tmp[i] - tmp[i + 1]);

        if (abs1 != abs2)
            return "Not Funny";
    }

    return "Funny";
}

int main()
{
    int n;
    cin >> n;

    for (int i = 0; i < n; i++)
    {
        string str;
        cin >> str;
        cout << funnyString(str) << '\n';
    }

    return 0;
}