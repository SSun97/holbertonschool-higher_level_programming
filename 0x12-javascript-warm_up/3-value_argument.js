#!/usr/bin/node
let s;
if (process.argv[2] == null) {
  s = 'No argument';
} else {
  s = process.argv[2];
}
console.log(s);
