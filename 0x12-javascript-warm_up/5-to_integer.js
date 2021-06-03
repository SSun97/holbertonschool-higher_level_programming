#!/usr/bin/node
const n = parseInt(process.arg[2]);
if (!isNaN(n)) {
  console.log('My number: ' + n);
} else {
  console.log('Not a number');
}
