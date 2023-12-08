let smallestX = time;
let x = 0;
let y = 0;
while (x < time) {
  y = x * (time - x);
  if (y > distance) {
    smallestX = x
    break;
  }
  x++;
}
console.log(smallestX);
let biggestX = 0;
x = time;
while (x > smallestX) {
  y = x * (time - x);
  if (y > distance) {
    biggestX = x;
    break;
  }
  x--;
}
console.log(biggestX);
console.log(biggestX-smallestX+1);