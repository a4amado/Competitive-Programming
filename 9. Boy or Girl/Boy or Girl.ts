/**
 * name: Boy or Girl
 * link: https://codeforces.com/contest/236/problem/A
 */

import { createInterface } from "readline";

const rl = createInterface({
    input: process.stdin,
    output: process.stdout,
    terminal: false,
});

rl.question("", (answer) => {
    const s = sanitizeString(answer);
    if (s % 2 === 0) {
        process.stdout.write("CHAT WITH HER!");
        process.exit();
    }
    process.stdout.write("IGNORE HIM!");
    process.exit();
});

function sanitizeString(s: string) {
    let chars: { [k: string]: number } = {};

    for (let index = 0; index < s.length; index++) {
        // @ts-ignore
        chars[s[index]] = (chars[s[index]] || 0) + 1;
    }

    return Object.keys(chars).length;
}
