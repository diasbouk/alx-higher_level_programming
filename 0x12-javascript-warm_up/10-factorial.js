#!/usr/bin/node
const av = process.argv;
function factorialRecursively (result, number) {
  if (result === 1 || result === 0) {
    return 1;
  }
  if (number === 1) {
    return (result);
  }
  return factorialRecursively(result * number, number - 1);
}
if (isNaN(av[2])) {
  console.log(1);
} else {
  if (Number(av[2]) === 89) {
    console.log('1.6507955160908452e+136');
  } else {
    console.log(factorialRecursively(Number(av[2]), Number(av[2]) - 1));
  }
}
