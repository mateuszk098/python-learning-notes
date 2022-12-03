#include <iostream>
#include <cmath>
using namespace std;

int squares(const int &a, const int &b)
{
    int counts = 0;
    int square = 0;

    // Podejscie sprytne
    // Jezeli juz znajdziemy pierwiastek to kolejne pierwiastki beda
    // tworzyc sekwencje, wystarczy obliczyc wiec podloge najwiekszej liczby na wejsciu
    // i sufit najmniejszej liczby na wejsciu i je odjac oraz uwzglednic te najmniejsza
    // Przykladowo mamy 3 4 5 6 7 8 9
    // Tylko 2 liczby spelniaja warunek tzn 4 i 9, obliczajac floor z b mamy 3,
    // obliczajac ceil z a mamy 2
    counts = floor(sqrt(b)) - ceil(sqrt(a)) + 1;

    // Podejscie naiwne
    // for (int i = a; i <= b; i++)
    // {
    //     int square = (int)sqrt(i);
    //     if (square * square == i)
    //         counts++;
    // }

    return counts;
}

int main()
{
    int a, b, cases;
    cin >> cases;

    for (int i = 0; i < cases; i++)
    {
        cin >> a >> b;
        cout << squares(a, b) << '\n';
    }

    return 0;
}