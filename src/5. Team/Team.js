"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const readline_1 = require("readline");
const rl = (0, readline_1.createInterface)({
  input: process.stdin,
  output: process.stdout,
  terminal: false,
});
let numberOfProblems;
let list = [];
let sureProblems = 0;
rl.on("line", (line) => {
  if (typeof numberOfProblems === "undefined") {
    numberOfProblems = parseInt(line, 10);
  } else if (line && list.length < numberOfProblems) {
    const state = line
      .split(" ")
      .map((n) => parseInt(n, 10))
      .reduce((p, c) => p + c);
    list.push(state);
    if (state >= 2) {
      sureProblems++;
    }
    if (list.length == numberOfProblems) {
      process.stdout.write(sureProblems.toString());
      process.exit(0);
    }
  }
});
