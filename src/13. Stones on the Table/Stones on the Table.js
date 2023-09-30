"use strict";
var __awaiter =
    (this && this.__awaiter) ||
    function (thisArg, _arguments, P, generator) {
        function adopt(value) {
            return value instanceof P
                ? value
                : new P(function (resolve) {
                      resolve(value);
                  });
        }
        return new (P || (P = Promise))(function (resolve, reject) {
            function fulfilled(value) {
                try {
                    step(generator.next(value));
                } catch (e) {
                    reject(e);
                }
            }
            function rejected(value) {
                try {
                    step(generator["throw"](value));
                } catch (e) {
                    reject(e);
                }
            }
            function step(result) {
                result.done
                    ? resolve(result.value)
                    : adopt(result.value).then(fulfilled, rejected);
            }
            step(
                (generator = generator.apply(thisArg, _arguments || [])).next(),
            );
        });
    };
Object.defineProperty(exports, "__esModule", { value: true });
const readline_1 = require("readline");
const rl = (0, readline_1.createInterface)({
    input: process.stdin,
    output: process.stdout,
    terminal: false,
});
function Input(q) {
    return __awaiter(this, void 0, void 0, function* () {
        return new Promise((res) => {
            rl.question(q, (answer) => res(answer));
        });
    });
}
function main() {
    return __awaiter(this, void 0, void 0, function* () {
        const _number = yield Input("");
        // @ts-ignore
        const _letters = yield Input("");
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
    });
}
main();
