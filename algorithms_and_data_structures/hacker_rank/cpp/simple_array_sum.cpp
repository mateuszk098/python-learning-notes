#include <iostream>
using namespace std;

int main(int argc, char *argv[])
{
    int n;
    cin >> n;
    int tmp, sum = 0;

    for (unsigned i = 0; i < n; i++)
    {
        cin >> tmp;
        sum += tmp;
    }

    cout << sum << '\n';

    return 0;
}