#include <iostream>
#include <math.h>
#include <cstdint>
#include <iomanip>

using namespace std;

typedef long double ll;

int main()
{

    int64_t n;
    cin >> n;

    if (n % 2 == 0)
    {

        cout << std::fixed << std::setprecision(0) << (ll)abs(ceil((ll)n / 2)) << endl;
        return 0;
    }

    int64_t a = -ceil((ll)n / 2);
    cout << std::fixed << std::setprecision(0) << a << endl;
    return 0;
}