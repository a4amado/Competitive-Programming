import { createInterface } from "readline";

const rl = createInterface({
    input: process.stdin,
    output: process.stdout,
    terminal: false,
});

async function Input(q: string) {
    return new Promise((res) => {
        rl.question(q, (answer) => res(answer));
    });
}

async function main() {
    const _number = await Input("");
    // @ts-ignore
    const _letters: string = await Input("");

    let num = 0;

    for (let i = 0; i < _letters.length; i++) {
        const current_Letter = _letters[i];
        const next_Letter = _letters[i + 1];
        if (
            typeof current_Letter === "undefined" ||
            typeof next_Letter === "undefined"
        ) {
            break;
        }
        if (current_Letter === next_Letter) num++;
    }

    process.stdout.write(`${num}`);
}

main();
