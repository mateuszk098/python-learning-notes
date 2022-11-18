#include <iostream>
#include <string>
using namespace std;

string timeConversion(const string &s)
{
    string result = s;
    string s_tmp = "";
    unsigned short tmp = 0;
    tmp = stoi(result.substr(0, 2));

    if (result.substr(8, 2) == "PM" && tmp != 12)
        tmp += 12;
    else if (result.substr(8, 2) == "AM" && tmp == 12)
        tmp = 0;

    result.replace(0, 2, to_string(tmp));

    if (tmp < 10)
        s_tmp = '0' + result.substr(0, 7);
    else
        s_tmp = result.substr(0, 8);

    return s_tmp;
}

int main()
{
    string s;
    getline(cin, s);
    cout << timeConversion(s) << '\n';

    return 0;
}