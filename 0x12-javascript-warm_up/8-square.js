#!/usr/bin/node

const size = Math.floor(Number(process.argv[2]));
const X = [];
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    X.push('X');
  }
  for (let i = 0; i < size; i++) {
    console.log(X.join(''));
  }
}
