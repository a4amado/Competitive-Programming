import { createInterface } from "readline";

const rl = createInterface({
    input: process.stdin,
    output: process.stdout,
    terminal: false
});

let NumbersOfGamesPlayed: number;
let Winners: string[] = [];

rl.on("line", (line) => {
    if (typeof NumbersOfGamesPlayed === "undefined") {
        const num = parseInt(line, 10);
        NumbersOfGamesPlayed = num;
    } else {
        Winners = line.trim().split("");
        rl.close()
    }
})

rl.once("close", () => {
    const w = {
        "A": 0,
        "D": 0
    };


    Winners.forEach((e: string) => {
        // @ts-ignore
        w[e] = w[e] + 1;
    })

    if (w["A"] > w["D"]) {
        process.stdout.write("Anton")
    } else if (w["A"] < w["D"]) {
        process.stdout.write("Danik")
    } else {
        process.stdout.write("Friendship")
    }
})