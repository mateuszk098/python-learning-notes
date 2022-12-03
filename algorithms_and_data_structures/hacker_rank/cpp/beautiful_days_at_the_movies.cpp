#include <iostream>
#include <algorithm>
#include <vector>
#include <numeric>
#include <cmath>
#include <string>
using namespace std;

int beautifulDays(const int &i, const int &j, const int &k)
{
    vector<int> days(j - i + 1);
    iota(days.begin(), days.end(), i); // Fill vector by consecutive numbers i, i+1, i+2, ..., j

    int counter = 0;
    string str;

    for (const int &value : days)
    {
        str = to_string(value);
        reverse(str.begin(), str.end());
        str.erase(0, str.find_first_not_of('0')); // remove leading 0 from string
        if (abs(value - stoi(str)) % k == 0)
            ++counter;
    }

    return counter;
}

int main()
{
    int i, j, k;
    cin >> i >> j >> k;
    cout << beautifulDays(i, j, k) << '\n';
    return 0;
}