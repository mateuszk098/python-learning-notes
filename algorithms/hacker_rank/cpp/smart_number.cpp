#include <iostream>
#include <cmath>
using namespace std;

// Liczba ktora ma nieparzysta liczbe dzielnikow to liczba kwadratowa
bool is_smart_number(const int &num)
{
    // Czyli trzeba obliczyc pierwiastek liczby i sprawdzic czy kwadrat pierwiastka jest rowny liczbie
    int val = (int)sqrt(num);
    if (val * val == num)
        return true;
    return false;
}

int main()
{

    int test_cases;
    cin >> test_cases;
    int num;
    for (int i = 0; i < test_cases; i++)
    {
        cin >> num;
        bool ans = is_smart_number(num);
        if (ans)
        {
            cout << "YES" << endl;
        }
        else
            cout << "NO" << endl;
    }
    return 0;
}
