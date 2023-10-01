import readline from "readline/promises";

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
    terminal: false,
});

(async function main() {
    const number_of_lines = await rl.question("");
    const n = parseInt(number_of_lines || "0", 10);

    let lines: {
        start: number;
        end: number;
    }[] = [];

    for (let index = 0; index < n; index++) {
        const [start, end]: string[] = (await rl.question("")).split("");
        lines.push({
            start: parseInt(start || "0", 10),
            end: parseInt(end || "0", 10),
        });
        if (index === n - 1) {
            let s = 0;
            for (let index = 0; index < lines.length; index++) {
                // handle first item and last item
                if (index === 0) {
                    s++;
                    continue;
                }
                if (index === lines.length - 1) {
                    continue;
                }

                if (lines[index]?.start === lines[index - 1]?.end) {
                    s++;
                }
            }
            console.log(s);

            rl.close();
        }
    }
})();
