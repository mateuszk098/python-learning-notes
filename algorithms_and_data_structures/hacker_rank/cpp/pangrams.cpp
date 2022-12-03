#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

string pangrams(string s)
{
    transform(s.begin(), s.end(), s.begin(), [](unsigned char c)
              { return std::tolower(c); });

    int counts = 0;
    vector<char> c{'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                   'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};

    for (int i = 0; i < c.size(); i++)
    {
        for (int j = 0; j < s.length(); j++)
        {
            if (c.at(i) == s.at(j))
            {
                ++counts;
                break;
            }
        }
    }

    if (counts == c.size())
        return "pangram";

    return "not pangram";
}

int main()
{
    string s;
    getline(cin, s);
    cout << pangrams(s) << '\n';
    return 0;
}
