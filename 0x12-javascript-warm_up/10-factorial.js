#!/usr/bin/node
function factorial (a) {
  if (a == NaN || a === 1) {
    return 1;
  } else {
      return a * factorial( a - 1);
    }
}
n = parseInt(process.argv[2]);
console.log(factorial(n));
