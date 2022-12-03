#include <iostream>
using namespace std;

int libraryFine(const int &d1, const int &m1, const int &y1, const int &d2, const int &m2, const int &y2)
{
    if (y1 > y2)
        return 10000;
    if (y1 < y2)
        return 0;

    if (m1 > m2)
        return (m1 - m2) * 500;
    if (m1 < m2)
        return 0;

    if (d1 > d2)
        return (d1 - d2) * 15;
    if (d1 < d2)
        return 0;

    return 0;
}

int main()
{
    int d1, m1, y1;
    int d2, m2, y2;
    cin >> d1 >> m1 >> y1;
    cin >> d2 >> m2 >> y2;
    cout << libraryFine(d1, m1, y1, d2, m2, y2);
    return 0;
}