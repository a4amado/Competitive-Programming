/**
 * name: Bear and Big Brother
 * link: https://codeforces.com/contest/791/problem/A
 */


import { createInterface } from "readline";

const rl = createInterface({
    input: process.stdin,
    output: process.stdout,
    terminal: false
});


rl.on("line", (line) => {
    let [Limak = 0, Bob = 0]: number[] = line.trim().split(" ").map(e => parseInt(e, 10));
    let years = 0;


    while (Limak <= Bob) {
        Limak = Limak * 3;
        Bob = Bob * 2
        years++;
    }

    process.stdout.write(years.toString())
    process.exit(0);


});

