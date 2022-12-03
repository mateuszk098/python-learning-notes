#include <iostream>
using namespace std;
typedef unsigned short us;

int viralAdvertising(const us &n)
{
    int shared = 5;
    int liked = shared / 2;
    int cum = liked;

    for (us i = 2; i <= n; i++)
    {
        shared = liked * 3;
        liked = shared / 2;
        cum += liked;
    }

    return cum;
}

int main()
{
    us n;
    cin >> n;
    cout << viralAdvertising(n) << '\n';
}