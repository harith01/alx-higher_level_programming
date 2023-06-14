#!/usr/bin/node

const dict = require('./101-data.js').dict;
const output = {};
for (const key in dict) {
  const id = dict[key];
  output[id] = [];
  for (const key in dict) {
    if (dict[key] === id) {
      output[id].push(key);
    }
  }
}
console.log(output);
