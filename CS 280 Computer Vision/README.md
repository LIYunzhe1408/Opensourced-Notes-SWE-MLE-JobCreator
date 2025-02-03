## Camera Calibration
Go from the pinhole model to real cameras imaging points in the 3D world. Understand the key behind algo, which can be called in most libraries.

### Preserve the image
How to we "preserve" the image? Like printing it out.
* Take pictures in 10Hz to record a motion was the first shoot by Leland Stanford in 1878.
* Digital cameras was developed in 1969, based on the fact that silicon atoms can release electrons when hit by photons. CCD is based on this theory to collect electrons. CMOS imagers are more common right now.
  * The key difference is in how the charge generated in converted to a voltage.
  * When digitized this becomes the pixel brightness value
* How to take this technology to get colored images?

### Whole story of calibration
World coordinates ->(3D to 3D Extrinsic) Pin hole camera coordinate ->(3D to 2D intrinsic) Pixel coordinate
* First transformation is called extrinsic $[R t]$
* Second transformation is called intrinsic $K$ as the CCD/CMOS is the device that collect electrons. To do with the focal length
* $P=K[R t]$ Camera matrix = intrinsic dot product extrinsic

For intrinsic parameters, $f_x$ and $f_y$ denote the focal length in pixels
* $f_x=\frac{F}{p_x}$ where $F$ is focal length in world unites, typically expressed n millimeters, $p_x$ is the size of the pixel in world units
* Also we have $s$ as skew coefficient
* Radial distortion coefficients model this type of distortion.

### Transformation
[Question] why multiply by 17, still the same point?
Rotation, translation, and perspective projection. Are these transformation linear?
* Rotation: yes
* Translation: no. x_1 + T, x_2 + T, x_1+x_2 = x_1+x_2+T not 2T
* Perspective projection: no

Euclidean transformation is the subset of Affine transformation.
* The rotation matrix is no need to be orthogonal

Use cross-product to get the intersect.

Represent infinity -> Homogenous -> rotation, translation -> graphic chips -> deep learning revolution
* Use homogenous coordinate for point representation.

Perspective projection makes 3D to 2D.

### Calibration methods
* Tsai's method: applying Direct Linear Transform algo. 
  * Over-determined solution -> least square solution based on dozens of points. 
  * Use SVD to solve it.
  * How to separate Intrinsic and Extrinsic? QR decomposition from linear algebra.
  * Use many more than 6 points (ideally more than 20) and non coplanar.
  * How to estimate the lens distortion parameters?
  * How can we enforce $\alpha{u}=\alpha{v}$
  * Reprojection error. The Euclidean distance between an observed image point and the reprojected point. It's for non-linear calibration refinement.
* Zhang's algorithm: Calibration from planar grids. More practical than tsai's calibration which requires world's 3D points are non-coplanar
  * Different in applying DLT as the points are coplanar and then $Z_w=0$
  * [Recheck slide 29 and the one in Tsai. Clarify the difference]

### Camera Localization
Perspective from n Points: PnP. This is the problem of determining the 6DoF pose of a camera(position and orientation) with respect to the world frame from a set of 3D-2D point correspondences.
* It assumes the camera to be **already calibrated**. Which indicates the pipeline of get image -> calibration -> find out location.
* It's the $R$, $T$ part.

It's important for computer vision in robotics because we need camera to give us inforamtion about the real world.


## Biocular Stereopsis
Disparity from eyes seeing a finger jump example. Triangularization.
* [Confusion]We need two fixed camera with Parallel Optical axes (fixation at infinity), so that we don't need motor to move them.


## Multi-view Geometry
[Important] What's known and what's unknown. Now, what if we don't know the camera and 3D shape. It's commonly used in reconstruction from internet images.
* General camera
* Unknown: camera and 3D shape
* Known: N Correspondence
* Goal: deepth of points.

How:
1. Define the relationship between
   * Epilolar line: Project the line in another image. Upon access = epipolar
   * Epipole: intersection of baseline with image planes
   * Relationship: a plane. Cross product -> normal -> define a plane. dot product for the normal and the point on the plane -> 0
2. 
   * Define the plane: the baseline is the translation between 2 cameras. Green line is the focal length. Then we get the $E$
   * Decompose the $E$
3. Solving depth via triangulation
   * $X$ is the coord in left camera, and $X'$is the coord in right camera. same point, different coord frame. K is from the SVD.
   * how many unknowns: 3, equations: 2*2
   * triangulation issue: noise. because we get information from the estimated camera not the calibrated one.

For robotics, $K$ is fixed, while every focal length and camera config are different on internet images. This can be used in motion tracking or match moveing for camera trajectory.

What if we want solid models instead of just points(what we have solved)? Multi-view stereo
* Input will be calibrated images from several viewpoints(Known camera: intirnsics and extrinsics). output a sense 3D model.
  * Getting the camera config from the video is very hard.
* how to choose the baseline?
  * Too small: large depth error
  * Too large: difficult search problem

* Voxel is a very expensice way to represent.
* What about 4D reconstruction?

