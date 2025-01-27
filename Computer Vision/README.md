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
* To be continued

Reprojection error. The Euclidean distance between an observed image point and the reprojected point. It's for non-linear calibration refinement.