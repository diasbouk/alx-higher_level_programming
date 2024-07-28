#!/usr/bin/node
const av = process.argv;
if (isNaN(Number(av[2]))) {
  console.log('Not a number');
} else {
  console.log('My number: ' + Number(av[2]));
}
