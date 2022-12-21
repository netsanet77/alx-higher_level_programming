#!/usr/bin/node
const size = parseInt(process.argv[2]);

if (Number.isSafeInteger(size)) {
  let str = 'X';
  for (let i = 1; i < size; i++) {
    str += 'X';
  }
  for (let j = 0; j < size; j++) {
    console.log(str);
  }
} else {
  console.log('Missing size');
}
