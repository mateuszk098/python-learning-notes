#include <iostream>
#include <sstream>
#include <iomanip>
using namespace std;

void staircase(const int &n)
{
    for (int i = 1; i <= n; i++)
    {
        string h(i, '#');
        string s(n - i, ' ');
        cout << s << h << '\n';
    }
}

// void staircase(const int &n)
// {
//     stringstream ss;

//     for (int i = 1; i <= n; i++)
//     {
//         cout << right << setw(n) << setfill(' ');

//         for (int j = 0; j < i; j++)
//             ss << '#';

//         cout << ss.str() << '\n';
//         ss.str("");
//     }
// }

int main()
{
    int n;
    cin >> n;
    staircase(n);

    return 0;
}