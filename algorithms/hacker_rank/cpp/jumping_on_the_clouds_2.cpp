#include <iostream>
#include <vector>
using namespace std;
typedef unsigned short us;

// Complete the jumpingOnClouds function below.
us jumpingOnClouds(const vector<us> &c, const us &k)
{
    us e = 100;
    us n = c.size();
    us index = 0;

    while (e != 0)
    {
        --e;
        index = (index + k) % n;
        if (c.at(index) == 1)
            e -= 2;
        if (index == 0)
            break;
    }

    return e;
}

int main()
{
    us n, k;
    cin >> n >> k;
    vector<us> clouds(n);

    for (us &val : clouds)
        cin >> val;

    cout << jumpingOnClouds(clouds, k) << '\n';
    return 0;
}