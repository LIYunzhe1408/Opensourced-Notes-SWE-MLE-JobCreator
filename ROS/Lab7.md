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