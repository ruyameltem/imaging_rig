//clip for
//19mm x 3mm thick handled holder for MCF 'train track' about 40mm long


thick=3;
wide=19;
$fn=12;
clearance=0.2; //this is minkowski around device

difference(){
    
    union(){
translate([0,0,0]) cube([thick+53,wide+25,4]);  //base plate 
translate([0,0,0]) cube([thick+2,wide+4,40]); //main holder
//translate([thick+2,2,0]) cylinder(h=40,d=6,$fn=12); //main rods
translate([thick+2,0,0]) cube([50,3,40]);      //plate to replace one rod, for servo waggling
translate([thick+2,wide+2,0]) cylinder(h=40,d=6,$fn=12); //main rods
    
        }
    
    //subtract core for grabbing flex
hull(){
translate([-1,wide/2+2,40]) rotate([0,90,0]) cylinder(d=wide/2.3,h=10);
translate([-1,wide/2+2,10]) rotate([0,90,0]) cylinder(d=wide/1.5,h=10);    
}
//MCF holder- this is the actual object to be held

hull(){
minkowski(){
translate([2,2,2]) cube([thick,wide,44]);
sphere(r=clearance);
}
translate([wide/3,wide/4+2,5]) cube([thick,wide/2,44]);

}
//translate([1,1,0]) cube([thick,wide+2,14]); //THIS WAS IN BASE OF CLIP 

//hole grid for mounting
for (i = [0:4]) {
    for (j = [0:5]) {
  translate([i*10+10,j*10+8,-1]) cylinder(d=5,h=20);
    }
}

}

module bracket(){
difference(){
union(){
translate([0,0,0]) cube([25,25,4]);  //base plate 
translate([0,0,0]) cube([4,25,20]); //bracket
}
for (i = [0:2]) {
    for (j = [0:3]) {
  translate([i*5+10,j*5+5,-1]) cylinder(d=2.5,h=20);
    }
}
}

}


//translate([30,0,0]) bracket();
