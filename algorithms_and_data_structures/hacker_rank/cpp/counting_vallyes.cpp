#include <iostream>
#include <vector>
#include <numeric>
using namespace std;

int countingValleys(const int &steps, const string &path)
{
    int level = 0, valleys = 0;

    for (const char &c : path)
    {
        if (c == 'U')
            level++;
        else if (c == 'D')
            level--;

        // Jezeli jestes na poziomie morza dzieki krokowi w gore to znaczy ze wyszedles z doliny
        if (level == 0 && c == 'U')
            valleys++;
    }

    return valleys;
}

int main()
{
    unsigned steps;
    string path;
    cin >> steps >> path;
    cout << countingValleys(steps, path) << '\n';
    return 0;
}
