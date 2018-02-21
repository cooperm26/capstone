var initial_length = Math.floor(Math.random() * 40);
var x=50;
var y=50;

function draw() {
  rect(x,y,initial_length,initial_length);
  if (x<200){
    x = x +1 ;
  } else {
    y = y+1 ;
  }
}
