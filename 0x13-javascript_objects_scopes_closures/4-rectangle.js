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

  rotate () {
    // rotate width and height
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    // double sizes of width and height
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
