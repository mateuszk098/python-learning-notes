#include <iostream>
#include <cmath>
using namespace std;

string kangaroo(int x1, const int &v1, int x2, const int &v2)
{
    // x1 + jumps * v1 = x2 + jumps * v2
    double jumps = 0.;

    if (v1 != v2)
        jumps = (double)(x2 - x1) / (v1 - v2);
    else
        return "NO";

    if (floor(jumps) == jumps && jumps > 0)
        return "YES";

    return "NO";
}

int main()
{
    int x1, v1, x2, v2;
    cin >> x1 >> v1 >> x2 >> v2;
    cout << kangaroo(x1, v1, x2, v2);
    return 0;
}
