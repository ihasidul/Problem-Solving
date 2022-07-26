// Use the following keyboard layout to solve the problem:
// ------- ------- -------
// |     | | ABC | | DEF |
// |  1  | |  2  | |  3  |
// ------- ------- -------
// ------- ------- -------
// | GHI | | JKL | | MNO |
// |  4  | |  5  | |  6  |
// ------- ------- -------
// ------- ------- -------
// |PQRS | | TUV | | WXYZ|
// |  7  | |  8  | |  9  |
// ------- ------- -------
// ------- ------- -------
// |     | |space| |     |
// |  *  | |  0  | |  #  |
// ------- ------- -------
// Print out the total number of keypress required to type a given phrase.

function presses(phrase) {
  var values = {
    A: 1,
    D: 1,
    G: 1,
    J: 1,
    M: 1,
    P: 1,
    T: 1,
    W: 1,
    " ": 1,
    1: 1,
    B: 2,
    E: 2,
    H: 2,
    K: 2,
    N: 2,
    Q: 2,
    U: 2,
    X: 2,
    0: 2,
    C: 3,
    F: 3,
    I: 3,
    L: 3,
    O: 3,
    R: 3,
    V: 3,
    Y: 3,
    S: 4,
    Z: 4,
    2: 4,
    3: 4,
    4: 4,
    5: 4,
    6: 4,
    8: 4,
    7: 5,
    9: 5,
  };
  return phrase.split("").reduce(function (count, val) {
    // console.log("Count: " + count + " Val: " + val);
    return count + values[val.toUpperCase()];
  }, 0);
}
console.log(presses("THREE3")); // returns 14
console.log(presses("Hello World")); // returns 25