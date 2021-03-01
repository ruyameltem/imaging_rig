
//LUGS for camera v2 board
module lugs(){
difference(){
hull(){
translate([10.4,0,0]) cylinder(r=3,h=10);
translate([20,0,0]) cylinder(r=5,h=5);
}
translate([10.4,0,-50]) cylinder(r=2,h=100);
}
}
    
module boardmount2(depth=4,pi2=true) {
union(){
//FIRST LUGS FOR CAMERA BOARD; can comment out for HQ camera
if(pi2){

lugs();
mirror([1,0,0]){
    lugs();
}
}
//THEN PLATE FOR MOUNTING
difference(){
union(){
translate([-30,-30,0]) cube([60,60,2]);
//add lugs for HQ camera    
translate([17,17,0]) cylinder(r=3,h=10);
translate([17,-17,0]) cylinder(r=3,h=10);
translate([-17,17,0]) cylinder(r=3,h=10);
translate([-17,-17,0]) cylinder(r=3,h=10);    
}
translate([-15,-15,-50]) cube([30,30,100]); //space for camera
    //ADD HOLES FOR HQ camera
translate([17,17,-50]) cylinder(r=2,h=100);
translate([-17,17,-50]) cylinder(r=2,h=100);
translate([17,-17,-50]) cylinder(r=2,h=100);
translate([-17,-17,-50]) cylinder(r=2,h=100);


}
}

}




boardmount2(); 
//boardmount2(pi2=false);
