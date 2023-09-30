"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const fs_1 = require("fs");
const path_1 = require("path");
const input = (0, fs_1.readFileSync)((0, path_1.join)(__dirname, "input.txt")).toString("ascii");
const nums = input.split(" ");
function main() {
    let boys = parseInt(nums[0], 10);
    let girls = parseInt(nums[1], 10);
    const letters = [];
    const g = rec(letters, boys, girls).join("");
    console.log(g);
    (0, fs_1.writeFileSync)((0, path_1.join)(__dirname, "output.txt"), g);
}
main();
function rec(l, b, g) {
    if (shouldIInsertAB(l, b, g)) {
        l.push("B");
        b--;
        return rec(l, b, g);
    }
    else if (shouldIInsertAG(l, b, g)) {
        l.push("G");
        g--;
        return rec(l, b, g);
    }
    return l;
}
function shouldIInsertAB(l, b, g) {
    if (b === 0)
        return false;
    if (l.length === 0) {
        if (g < b || g == b)
            return true;
        else
            return false;
    }
    if (l[l.length - 1] === "B") {
        if (g === 0)
            return true;
        else
            return false;
    }
    return true;
}
function shouldIInsertAG(l, b, g) {
    if (g === 0)
        return false;
    if (l.length === 0) {
        if (g > b || g == b)
            return true;
        else
            return false;
    }
    if (l[l.length - 1] === "G") {
        if (b === 0)
            return true;
        else
            return false;
    }
    return true;
}
