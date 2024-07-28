#!/usr/bin/node
const av = process.argv;
function add (a, b) {
  return Number(a) + Number(b);
}
console.log(add(av[2], av[3]));
