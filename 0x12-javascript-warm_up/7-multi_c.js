#!/usr/bin/node
const av = process.argv;
if (isNaN(Number(av[2]))) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;
  while (i < Number(av[2])) {
    console.log('C is fun');
    i++;
  }
}
