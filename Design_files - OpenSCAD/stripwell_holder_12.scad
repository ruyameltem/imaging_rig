// top part

rotate ([0,0,90]) translate([0,-180,2]) {
    
translate ([0,0,42]) cube([13,112,3]);

translate ([0,2,45]) cube([2,108,3]);

translate ([11,2,45]) cube([2,108,3]);

translate([0,0,45]) cube([13,2,3]);

translate([0,110,45]) cube([13,2,3]);

}

// middle part

rotate ([0,0,90]) translate ([0,-71,3]) cube([13,3,41]);

cube([71,13,3]);

// bottom part with holes

difference() {

translate([0,0,-19]) cube([3,13,19]);

//hole
    
rotate ([0,90,0]) translate([10,6.5,0]) cylinder(h=3,r=2.5,$fn=100);

}
