#!/usr/bin/node
const a = parseInt(process.argv[2]);

function factorial (x) {
  if (x === 0) 
    return (1);
  } else if (x < 0) {
    return (0);
  } else {
    return (x * factorial(x - 1));
  }
}

if (isNaN(a)) {
  console.log(1);
} else {
  console.log(factorial(a));
}
