

//plan to have servo horn with 15mm offset to make cam


module eccentrichorn(sized=80,offset=15){
    difference(){
    translate([offset/2,0,0])cylinder(h=2,d=sized,$fn=120);
    
translate([0,0,-50])        cylinder(d=2,h=100,$fn=12);
        
         for (i = [1:3]) { 
            translate([i*5,0,-50]) cylinder(d=2.5,h=100,$fn=12);
mirror([1,0,0])translate([i*5,0,-50]) cylinder(d=2.5,h=100,$fn=12);
             }
        
    }
}


eccentrichorn();
