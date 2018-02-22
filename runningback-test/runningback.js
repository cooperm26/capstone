function setup() {
  createCanvas(400, 400);
}
var rb = {
  x : 200 ,
  y : Math.floor(Math.random()*100)+300,
  length : 20 ,
  targetx : Math.floor(Math.random() * 400) ,
  targety : 200-Math.floor(Math.random() * 200) ,
  speedy : Math.floor(Math.random() * 4) +1,
  speedx : Math.floor(Math.random()*2.5) +1
}
function draw() {
  background(0,255,0) ;
  rect(rb.x,rb.y,rb.length,rb.length);
  fill(255,0,0)
  if (rb.x > rb.targetx) {
      rb.x = rb.x -rb.speedx;
  } else if (rb.x === rb.targetx) {
      rb.x = rb.x;
  } else {
      rb.x = rb.x + rb.speedx ;
  }
  if (rb.y > rb.targety) {
      rb.y = rb.y - rb.speedy ;
  } else if (rb.y === rb.targety) {
    rb.y = rb.y ;
  } else {
      rb.y = rb.y + rb.speedy ;
    }
}
