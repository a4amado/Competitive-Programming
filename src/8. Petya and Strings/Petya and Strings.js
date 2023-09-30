"use strict";
/**
 * name: Petya and Strings
 * link: https://codeforces.com/contest/112/problem/A
 */
Object.defineProperty(exports, "__esModule", { value: true });
const readline_1 = require("readline");
const rl = (0, readline_1.createInterface)({
    input: process.stdin,
    output: process.stdout,
    terminal: false,
});
let S1 = false;
let firstTotal = "";
let secondTotal = "";
rl.on("line", (line) => {
    var _a, _b;
    if (!S1) {
        firstTotal = line.toLowerCase().trim();
    }
    else {
        secondTotal = line.toLowerCase().trim();
    }
    if (S1) {
        for (let index = 0; index < firstTotal.length; index++) {
            const n1 = (_a = firstTotal[index]) === null || _a === void 0 ? void 0 : _a.toLowerCase();
            const n2 = (_b = secondTotal[index]) === null || _b === void 0 ? void 0 : _b.toLowerCase();
            // @ts-ignore
            if (n1 < n2) {
                process.stdout.write("-1");
                process.exit(0);
                // @ts-ignore
            }
            else if (n1 > n2) {
                process.stdout.write("1");
                process.exit(0);
            }
        }
        process.stdout.write("0");
        process.exit(0);
    }
    S1 = true;
});
