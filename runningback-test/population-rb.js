function Population(targetx, targety, m, num) {
  this.population ;
  this.matingpool ;
  this.generations = 0 ;
  this.finished = false ;
  this.targetx = targetx ;
  this.targety = targety ;
  this.mutationrate = m ;
  this.perfectscorex = 0 ;
  this.perfectscorey  = 0 ;

  this.population = [];
  for (var i = 0; i < num; i++) {
   this.population[i] = new DNA(this.target.length);
 }

   this.matingPool = [];


}
