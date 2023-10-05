/*
 █ █  █▀▀▄  ▀▀▀█
  █   █░▒█    █
 █ █  █▄▄▀  ▄█▄▄▄
 */
//XDZ --> by Mr.X ;
#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <set>
#include <vector>
#include <map>
#include <list>
#include <deque>
#include <math.h>
#include <cstring>
#include <string.h>
#include <iomanip>
#include <stdlib.h>
#include <sstream>
#include <fstream>
using namespace std ;
int main(){
    unsigned int n ;
    while ( cin >> n && n != 0 ) {
        unsigned int sq = ( int ) sqrt( n ) ;
        cout << ( sq * sq == n ? "yes\n" : "no\n" ) ;
    }
    return 0 ;
}
