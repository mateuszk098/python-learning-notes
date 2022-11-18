#include <iostream>
#include <algorithm>
using namespace std;

long repeatedString(const string &s, const long &n)
{
    int sLenght = s.length();
    long fullRepeats = n / sLenght;
    int remainder = n % sLenght;
    long count = count_if(s.begin(), s.end(), [](char c) { return c == 'a'; });
    count *= fullRepeats;
    count += count_if(s.begin(), s.begin() + remainder, [](char c) { return c == 'a'; });

    return count;
}

int main()
{
    string s;
    cin >> s;

    long n;
    cin >> n;

    cout << repeatedString(s, n) << "\n";

    return 0;
}