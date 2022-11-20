
# ENPM662 - Project 1 Toy Car CAD Modeling & Simulation using Gazebo 



## Authors

- [Suriya Suresh](https://www.github.com/theunknowninfinite)
- [Sandip Sharan Senthil Kumar](https://github.com/Sandip2612)

## 1. Project Goals

1. Build a robot model on SolidWorks and export it as URDF.

2. Add LiDAR Sensor onto robot and show  visualization of LiDAR data in RViz.

3. Perform teleop and move around in the map in Gazebo.

4. Code up a simple publisher and subscriber for the robot so that it moves ahead in a straight line or circular loop for 10~15 seconds.

## 2. Installation of Dependencies

ROS is required to this package.
Install ROS by follwoing the instructions on:

http://wiki.ros.org/noetic/Installation

## 3. Setting up the package

1. Clone the github repo.

```` 
$ git clone link-of-repo
````
2. After cloning, you will see  three folders, Assembly

3. Inside the repo under package is the ROS package which is required to run the robot & the package is named as robo_car

4. Go to your catkin_ws by typing the command  ````$ cd <your catkin_ws_name>```` 

5. Place that package in your catkin_ws under src 

6. Then run the command ```` $ catkin_make clean && catkin_make ```` to build the package

7. Source everytime you open a new terminal or made any changes in the ROS package using the command
````
source devel/setup.bash
````
## 4. Instruction to run RViz to visualize LiDAR

1. Open two terminals and source the package using the command mentioned above <br />

2. Run the command below to launch the toy car in Gazebo environment
```` 
roslaunch robo_car template_launch.launch 
```` 
3. In your other terminal run the command, to launch the teleop controllers
````
rosrun rviz rviz
````

4. Add the RobotModel and Laserscan. There you go you can see the Toy car and LiDAR visualization in RViz

## 5. Instructions to run the toy car using Teleop

1. Open two terminals and source ROS using the command mentioned above <br />

2. Run the command below to launch the toy car in Gazebo environment
```` 
roslaunch robo_car template_launch.launch 
```` 
3. In your other terminal run the command, to launch the teleop controllers
````
rosrun robo_car teleop_template.py
````
4. The controls to move the toy car are: 


    " i "- To move Forward 

    " j "- To turn to the Right

    " l "- To turn to the Left
    
    " , "- To move Backwards

    " o "- To move Forward turning to the left at the same time

    " u "- To move Forward turning to the right at the same time

    " m "- To move Backwards turning to the left at the same time

    " . "- To move Backwards turning to the right at the same time

    " k " - Force Stop

    "Anything else" - Smooth stop

## 6. Instructions to run the toy car using Subscriber and Publisher

## ---------- For Straight Line Movement ----------

1. Open three terminals and source ROS using the command mentioned above <br />

2. Run the command below in the first terminal to launch the toy car in Gazebo environment
```` 
roslaunch robo_car template_launch.launch 
```` 
3. In your second terminal run the command, to launch the subscriber 
````
rosrun robo_car subscriber_straight.py
````
4. In your third terminal run the command, to launch the publisher
````
rosrun robo_car publisher_straight.py
````
5. The robot car can be seen moving along the X-axis of the Gazebo in a straight path before coming to a stop.

## ---------- For Circular Loop Movement ----------

1. Open three terminals and source ROS using the command mentioned above <br />

2. Run the command below in the first terminal to launch the toy car in Gazebo environment
```` 
roslaunch robo_car template_launch.launch 
```` 
3. In your second terminal run the command, to launch the subscriber 
````
rosrun robo_car subscriber_circle.py
````
4. In your third terminal run the command, to launch the publisher
````
rosrun robo_car publisher_circle.py
````
5. The robot car can be seen moving along a circular loop in Gazebo before coming to a stop.

