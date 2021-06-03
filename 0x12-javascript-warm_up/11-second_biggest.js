#!/usr/bin/node
if (process.argv.length < 4) {
  console.log(0);
} else {
  let first = process.argv[2];
  let second = process.argv[3];
  if (first < second) {
    [first, second] = [process.argv[3], process.argv[2]];
  }
  for (let i = 4; i < process.argv.length; i++) {
    if (process.argv[i] >= first) {
      second = first;
      first = process.argv[i];
    } else if (process.argv[i] <= first && process.argv[i] >= second) {
      second = process.argv[i];
    }
  }

  console.log(second);
}
