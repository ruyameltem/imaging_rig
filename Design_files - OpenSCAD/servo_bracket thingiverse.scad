//https://www.thingiverse.com/thing:40590
 
//arm();
main();

module main(){

	servo_width = 20;
	servo_length=40.3;
	base_length = servo_length+18;
	base_width = 18;
	base_thickness = 3;
	
	union () {
		difference () {
			cube ([base_width,base_length,base_thickness], center = true);	//base
			translate ([-(base_width/2)+8,base_length/2-3.5,0]) cylinder(h = 30, r = 2, center = true, $fn=20); //holes
			translate ([-(base_width/2)+8,-base_length/2+3.5,0]) cylinder(h = 30, r = 2, center = true, $fn=20); //holes

			translate ([(base_width/2)-5,base_length/2-3.5,0]) cylinder(h = 30, r = 2, center = true, $fn=20); //holes
			translate ([(base_width/2)-5,-base_length/2+3.5,0]) cylinder(h = 30, r = 2, center = true, $fn=20); //holes
		}
		translate ([-base_width/2,servo_length/2,base_thickness/2]) arm(servo_width,base_width);
		mirror([0,1,0]) translate ([-base_width/2,servo_length/2,base_thickness/2]) arm(servo_width,base_width);

	}
}

module arm(servo_width,base_width){
	hole_distance = 8.1;
	hole_diameter = 3;
	
	echo(servo_width);
	
	 union () {
		difference () {
	          	translate([0,0,0]) cube( [3,9,servo_width]);	 
			translate (v=[0,3.5,servo_width/2-hole_distance/2]) { rotate(a=[0,90,0]) {cylinder(h = 30,r=hole_diameter /2, center = true, $fn=100);}}
			translate (v=[0,3.5,servo_width/2+hole_distance/2]) { rotate(a=[0,90,0]) {cylinder(h = 30,r=hole_diameter /2, center = true, $fn=100);}}
		}
		translate (v=[3,0,servo_width]) mirror([0,0,1]){
			polyhedron ( points = [[0, 0, servo_width], [0, 2, servo_width], [0, 2, 0], [0, 0, 0], [base_width-3, 0, servo_width], [base_width-3, 2, servo_width]], 
			faces = [[0,3,2], [0,2,1], [3,0,4], [1,2,5], [0,5,4], [0,1,5],  [5,2,4], [4,2,3], ]);
		}
	}
}
