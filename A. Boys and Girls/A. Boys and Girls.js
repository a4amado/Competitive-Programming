const { readFileSync, writeFileSync } = require("node:fs");
const { join } = require("node:path");
const input = readFileSync(join(__dirname, "input.txt")).toString("ascii");
const nums = input.split(" ")


function main() {
    let boys = parseInt(nums[0], 10);
    let girls = parseInt(nums[1], 10);


    const letters = [];



    writeFileSync(join(__dirname, "output.txt"), rec(letters, boys, girls).join(" "))
    return true


}
main()

function rec(l, b, g) {
    if (shouldIInsertAB(l, b)) {
        l.push("B")
        b--;
        return rec(l, b, g)
    } else if (shouldIInsertAG(l, b, g)) {
        l.push("G")
        g--;
        return rec(l, b, g)
    } else {
        return l;
    }
}

function shouldIInsertAB(l, b, g) {
    if (b === 0) return false;

    const last_item = l[l.length - 1]
    if (b > 0 && g === 0) return true
    if (last_item === "B") return false;

    return true;


}

function shouldIInsertAG(l, b, g) {
    if (g === 0) return false;
    const last_item = l[l.length - 1]
    if (g > 0 && b === 0) return true
    if (last_item === "G") return false;

    return true;


}