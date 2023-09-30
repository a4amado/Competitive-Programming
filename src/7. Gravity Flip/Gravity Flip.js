"use strict";
/**
 * name: Gravity Flip
 * link: https://codeforces.com/contest/405/problem/A
 */
Object.defineProperty(exports, "__esModule", { value: true });
const readline_1 = require("readline");
const rl = (0, readline_1.createInterface)({
    input: process.stdin,
    output: process.stdout,
    terminal: false,
});
let columns = 0;
let arr = [];
rl.on("line", (line) => {
    if (columns === 0) {
        columns = parseInt(line, 10);
    }
    else if (arr.length === 0) {
        arr = line.split(" ").map((e) => parseInt(e, 10));
        arr.sort((a, b) => {
            if (a > b) {
                return 1;
            }
            else if (b > a) {
                return -1;
            }
            else {
                return 0;
            }
        });
        process.stdout.write(arr.join(" "));
        process.exit();
    }
});
