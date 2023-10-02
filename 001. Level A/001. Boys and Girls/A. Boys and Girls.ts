import { readFileSync, writeFileSync } from "fs";
import { join } from "path";
const input = readFileSync(join(__dirname, "input.txt")).toString("ascii");
const nums: string[] = input.split(" ");

function main() {
    let boys = parseInt(nums[0] as string, 10);
    let girls = parseInt(nums[1] as string, 10);

    const letters: Array<"B" | "G"> = [];

    const g = rec(letters, boys, girls).join("");
    console.log(g);
    writeFileSync(join(__dirname, "output.txt"), g);
}
main();

function rec(l: Array<"B" | "G" | null>, b: number, g: number) {
    if (shouldIInsertAB(l, b, g)) {
        l.push("B");
        b--;
        return rec(l, b, g);
    } else if (shouldIInsertAG(l, b, g)) {
        l.push("G");
        g--;
        return rec(l, b, g);
    }
    return l;
}

function shouldIInsertAB(l: Array<"B" | "G" | null>, b: number, g: number) {
    if (b === 0) return false;

    if (l.length === 0) {
        if (g < b || g == b) return true;
        else return false;
    }

    if (l[l.length - 1] === "B") {
        if (g === 0) return true;
        else return false;
    }

    return true;
}

function shouldIInsertAG(l: Array<"B" | "G" | null>, b: number, g: number) {
    if (g === 0) return false;
    if (l.length === 0) {
        if (g > b || g == b) return true;
        else return false;
    }
    if (l[l.length - 1] === "G") {
        if (b === 0) return true;
        else return false;
    }

    return true;
}
