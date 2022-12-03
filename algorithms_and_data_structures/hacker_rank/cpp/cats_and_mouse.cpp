#include <iostream>
#include <sstream>
using namespace std;

string catAndMouse(const int &x, const int &y, const int &z)
{
    if (abs(z - y) > abs(z - x))
        return "Cat A";
    else if (abs(z - y) < abs(z - x))
        return "Cat B";
    else
        return "Mouse C";
}

int main()
{
    int n, x, y, z;
    cin >> n;

    for (int i = 0; i < n; i++)
    {
        cin >> x >> y >> z;
        cout << catAndMouse(x, y, z) << '\n';
    }

    return 0;
}
