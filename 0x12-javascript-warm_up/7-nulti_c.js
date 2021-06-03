#!/usr/bin/node
const str = 'C is fun';
if (process.argv[2] == null) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < process.argv[2]; i++) {
    console.log(str);
  }
}
