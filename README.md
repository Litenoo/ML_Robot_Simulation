# MLRobot
A virtual simulation with a moving robot, that will be controlled by ML model. By fitting the virtual model in game, I want to use gained experience later in real life project of robot made with Raspberry Pi


Here is the minimal requirements for 1.0 version of the simulation
The simulation 1.0:

### 1. There is a map, that is modificable. 

### 2. Collision system. If robot collides with wall, it is being punished.

### 3. There is a robot, which : 
- Has one sensor
- Can read the data of gyroscope that is mounted on it
- Can measure the distance with the sensor. The sensor only measures the distance in the front of the robot
- Has steering system, which is built of two independent wheels and servos

### 4. Graphical environment is optional, by editing flag
