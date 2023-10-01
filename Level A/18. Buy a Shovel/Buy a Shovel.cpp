#include <iostream>
using namespace std;

int main() {
 int sh , ch , sum=1 ;
    cin>>sh>>ch;
    while(true){
        if ( (sh*sum)%10 == ch || (sh*sum)%10 == 0 ){
        cout<< sum ; // 1053%10 ==3 || 0
        return 0;
        }
        ++sum ;
    }
}