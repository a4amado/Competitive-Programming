/**
 * name: Gravity Flip
 * link: https://codeforces.com/contest/405/problem/A
 */

import { createInterface } from "readline";

const rl = createInterface({
    input: process.stdin,
    output: process.stdout,
    terminal: false,
});

let columns = 0;
let arr: number[] = [];

rl.on("line", (line) => {
    if (columns === 0) {
        columns = parseInt(line, 10);
    } else if (arr.length === 0) {
        arr = line.split(" ").map((e) => parseInt(e, 10));
        arr.sort((a, b) => {
            if (a > b) {
                return 1;
            } else if (b > a) {
                return -1;
            } else {
                return 0;
            }
        });
        process.stdout.write(arr.join(" "));
        process.exit();
    }
});
