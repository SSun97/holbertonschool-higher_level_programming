#!/usr/bin/node
// concats 2 files
const fc = require('fs');
const textA = fc.readFileSync(process.argv[2]);
const textB = fc.readFileSync(process.argv[3]);
fc.writeFileSync(process.argv[4], textA + textB);
