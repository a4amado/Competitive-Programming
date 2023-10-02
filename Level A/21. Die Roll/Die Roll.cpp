#include <iostream>
using namespace std;
 
int main() {
    int Yakko, Wakko;
    cin >> Yakko >> Wakko;

    int bigger = 0;
    if (Yakko > Wakko) {
        bigger = Yakko;
    } else {
        bigger = Wakko;
    };
    int probability = (6 - (bigger));



    

    cout << abs(probability - 6) << 6 <<endl;
    return 0;
}
