"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const promises_1 = __importDefault(require("readline/promises"));
const rl = promises_1.default.createInterface({
    input: process.stdin,
    output: process.stdout,
    terminal: false,
});
(function main() {
    var _a, _b;
    return __awaiter(this, void 0, void 0, function* () {
        const number_of_lines = yield rl.question("");
        const n = parseInt(number_of_lines || "0", 10);
        let lines = [];
        for (let index = 0; index < n; index++) {
            const [start, end] = (yield rl.question("")).split("");
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
                    if (((_a = lines[index]) === null || _a === void 0 ? void 0 : _a.start) === ((_b = lines[index - 1]) === null || _b === void 0 ? void 0 : _b.end)) {
                        s++;
                    }
                }
                console.log(s);
                rl.close();
            }
        }
    });
})();
