#!/usr/bin/node

if (process.argv.length < 4) {
  console.log(0);
}
const myarr = process.argv.map(Number).slice(2).sort((a, b) => a - b);
console.log(myarr[myarr.length - 2]);
