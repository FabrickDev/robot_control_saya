# Robot Control Saya

ROS 2 package for controlling and simulating a mobile robot in Gazebo. This package provides a Python-based ROS 2 node for controlling the robot's movement through ROS 2 topics.

## Dependencies

This package requires the following ROS 2 packages:

* [robin_bringup](https://github.com/Bakso14/robin_bringup) — Robot simulation and Gazebo launch configuration.
* [robin_description](https://github.com/Bakso14/robin_description) — Robot description, including the robot model and related configuration.

This project:

* [robot_control_saya](https://github.com/FabrickDev/robot_control_saya) — Robot control node developed in Python.

## Requirements

Before using this package, make sure the following are installed:

* ROS 2
* Gazebo
* Git
* `colcon`

The ROS 2 environment should also be properly configured before building and running the workspace.

## Workspace Setup

Create a dedicated ROS 2 workspace:

```bash
mkdir -p ~/ros2_ws/src
```

Navigate to the `src` directory:

```bash
cd ~/ros2_ws/src
```

Clone all required repositories into the `src` directory:

```bash
git clone https://github.com/Bakso14/robin_bringup.git
git clone https://github.com/Bakso14/robin_description.git
git clone https://github.com/FabrickDev/robot_control_saya.git
```

After cloning, the workspace should have a structure similar to:

```text
ros2_ws/
└── src/
    ├── robin_bringup/
    ├── robin_description/
    └── robot_control_saya/
```

Using a dedicated `src` directory is the standard ROS 2 workspace organization, while `git clone` creates local copies of the required repositories.

## Build the Workspace

Return to the root directory of the workspace:

```bash
cd ~/ros2_ws
```

Build the workspace using `colcon`:

```bash
colcon build
```

After the build process has completed successfully, source the ROS 2 workspace:

```bash
source ~/.bashrc
```

If the workspace has not previously been added to `.bashrc`, you can alternatively source the generated setup file directly:

```bash
source ~/ros2_ws/install/setup.bash
```

## Run the Robot Simulation

Start the Gazebo simulation using the `robin_bringup` package:

```bash
ros2 launch robin_bringup my_robot_gazebo.launch.xml
```

This launch file starts the robot simulation and loads the required Gazebo environment and robot configuration.

Keep this terminal running while using the control node.

## Run the Robot Control Node

Open a new terminal and source the ROS 2 environment:

```bash
source ~/.bashrc
```

Then run the robot control node:

```bash
ros2 run robot_control_saya robot_saya_node
```

The control node will communicate with the simulated robot through ROS 2.

## Usage

The typical workflow is:

```text
Create ROS 2 workspace
        │
        ▼
Create src directory
        │
        ▼
Clone required repositories
        │
        ▼
colcon build
        │
        ▼
source ~/.bashrc
        │
        ▼
Launch Gazebo simulation
        │
        ▼
ros2 launch robin_bringup my_robot_gazebo.launch.xml
        │
        ▼
Open a new terminal
        │
        ▼
ros2 run robot_control_saya robot_saya_node
        │
        ▼
Robot control
```

## Repository

Main repository:

https://github.com/FabrickDev/robot_control_saya

## Related Repositories

* [Bakso14/robin_bringup](https://github.com/Bakso14/robin_bringup)
* [Bakso14/robin_description](https://github.com/Bakso14/robin_description)
* [FabrickDev/robot_control_saya](https://github.com/FabrickDev/robot_control_saya)

## Author
**Electrical Engineering Class of 2023 C – Industrial Robotics**

**Achmad Syahrul Ramadhan (23050874070)**

**Naufal Herjuno (23050874084)**

**Faqisna Putra Mardhatillah (23050874094)**
