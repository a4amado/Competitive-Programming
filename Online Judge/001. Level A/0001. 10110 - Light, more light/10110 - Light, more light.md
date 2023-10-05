# 10110 - Light, more light

mabu switches lights

he walks back and forth [n] times
each time is called [i] he onlt toogles the swithces whose serial is dividable by [i]
He does not press any switch when coming back to his initial position
going back to the initial does not count



here is the problem text `There is man named ”mabu” for switching on-off light in our University. He switches on-off the lights
in a corridor. Every bulb has its own toggle switch. That is, if it is pressed then the bulb turns on.
Another press will turn it off. To save power consumption (or may be he is mad or something else)
he does a peculiar thing. If in a corridor there is n bulbs, he walks along the corridor back and forth
n times and in i-th walk he toggles only the switches whose serial is divisable by i. He does not press
any switch when coming back to his initial position. A i-th walk is defined as going down the corridor
(while doing the peculiar thing) and coming back again. Now you have to determine what is the final
condition of the last bulb. Is it on or off?
Input
The input will be an integer indicating the n’th bulb in a corridor. Which is less then or equals 232 −1.
A zero indicates the end of input. You should not process this input.
Output
Output ‘yes’ if the light is on otherwise ‘no’, in a single line.
Sample Input
3
6241
8191
0
Sample Output
no
yes
no`


hee is the code that solved it 
`
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

`



that code right that is calcuating if the number is a perfect square or no 
then what does that has to doo with the number of factors