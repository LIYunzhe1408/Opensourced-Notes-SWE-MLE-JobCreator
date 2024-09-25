## Comments
This is summarized from the review of L2 and HW1.

### Key tips
![](./Figures/RB%20Rotation.jpg)
![](./Figures/RBGeneral%20Motion.jpg)
![](./Figures/Twist-1.jpg)
![](./Figures/Twist-2.jpg)
![](./Figures/Screw.jpg)
![](./Figures/tips.jpg)
   

# Rigid Body Motion
A rigid body motion of an object is a motion which preserves distance between points.

## Rigid Body transformations
A mapping $g:\mathbb{R^3} \rightarrow \mathbb{R^3}$ is a rigid body transformation if it satisfies: (not just rotation, but also translation)
1. Length is preserved: $\left |\left|  g(p)-g(q)  \right|\right| = \left |\left|  p-q  \right|\right|$ for all points $p, q \in \mathbb{R^3}$
    - But the $p-q\not= g(p)-g(q)$, as the vector has been rotated and the **orientation gonna be different**.
    - The transformation is defined for the two points, so the transformation for the vector is nothing more than applying the trans to the origin of the vector and the destination of the vector s.t. $g(v)=g(p-q)=g(p)-g(q)$
2. The cross product is preserved: $g(v\times{w})=g(v)\times{g(w)}$ for all vectors $v,w \in \mathbb{R^3}$
    - It is also called orientation-preserving, but it most presented the orientation the cross product.
    - The reflection in the mirror not preserves the orientation.

## Rotational Motions
1. Choose an inertial frame A
2. Attach a frame B to the body
3. The rotated vector $\overrightarrow{x_b}=x_{ab_1}\overrightarrow{x_a}+x_{ab_2}\overrightarrow{y_a}+x_{ab_3}\overrightarrow{z_a}$, then the $x_{ab}=[x_{ab_1}, x_{ab_2}, x_{ab_3}]^\mathsf{T}$ is the coordinate of vector $\overrightarrow{x_b}$ relative to the frame A.
4. The $y_{ab}, z_{ab}$ can be defined in the same way, then the **rotation matrix** is stacking them together as $R_{ab}=[x_{ab}|y_{ab}|z_{ab}]$ which is a $3\times{3}$ matrix.
    - $R_{AB}$ is the rotation matrix that "rotates" a frame, initially aligned with frame ${A}$ to fram ${B}$

### Property of Rotation Matrix
Rotation matrices are also coordinate transformation matrices. Points, and axes are both transformed.
1. $R_{ab}R^{\mathsf{T}}_{ab}=R^{\mathsf{T}}_{ab}R_{ab}=I$
      - As vectors in the rotation matrix are **orthonormal** that their unit is 1 and their multiplication is 0 unless multiply by themselves , we get $R_{ab}R^{\mathsf{T}}_{ab}=R^{\mathsf{T}}_{ab}R_{ab}=I$
2. $\det(R)=1$
    - Based on property 1:  $\det(R^{\mathsf{T}}R)=\det(R^{\mathsf{T}})\cdot \det(R)=(\det(R))^2=1 \Rightarrow \det(R)=\pm 1$
    - Recall the linear algebra that $\det(R)=r^{\mathsf{T}}_1(r_2\times r_3)r_1=1 \Rightarrow \det(R) = 1$
3. Preserve length between two points and orientation of the cross product.
    - $\left | \left |  R_{ab}\cdot (p-q) \right | \right | = \left | \left | p-q \right | \right |$
    - $R(v\times w)=(Rv)\times Rw$

### $SO(3)$
The set of all $3\times 3$ matrices satisfying these two properties is denoted $SO(3)$, which is *special orthogonal* referring to their $\det$ is 1 not $\pm 1$
- This is a group because it satisfies 4 properties of the group.(Page 28 of L2)
- Little $so(3)$ is a vector space, a set of all $3\times 3$ skew-symmetric matrices, not a group.

<br>
<br>
<br>

## Glossary
### Frame
You need:
1. The origin: point
2. 3 orthonormal vectors
    - Magnitude is 1
    - Orthogonal to each other. Multiply with each other is 0

### Coordinates
The motion of a particle moving in Euclidean space is described by giving the location of the particle at each instant of time, relative to an inertial coordinate system. Specifically, we choose a set of 3 orthonormal axes and specify the particle’s location using the triple $(x,y,z)\in \mathbb{R^3}$, where each **coordinate gives the projection** of the particle’s location **onto the corresponding axis**.

### Trajectory
A trajectory of a particle is a curve $p(t)=(x(t), y(t), z(t))\in{\mathbb{R^3}}$.
> All points on this curve form a trajectory.


### Rigid body
Rigid body is a collection of particles s.t. the distance between any two particles remains fixed. 
