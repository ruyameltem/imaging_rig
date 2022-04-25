
<h1 style="text-align: justify;"><strong>imaging Rig for Microfluidic blood analysiS (RMS)</strong></h1>
<h2 style="text-align: center;">Lights, Camera, Action!</h2>
<p><img src="https://i.ibb.co/pLZQtrF/Screenshot-2022-04-08-153114.png" alt="Rise of the blood and plasma" /></p>

<p style="text-align: justify;"><strong>Developed by</strong> Edwards lab, University of Reading School of Pharmacy <a href="https://research.reading.ac.uk/biomedical-technology-lab/">Biomedical Technology Lab</a></p>


<p style="text-align: justify;">The imaging rig has been developed to quickly test platelet function for cardiovascular health and disease epidemiology.</p>

<p style="text-align: justify;">This project aims at developing new assays and miniaturised devices to measure the function of the blood cells involved in clotting and thrombus formation- platelets (thrombocytes). The micro capillary film containing small capillaries and made using a melt extrusion process is used to develop new ways of measuring platelet function. We have been testing new detection methods such as using the Raspberry Pi camera.</p>

<p style="text-align: justify;">This system can be used to measure the parameters of liquids such as density and viscosity. By taking time-lapse images, kinetic information of the fluid in the capillary can be obtained. In this way, it is a suitable device not only for blood studies, but also for anyone who wants to work with fluids.</p>


<p style="text-align: justify;">This research shall contribute to the improvement of a new generation with state-of-the-art but affordable point-of-care tests for global utilizations.</p>

<h3 style="text-align: justify;">Materials list</h3>
<p>The file with the necessary materials and prices to build the system:</p>
<p><a title="Bill of Materials" href="https://gitlab.com/ruyameltem/imaging_rig/-/blob/master/Bill%20of%20Materials.pdf">Bill of Materials</a></p>

<h3 style="text-align: justify;">Run the Rig</h3>
</p>You only need to place your samples and microfluidic into the system. Then only you will need to run the script.</p>
</p>If you are wondering how the system works, check it out:</p>
<p><a title="Rig" href="https://gitlab.com/ruyameltem/imaging_rig/-/blob/master/Rig.mp4">Rig</a></p>

</p>A short video from an experiment:</p>
<p><a title="Performing an experiment" href="https://gitlab.com/ruyameltem/imaging_rig/-/blob/master/Performing%20an%20experiment.mp4">Performing an experiment</a></p>

<h3 style="text-align: justify;">Software</h3>

<p>If you want to update Python and your Raspberry Pi, make sure you type and run the following separately in the command section:</p>
<p>1 - sudo apt update</p>
<p>2 - sudo apt full-upgrade</p>
<p>3 - sudo apt-get update</p>
<p>4 - sudo apt-get install python3</p> 

<p>Note: I did not install the Bullseye edition because the camera system has errors with the last update of Raspberry Pi. But if you want to install and update, you can get help from this video to solve the problem:</p>
<p><a title="Raspberry Pi OS Bullseye Update: New Features &amp; Camera Issues" href="https://www.youtube.com/watch?v=0kr_yS9OhLM" target="_blank" rel="noopener">Raspberry Pi OS Bullseye Update: New Features &amp; Camera Issues</a></p>

<p>If you want to use the scripts separately, there are separate scripts for recording video, controlling the LED with a relay, and taking time-lapse images with a date stamp.</p>
<p>But if you want to download and use it directly, the script file you will run is called "Imaging Rig".</p>
<p>Here are the Python scripts you need:</p>
<p><a title="Software" href="https://gitlab.com/ruyameltem/imaging_rig/-/tree/master/Software">Software</a></p>
<p>It is good to have basic Python skills to make some changes on the scripts.</p>

<h3 style="text-align: justify;">Useful links and assembly instructions:</h3>
<p>Check them out for some useful links and assembly instructions:</p>
<p><a title="Getting started with Raspberry Pi" href="https://www.raspberrypi.com/dhttps://www.raspberrypi.com/documentation/computers/getting-started.htmlocumentation/computers/getting-started.html" target="_blank" rel="noopener">Getting started with Raspberry Pi</a></p>
<p><a title="Documentation: Raspberry Pi" href="https://www.raspberrypi.com/documentation/" target="_blank" rel="noopener">Documentation: Raspberry Pi</a></p>
<p><a title="Software: Raspberry Pi" href="https://www.raspberrypi.com/software/" target="_blank" rel="noopener">Software: Raspberry Pi</a></p>
<p><a title="Getting started with 7&Prime; touchscreen" href="https://www.okdo.com/getting-started/get-started-with-7-touchscreen-for-raspberry-pi/" target="_blank" rel="noopener">Getting started with 7&Prime; touchscreen</a></p>
<p><a title="Getting started with picamera" href="https://projects.raspberrypi.org/en/projects/getting-started-with-picamera" target="_blank" rel="noopener">Getting started with picamera</a></p>
<p><a title="Gantry plate assembly" href="https://ooznest.co.uk/wp-content/uploads/2018/07/OX-Assembly-Manual.pdf">Gantry plate assembly</a></p>
<p><a title="Instructions: servo six board" href="https://cdn.shopify.com/s/files/1/0176/3274/files/instructions_servo_six.pdf?v=1589990518" target="_blank" rel="noopener">Instructions: servo six board</a></p>
<p><a title="Relay and Raspberry Pi" href="https://www.electronicshub.org/control-a-relay-using-raspberry-pi/#:~:text=Technically%20speaking%2C%20a%20relay%20is,with%20respect%20to%20Raspberry%20Pi." target="_blank" rel="noopener">Relay and Raspberry Pi</a></p>

<h3 style="text-align: justify;">The Rig</h3>
<p style="text-align: justify;">The device is shown below.</p>
<h2 style="text-align: center;"><img src="Imaging_Rig3.jpeg" alt="Imaging Rig" width="700" height="525" /></h2>
<h2 style="text-align: center;"><img src="Imaging_Rig4.jpeg" alt="Imaging Rig 2" width="450" height="600" /></h2>
<p>The rig gives images like the following one:</p>
<p><img src="Sample_image_1.jpeg" alt="Rise of the blood and plasma" /></p>
