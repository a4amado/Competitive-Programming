/**
 * name: Petya and Strings
 * link: https://codeforces.com/contest/112/problem/A
 */

import { createInterface } from "readline";

const rl = createInterface({
    input: process.stdin,
    output: process.stdout,
    terminal: false,
});
let S1 = false;

let firstTotal = "";
let secondTotal = "";

rl.on("line", (line) => {
    if (!S1) {
        firstTotal = line.toLowerCase().trim();
    } else {
        secondTotal = line.toLowerCase().trim();
    }

    if (S1) {
        for (let index = 0; index < firstTotal.length; index++) {
            const n1 = firstTotal[index]?.toLowerCase();
            const n2 = secondTotal[index]?.toLowerCase();
            // @ts-ignore
            if (n1 < n2) {
                process.stdout.write("-1");
                process.exit(0);
                // @ts-ignore
            } else if (n1 > n2) {
                process.stdout.write("1");
                process.exit(0);
            }
        }
        process.stdout.write("0");
        process.exit(0);
    }
    S1 = true;
});
