#!/usr/bin/node
exports.callMeBoy = function (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
