#!/usr/bin/node
function factorial (a) {
  if (isNaN(a) || a === 1) {
    return 1;
  } else {
    return a * factorial(a - 1);
  }
}
const n = parseInt(process.argv[2]);
console.log(factorial(n));
