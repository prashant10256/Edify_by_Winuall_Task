// TODO => Write a function that takes an array of integers and returns a new array with only the unique values.

function getUniqueValues(arr) {
    const uniqueArray = [];
    arr.forEach(function(element) {
        if (!uniqueArray.includes(element)) {
            uniqueArray.push(element);
        }
    });
    return uniqueArray;
}

// Example usage:
const array = [1, 2, 3, 4, 2, 3, 5];
const uniqueArray = getUniqueValues(array);
console.log(uniqueArray); 

//================================= OR Example 2 =================>>>
function getUniqueValues(arr) {
    return [...new Set(arr)];
}

// Example usage:
const arr = [1,1,2,3,2,4,5,8,8,0,9];
const uniqueArr = getUniqueValues(arr);
console.log(uniqueArr); 
