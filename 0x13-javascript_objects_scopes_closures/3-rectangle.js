#!/usr/bin/node
// Rectangle Class with restrictions
class Rectangle {
  constructor (w, h) {
    w = parseInt(w);
    h = parseInt(h);
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
   print () {
    console.log(('X'.repeat(this.width) + '\n').repeat(this.height).split('')
      .slice(0, -1).join(''));
}

module.exports = Rectangle;
