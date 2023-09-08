"use strict";
/**
 * name: Boy or Girl
 * link: https://codeforces.com/contest/236/problem/A
 */
Object.defineProperty(exports, "__esModule", { value: true });
const readline_1 = require("readline");
const rl = (0, readline_1.createInterface)({
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
function sanitizeString(s) {
    let chars = {};
    for (let index = 0; index < s.length; index++) {
        // @ts-ignore
        chars[s[index]] = (chars[s[index]] || 0) + 1;
    }
    return Object.keys(chars).length;
}
