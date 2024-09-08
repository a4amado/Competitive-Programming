/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    const memo = {};
    return function(...args) {
        const key = JSON.stringify(args)
        if (key in memo) {
            return memo[key]
        }
        memo[key] = fn(...args)  
        return memo[key]
    }
}

