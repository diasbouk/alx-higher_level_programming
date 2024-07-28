#!/usr/bin/node
const av = process.argv;
if (isNaN(Number(av[2]))) {
  console.log('Missing size');
} else {
  let i = 0;
  let line = '';
  while (i < Number(av[2])) {
    line += 'X';
    i++;
  }
  i = 0;
  while (i < Number(av[2])) {
    console.log(line);
    i++;
  }
}
