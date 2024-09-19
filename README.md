
## advice about DP from [PiyushRaj27](https://leetcode.com/u/PiyushRaj27/)
```
I am in no way entitled to give advice but this is what i do:

Generally whenever we see problem containing permutation and combination (basically counting) or minimizing or maximizing we can use DP to solve it.

    First try to get recursive solution. If you are comfortable with that, it should be easy from here.
    Try to find if you get some overlap in the recursion tree. I mean try to find, if you will land on same parameters for your recursive function via multiple paths. If yes then start memoizing every solution you create in a DP (which can be an array for hash map of some sort). This should be good enough for most of the problems.
    To solve via tabulation, try to find the base cases and then continue building from that to your problem. Store the intermediate results.

Practice would really help with DP. Mostly DP is applicable in Array questions and string questions. Try to solve some 1D DP and then 2D DP and then 3D DP.

Hope this helps.
```