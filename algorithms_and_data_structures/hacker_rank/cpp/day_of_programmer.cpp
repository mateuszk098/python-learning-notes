#include <iostream>
#include <sstream>
#include <vector>
#include <numeric>
using namespace std;

string dayOfProgrammer(const int &year)
{
    vector<int> months{31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    int tmp = 0;
    stringstream str;

    if (year >= 1919)
    {
        if (year % 400 == 0 || (year % 4 == 0 && year % 100 != 0))
            months.at(1) += 1;

        tmp = accumulate(months.begin(), months.begin() + 8, 0);
        tmp = 256 - tmp;
        str << tmp << '.' << "09" << '.' << year;
    }
    else if (1700 <= year && year <= 1917)
    {
        if (year % 4 == 0)
            months.at(1) += 1;

        tmp = accumulate(months.begin(), months.begin() + 8, 0);
        tmp = 256 - tmp;
        str << tmp << '.' << "09" << '.' << year;
    }
    else if (year == 1918)
    {
        tmp = accumulate(months.begin(), months.begin() + 8, 0);
        tmp = 256 + 13 - tmp;
        str << tmp << '.' << "09" << '.' << year;
    }

    return str.str();
}

int main()
{
    int year;
    cin >> year;
    cout << dayOfProgrammer(year) << '\n';

    return 0;
}