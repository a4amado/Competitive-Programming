import { stdout } from "process";
import { createInterface } from "readline";

const rl = createInterface({
    input: process.stdin,
    output: process.stdout,
    terminal: false,
});

let numberOfFriends: number | undefined;
let heightOfTheFence: number | undefined;
let heights: number[] = [];

rl.on("line", (input) => {
    if (!numberOfFriends || !heightOfTheFence) {
        const [n, h] = input
            .trim()
            .split(" ")
            .map((e) => parseInt(e));
        numberOfFriends = n;
        heightOfTheFence = h;
    } else if (heights.length === 0) {
        heights = input
            .trim()
            .split(" ")
            .map((e) => parseInt(e, 10))
            .filter((e) => Number.isInteger(e));

        rl.close();
    }
});

rl.once("close", () => {
    let road_width = 0;

    for (let index = 0; index < heights.length; index++) {
        // @ts-ignore
        if (heights[index] > heightOfTheFence) {
            road_width += 2;
        } else {
            road_width++;
        }
    }

    stdout.write(road_width.toString(), () => {
        process.exit(0);
    });
});
