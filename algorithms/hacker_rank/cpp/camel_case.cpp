#include <iostream>
#include <algorithm>
using namespace std;

int camelcase(const string &s)
{
    int upper = count_if(s.begin(), s.end(), [](char c) { return isupper(c); });
    return upper + 1;
}

int main()
{
    string s;
    cin >> s;
    cout << camelcase(s) << '\n';

    return 0;
}
