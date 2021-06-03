#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
[myObject.type, myObject.value] = [myObject.value, myObject.type];
console.log(myObject);
