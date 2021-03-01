
//This camera mount is to go on the back of either V2 or HQ raspberry pi camera module.
//The mounting is from the back to allow modification (e.g. different lenses) to the front
//it's pretty crude and simple but is intended to be a drop-in module for more complex systems e.g. darkfield illumination system to measure light scattering from cells in microdevices.


//parameters varibales and spacing
lugy=5;
lugx=25;
ymount=40;
$fn=12;
    // HQ holes are 4mm from edge of 38mm square; i.e. 38/2-4 mm from centrepoint 19-4=15mm 
HQmount=15;

//LUGS for camera v2 board
module lugs(){
difference(){
hull(){
translate([10.4,0,0]) cylinder(d=4,h=10);
translate([20,0,0]) cylinder(d=8,h=4);
}
translate([10.4,0,-50]) cylinder(d=2,h=100);
}
}
    
module boardmount2(depth=4,pi2=true) {
union(){
//FIRST LUGS FOR CAMERA v2 BOARD has 2.2mm mounting holes; can comment out for HQ camera
if(pi2){

lugs();
mirror([1,0,0]){
    lugs();
}
}
//THEN PLATE FOR MOUNTING
difference(){
union(){
    //base plate (can be various shapes)
hull(){
translate([0,0,0]) cylinder(d=56,h=3);
translate([0,ymount,0]) cylinder(d=46,h=5);
}

//add first pair lugs for HQ camera    
translate([HQmount,-HQmount,0]) cylinder(d=6,h=10);
translate([-HQmount,-HQmount,0]) cylinder(d=6  ,h=10);  
    
//add lugs for mounting
    // lugx and lugy grid for mounts
//offset from core by ymount


translate([lugx,lugy+ymount,0]) cylinder(d=15,h=6);
translate([-lugx,lugy+ymount,0]) cylinder(d=15,h=6);

//paired lugs
hull(){
translate([HQmount,HQmount,0]) cylinder(d=6,h=10);
translate([lugx,-lugy+ymount,0]) cylinder(d=15,h=6);
}
hull(){
translate([-HQmount,HQmount,0]) cylinder(d=6,h=10);
translate([-lugx,-lugy+ymount,0]) cylinder(d=15,h=6);  
}

}


translate([-13,-13,-50]) cube([26,26,100]); //space for camera
    //ADD 2.8mm HOLES FOR HQ camera- PCB has 2.5mm mounting holes 
translate([HQmount,HQmount,-50]) cylinder(d=2.8,h=100);
translate([HQmount,-HQmount,-50]) cylinder(d=2.8,h=100);
translate([-HQmount,HQmount,-50]) cylinder(d=2.8,h=100);
translate([-HQmount,-HQmount,-50]) cylinder(d=2.8,h=100);

    //ADD 5.5mm HOLES FOR mounting with M5 t-nut bolts
translate([lugx,lugy+ymount,-50]) cylinder(d=5.5,h=100);
translate([lugx,-lugy+ymount,-50]) cylinder(d=5.5,h=100);
translate([-lugx,lugy+ymount,-50]) cylinder(d=5.5,h=100);
translate([-lugx,-lugy+ymount,-50]) cylinder(d=5.5,h=100);


}
}

}

//Bolt check
//translate([-HQmount,-HQmount,-50]) cylinder(r=1,h=100,$fn=120);


//boardmount2(); 
boardmount2(pi2=false);