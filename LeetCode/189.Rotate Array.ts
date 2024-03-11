let list = [1,2];
let k = 3;



function rotate(nums: number[], k: number): void {
    const new_arr: number[] =  Array.from({ length: nums.length });


    for (let i = 0; i < nums.length; i++) {
        let idx = (i + k) % nums.length;
        new_arr[idx] = nums[i];
    }

    for (let i = 0; i < nums.length; i++) {
        nums[i] = new_arr[i]
    }
};


rotate(list, k)
console.log(list);


