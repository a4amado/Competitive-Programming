#include <iostream>
#include <math.h>

using namespace std;


int kadane(int* a) {
    int max_sub = 0;
    int currunt_max = 0;
    for (int i = 0; i < 6; i++) { 
        // if curr < 0 return to z;
        currunt_max = max(currunt_max, 0);

        currunt_max = currunt_max + a[i];

        max_sub = max(max_sub, currunt_max);
    }
    return max_sub;
}

int main() {

    int *a = new int[6];
    a[0] = 4;
    a[1] = -1;
    a[2] = 2;
    a[3] = -7;
    a[4] = 3;
    a[5] =  4;



    


    cout << kadane(a) << endl;



    return 0;
}