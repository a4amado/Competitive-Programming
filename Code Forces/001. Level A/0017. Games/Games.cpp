#include <iostream>
#include <cstring>
#include <cstdlib>
#include <vector>

using namespace std;



int main() {
    
    int teams;
    cin >> teams;
    int res = 0;

    int home[teams], guest[teams];

    for (int i = 0; i < teams; i++) {
        cin >> home[i] >> guest[i];
    };

    for (int i = 0; i < teams; i++) {
        for (int j = 0; j < teams; j++) {
            if (home[i] == guest[j]) {
                res++;
            }
        }
    }


    cout << res << endl;
    return 0;
};