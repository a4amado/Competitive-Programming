"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const process_1 = require("process");
const readline_1 = require("readline");
const rl = (0, readline_1.createInterface)({
  input: process.stdin,
  output: process.stdout,
  terminal: false,
});
let numberOfFriends;
let heightOfTheFence;
let heights = [];
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
  process_1.stdout.write(road_width.toString(), () => {
    process.exit(0);
  });
});
