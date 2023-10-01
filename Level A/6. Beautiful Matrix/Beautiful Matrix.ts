/**
 * name: Beautiful Matrix
 * link: https://codeforces.com/contest/263/problem/A
 */

import { createInterface } from "readline";

const rl = createInterface({
    input: process.stdin,
    output: process.stdout,
    terminal: false,
});

let rows = 0;

const po = {
    columns: 0,
    rows: 0,
};

rl.on("line", (line) => {
    if (rows < 5) {
        line.split(" ").map((e, index) => {
            const num = parseInt(e, 10);

            if (num === 1) {
                po["rows"] = rows;
                po["columns"] = index;
            }
        });
        rows++;

        if (rows === 5) {
            const list_of_steps =
                differenceBetween2Numbers(po["rows"], 2) +
                differenceBetween2Numbers(2, po["columns"]);

            process.stdout.write(list_of_steps.toString());
            process.exit();
        }
    }
});

function differenceBetween2Numbers(num1: number, num2: number) {
    return Math.abs(num1 - num2);
}
