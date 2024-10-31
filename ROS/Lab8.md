## Checkpoint 1
### Setup Realsense Camera
1. ssh into the turtlebot and launch the realsense.
2. Check the parameters of the launch command.
> * `color_width`, `color_height`: resolution of the image
> * `depth_width`, `depth_height`: resolution of the depth image
> * `align_depth`: align the depth image to the RGB image. Map RGB pixels to depth points
> * `depth_fps`, `color_fps`: save compute. Launch Rviz to see raw images.

### Find a Goal Position
Link base_footprint with camera_link by
> `rosrun tf static_transform_publisher`

Use `rosrun tf2 tools view frames.py` to visualize the full tree of coordinate transforms.

### Camera Intrinsics
Fill in the `camera_info_callback()`, the msg info is listed https://docs.ros.org/en/noetic/api/sensor_msgs/html/msg/CameraInfo.html

To index the intrinsic matrix, call `msg.K`, 
```python
def camera_info_callback(self, msg):
    # TODO: Extract the intrinsic parameters from the CameraInfo message
    self.fx = msg.K[0]
    self.fy = msg.K[4]
    self.cx = msg.K[2]
    self.cy = msg.K[5]
```
### Object Detection
#### Color thresholding
It is one of the simplest yet most effective methods for object detection in images, especially when the object of interest has a distinct color. The result is a binary image where the pixels within our defined range are set to white (255) and all other pixels are set to black (0). Limitations:
* sensitivity to lighting: HSV can alleviate
* objects with similar color will be detected as well

#### Convert to HSV
HSV is more robust to lighting changes and allows us to focus on the Hue, which is a more accurate representation of color. Tips:
* make Hue bounds much tighter (+/-10) to filter out other color
* make Saturation and Value bounds much looser (+/-80)

#### Steps to do
1. Find the correct threshold by running `rosrun perception hsv_color_thresholder.py`
2. Create a mask by `mask = cv2.inRange(image_HSV, low_bound, up_bound)`
3. Use `np.nonzero(mask)` to get the coordinates of the cup points on the mask. An example is shown below, the first array is the x coordinate, the second is the y coordinate.
    ```python
    import numpy as np
    x = np.array([[3, 0, 0], [0, 4, 0], [5, 6, 0]])
    x
    array([[3, 0, 0],
           [0, 4, 0],
           [5, 6, 0]])
    np.nonzero(x)
    (array([0, 1, 2, 2]), array([0, 1, 0, 1]))
    ```
4. While there are better ways to filter out this noise, we can simply take the mean position of all points left in the mask and call that the center of our cup
5. Complete the coordinate transform
    ```python
    def pixel_to_point(self, u, v, depth):
        # Convert pixel coordinates (u, v) and depth to 3D real-world coordinates
        X = (u - self.cx) * depth / self.fx
        Y = (v - self.cy) * depth / self.fy
        Z = depth
        return X, Y, Z
    ```
6. Run `rosrun rviz rviz` and add an Image object in RVIZ

## Checkpoint 2
### Bézier curve
```python
def bezier_curve(p0, p1, p2, p3, t):
    """Calculate a point on a cubic Bezier curve defined by p0, p1, p2, and p3 at parameter t."""
    return (1 - t)**3 * p0 + 3 * (1 - t)**2 * t * p1 + 3 * (1 - t) * t**2 * p2 + t**3 * p3
```
### Curved Traj
```python
tfBuffer = tf2_ros.Buffer()  # Initialize a buffer
tfListener = tf2_ros.TransformListener(tfBuffer)  # Initialize a transform listener
trans = tfBuffer.lookup_transform('world', 'turtlebot', rospy.Time(0))
x2 = x1 + target_position[0]
y2 = y1 + target_position[1]
```

## Checkpoint 3
### Controller
``python
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)  # Publish to the cmd_vel topic
tfBuffer = tf2_ros.Buffer()  # Initialize a buffer
tfListener = tf2_ros.TransformListener(tfBuffer)  # Initialize a transform listener

prev_time = rospy.get_time()  # Initialize time
integ = np.array([0, 0])  # Initialize integral term as a zero array
derivative = np.array([0, 0])  # Initialize derivative term as a zero array
previous_error = np.array([0, 0]) 


# Prepare waypoint for transformation to base_link frame
waypoint_trans = PoseStamped()
waypoint_trans.pose.position.x = waypoint[0]
waypoint_trans.pose.position.y = waypoint[1]
waypoint_trans.pose.position.z = 0  # Assuming the waypoint is on the ground

# Set orientation based on the current yaw angle
quat = quaternion_from_euler(0, 0, baselink_yaw)
waypoint_trans.pose.orientation.x = quat[0]
waypoint_trans.pose.orientation.y = quat[1]
waypoint_trans.pose.orientation.z = quat[2]
waypoint_trans.pose.orientation.w = quat[3]

waypoint_in_base_link = do_transform_pose(waypoint_trans, trans_odom_to_base_link)


# Calculate error
x_error = waypoint_in_base_link.pose.position.x
y_error = waypoint_in_base_link.pose.position.y
error = np.array([x_error, y_error])

 # Integral term
integ += error * dt  # Sum error over time
integral = np.dot(Ki, integ).squeeze()

# Derivative term
error_deriv = (error - previous_error) / dt
derivative = np.dot(Kd, error_deriv).squeeze()

previous_error = error
prev_time = curr_time

pub.publish(control_command)

# Stopping condition: Check if the waypoint is close enough
if np.linalg.norm(error) < 0.05:  # If within 5 cm of target
    print("Moving to next waypoint in trajectory")
    return

def planning_callback(msg):
    try:
        trajectory = plan_curved_trajectory((msg.pose.position.x, msg.pose.position.y))  # Plan trajectory to target
    
        # Loop over waypoints and call the controller function on each waypoint
        for waypoint in trajectory:
            controller((waypoint[0], waypoint[1]))

rospy.Subscriber("/move_base_simple/goal", PoseStamped, planning_callback)
```
