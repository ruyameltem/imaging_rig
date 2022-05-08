
<h1 style="text-align: justify;"><strong>imaging Rig for Microfluidic blood analysiS (RMS)</strong></h1>
<h2 style="text-align: center;">Lights, Camera, Action!</h2>
<p><img src="https://i.ibb.co/pLZQtrF/Screenshot-2022-04-08-153114.png" alt="Rise of the blood and plasma" /></p>

<p style="text-align: justify;"><strong>Developed by</strong> Edwards lab, University of Reading School of Pharmacy <a href="https://research.reading.ac.uk/biomedical-technology-lab/">Biomedical Technology Lab</a></p>


<p style="text-align: justify;">The imaging rig has been developed to quickly test platelet function for cardiovascular health and disease epidemiology.</p>

<p style="text-align: justify;">This project aims at developing new assays and miniaturised devices to measure the function of the blood cells involved in clotting and thrombus formation- platelets (thrombocytes). The micro capillary film containing small capillaries and made using a melt extrusion process is used to develop new ways of measuring platelet function. We have been testing new detection methods such as using the Raspberry Pi camera.</p>

<p style="text-align: justify;">This system can be used to measure the parameters of liquids such as density and viscosity. By taking time-lapse images, kinetic information of the fluid in the capillary can be obtained. In this way, it is a suitable device not only for blood studies, but also for anyone who wants to work with fluids.</p>


<p style="text-align: justify;">This research shall contribute to the improvement of a new generation with state-of-the-art but affordable point-of-care tests for global utilizations.</p>

<p>You can find the rig's <a title="Technical Specifications" href="https://gitlab.com/ruyameltem/imaging_rig/-/blob/master/Technical%20Specifications.pdf" target="_blank" rel="noopener">Technical Specifications</a></p>

<h3 style="text-align: justify;">Fundamental and 3D-printed parts</h3>
<p><strong>Before you begin,</strong> make sure you have all the necessary parts. You can find all the parts in the <a title="Bill of Materials" href="https://gitlab.com/ruyameltem/imaging_rig/-/blob/master/Bill%20of%20Materials.pdf" target="_blank" rel="noopener">Bill of Materials</a> list.</p>
<p>It is good to have basic skills to use Raspberry Pi, some wiring skills for electronic parts, and designing and printing skills for <a title="3D-printed parts" href="https://gitlab.com/ruyameltem/imaging_rig/-/blob/master/3D%20printed%20parts.pdf">3D-printed parts</a>. Do not worry! You can gain skills by watching some short videos and browsing websites. Keep moving forward I added useful links for you. You only need to know how you can use the Raspberry Pi, which is a minicomputer and its pins, how you can wire the "black and red" cables and how to print the designs.</p>
<p>Make sure you have the necessary parts (camera, screen, power supply, SD card, optional: keyboard, mouse) to run the Raspberry pi.</p>
<p>Here are some useful links for Raspberry Pi: <a title="Getting started with Raspberry Pi" href="https://www.raspberrypi.com/dhttps://www.raspberrypi.com/documentation/computers/getting-started.htmlocumentation/computers/getting-started.html" target="_blank" rel="noopener">Getting started with Raspberry Pi</a>, <a title="Documentation: Raspberry Pi" href="https://www.raspberrypi.com/documentation/" target="_blank" rel="noopener">Documentation: Raspberry Pi</a>, <a title="Software: Raspberry Pi" href="https://www.raspberrypi.com/software/" target="_blank" rel="noopener">Software: Raspberry Pi</a></p> 

<p><strong>After collecting the fundamental parts,</strong> you will need to print the 3D printed parts. Download the STL files through the <a title="Design files - OpenSCAD" href="https://gitlab.com/ruyameltem/imaging_rig/-/tree/master/Design_files%20-%20OpenSCAD" target="_blank" rel="noopener">Design files - OpenSCAD</a> page.</p>

<p>You will need the nuts, bolts, etc. to assemble some of the parts. I printed 3D parts with Prusa i3 MK3. It is fine to use another 3D printer. You can tick the support option for some designs. You can change the layer size or any other settings. See below the settings I use:</p>

<p><img src="https://i.ibb.co/n8Kbw4h/prusa.png" alt="printer settings" border="0"></p>
<p>I used the black PLA filament to print all the parts. I just used transparent PLA filament for the test strip holder.</p>
<p>I designed and printed holders to attach all parts (battery, relay, etc.) to the aluminium extrusion. All are available on the design page.</p>
<p>If you have purchased the parts and printed what you need to print, now it is time to assemble them.</p>

<h3 style="text-align: justify;">Assembly Instructions</h3>
<h4 style="text-align: justify;">Assembling the V-Slot aluminium extrusions</h4>
<p>We used 4 20x20mm V-Slot linear rails to create the rectangle at the base. We used a 20x40mm extrusion to attach the servo motor, v-slot gantry plate kit, sample and test strip holders. We used a 20x80mm extrusion to fix the Pi camera and touchscreen. We wanted to be able to change the height of the camera when needed.</p>
<p>We used inside hidden corner, 90-degree cast corner, drop-in tee nuts and hex nuts to combine them. You can find the details in the bill of materials.</p>

<h4 style="text-align: justify;">Assembling the servo motor, gantry plate and strip holder</h4>
<p>The servo motor was attached to the 20x40mm aluminium extrusion by means of the servo bracket. An eccentric horn was placed on the servo in order to make the test strip holder rise and fall as the servo operated.</p>
<p>Servo is controlled by Raspberry Pi via servo six motor kit. The kit is powered by 4 AA batteries.</p>
<p>Useful link for servo six motor kit assembly instruction: <a title="Instructions: servo six board" href="https://cdn.shopify.com/s/files/1/0176/3274/files/instructions_servo_six.pdf?v=1589990518" target="_blank" rel="noopener">servo six board</a></p>

<p>Also, the stripwell holder is mounted on the extrusion. The holder fits a 1 x 12 Stripwell™ Microplate.</p>

<p>The gantry plate was placed on the extrusion so that it was on the upper part of the servo. In addition, the rack holder was mounted on the gantry plate to place the strip holder. Thus, the plate moves up and down by the servo so that it moves the holder.
Useful link for <a title="Gantry plate assembly" href="https://ooznest.co.uk/wp-content/uploads/2018/07/OX-Assembly-Manual.pdf">Gantry plate assembly instructions</a></p>

See figures:
<p><img src="https://i.ibb.co/SvCcXZH/servooo.png" alt="servo assembly" border="0"></p>

<h4 style="text-align: justify;">Assembling the camera and touchscreen</h4>
<p>The V2 Pi camera was mounted on the Raspberry Pi camera medium plate V2. Following this, the plate was attached to the 20x80mm aluminium extrusion. In addition, the touch screen was attached to the same extrusion by means of 2 touch Pi mounts and 2 universal mounts. Raspberry Pi was mounted on the back of the screen via the Pi case.</p>
<p>Useful links for camera and screen assembly instructions: <a title="Getting started with 7&Prime; touchscreen" href="https://www.okdo.com/getting-started/get-started-with-7-touchscreen-for-raspberry-pi/" target="_blank" rel="noopener">Getting started with 7&Prime; touchscreen</a>, <a title="Getting started with picamera" href="https://projects.raspberrypi.org/en/projects/getting-started-with-picamera" target="_blank" rel="noopener">Getting started with picamera</a></p>

<h4 style="text-align: justify;">Assembling the light sources and relay</h4>
<p>The white LED strips were soldered to the plastic sheet with black and red wires and framed by 4 20x80mm aluminium extrusions. The black wire should be soldered to the minus and the red wire to the positive. The lightbox was also mounted on the main frame.</p>
<p>The light source is controlled by Raspberry Pi via relay.</p>
<p>Useful links for relay assembly instructions and LED wiring: <a title="Relay and Raspberry Pi" href="https://www.electronicshub.org/control-a-relay-using-raspberry-pi/#:~:text=Technically%20speaking%2C%20a%20relay%20is,with%20respect%20to%20Raspberry%20Pi." target="_blank" rel="noopener">Relay and Raspberry Pi</a>, <a title="LED strips" href="https://www.waveformlighting.com/home-residential/how-to-connect-an-led-strip-to-a-power-supply" target="_blank" rel="noopener">LED strips</a></p>

<p><img src="https://i.ibb.co/zV51Zv0/Picture10led.png" alt="Picture10led" border="0"></p>


<h3 style="text-align: justify;">Run the Rig</h3>
</p>You only need to place your samples and microfluidic into the system. Then only you will need to run the script.</p>
</p>If you are wondering how the system works, check it out: <a title="Rig" href="https://gitlab.com/ruyameltem/imaging_rig/-/blob/master/Rig.mp4">Rig</a></p>

<p>A short video from an experiment: <a title="Performing an experiment" href="https://gitlab.com/ruyameltem/imaging_rig/-/blob/master/Performing%20an%20experiment.mp4">Performing an experiment</a></p>

<h3 style="text-align: justify;">Software</h3>

<p>If you want to update Python and your Raspberry Pi, make sure you type and run the following separately in the command section:</p>
<p>1 - sudo apt update</p>
<p>2 - sudo apt full-upgrade</p>
<p>3 - sudo apt-get update</p>
<p>4 - sudo apt-get install python3</p> 

<p>Note: I did not install the Bullseye edition because the camera system has errors with the last update of Raspberry Pi. But if you want to install and update, you can get help from this video to solve the problem: <a title="Raspberry Pi OS Bullseye Update: New Features &amp; Camera Issues" href="https://www.youtube.com/watch?v=0kr_yS9OhLM" target="_blank" rel="noopener">Raspberry Pi OS Bullseye Update: New Features &amp; Camera Issues</a></p>

<p>If you want to use the scripts separately, there are separate scripts for recording video, controlling the LED with a relay, and taking time-lapse images with a date stamp.</p>
<p>But if you want to download and use it directly, the script file you will run is called "Imaging Rig".</p>
<p>Here are the Python scripts you need: <a title="Software" href="https://gitlab.com/ruyameltem/imaging_rig/-/tree/master/Software">Software</a></p>
<p>It is good to have basic Python skills to make some changes on the scripts.</p>

<p>For any questions, please contact me: <a title="r.sariyer@pgr.reading.ac.uk" href="mailto:r.sariyer@pgr.reading.ac.uk">r.sariyer@pgr.reading.ac.uk</a></p>

<h3 style="text-align: justify;">The Rig</h3>
<p style="text-align: justify;">The device is shown below.</p>
<h2 style="text-align: center;"><img src="Imaging_Rig3.jpeg" alt="Imaging Rig" width="700" height="525" /></h2>
<h2 style="text-align: center;"><img src="Imaging_Rig4.jpeg" alt="Imaging Rig 2" width="450" height="600" /></h2>
<p style="text-align: justify;">The top view of the rig:</p>
<p><img src="https://i.ibb.co/ZJ02xhD/Picture9.jpg" alt="Picture9" border="0"></p>
<p>The rig gives images like the following one:</p>
<p><img src="Sample_image_1.jpeg" alt="Rise of the blood and plasma" /></p>
