// TODO => Implement a recursive function to calculate the factorial of a number.

function factorial(n) {
    // Base case: 
    if (n === 0) {
        return 1;
    }
    // Recursive case: 
    return n * factorial(n - 1);
}

const number = 4;
const result = factorial(number);
console.log(`The factorial of ${number} is: ${result}`); 
    