#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

inline const int solveMeFirst(const int &a, const int &b) { return a + b; }

int main()
{
    int num1, num2, sum;
    cin >> num1 >> num2;
    sum = solveMeFirst(num1, num2);
    cout << sum;

    return 0;
}