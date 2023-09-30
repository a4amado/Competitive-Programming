"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const readline_1 = require("readline");
const rl = (0, readline_1.createInterface)({
    input: process.stdin,
    output: process.stdout,
    terminal: false,
});
let NumbersOfGamesPlayed;
let Winners = [];
rl.on("line", (line) => {
    if (typeof NumbersOfGamesPlayed === "undefined") {
        const num = parseInt(line, 10);
        NumbersOfGamesPlayed = num;
    } else {
        Winners = line.trim().split("");
        rl.close();
    }
});
rl.once("close", () => {
    const w = {
        A: 0,
        D: 0,
    };
    Winners.forEach((e) => {
        // @ts-ignore
        w[e] = w[e] + 1;
    });
    if (w["A"] > w["D"]) {
        process.stdout.write("Anton");
    } else if (w["A"] < w["D"]) {
        process.stdout.write("Danik");
    } else {
        process.stdout.write("Friendship");
    }
});
