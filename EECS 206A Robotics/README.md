## Dashboard
| Topics | Status| Takeaways |
| :---- | :-------- | :--------------------------------- |
| [Rigid Body Motion](./Notes/Rigid%20Body%20motion/)| <span style="color:green">**Check** | Change position in 3D space.|
| [Computer Vision](./Notes/Computer%20Vision/)| <span style="color:green">**Check** | Camera model, intrinsic matrix, map points with two cameras.|
| [Velocity](./Notes/Velocity/)| <span style="color:green">**Check**      | Map the point to its time derivatives.|
| [Jacobian](./Notes/Jacobian/)| <span style="color:green">**Check**      | Map the angle changes of joints to body/spatial velocity. Singularity & how to measure|
| [Dynamics](./Notes/Dynamics)  | Ready to start | |
| [3D Lagrangian]()  | Not Start | |
| [Control]()  | Not Start  | |

## Linear Algebra Python Usage
`np.outer` computes the outer product of two vectors. Commonly used in $ww^{\mathsf{T}}$ situations.
```
# Calculate ww^T
w = np.array([1, 2, 3])
result = np.outer(w, w)

# result = [[1 2 3]
#                 [2 4 6]
#                 [3 6 9]]
```
`np.dot` is versatile for scalar, vector, and matrix operations; acts like matrix multiplication for 2-D arrays. Commonly used in $\hat{w}v$

`np.cross` is commonly used for $\hat{w}v=w\times{v}$

```
w_hat = skew_3D(w)
np.dot(w_hat, v) = np.cross(w, v)
```

## Linear Algebra
Refer to [Linear Algebra review](./Linear%20Algebra/Linear%20Algebra%20Review.md).

If Linear Algebra is widely used in VR/AR, this section will be moved out to the parent folder.

## Ordinary Differential Equation
Refer to [Ordinary Differential Equation basics](./Ordinary%20Differential%20Equation/ODE%20basics.jpg).

If Ordinary Differential Equation is widely used in VR/AR, this section will be moved out to the parent folder.


# Logistics
- Website: https://pages.github.berkeley.edu/EECS-106/fa24-site/
- Questions: https://edstem.org/us/courses/63948/discussion/
- Each week, you are expected to attend 3 hours of lecture, 3 hours of lab section, and 1 hour of discussion.
- Lectures: 
  - 2-3:30pm on Tuesday/Thursday in Dwinelle 145
  - Lecture recordings: https://bcourses.berkeley.edu/courses/1537483/external_tools/78985
  - Lecture slides: https://bcourses.berkeley.edu/courses/1537483/modules
- Discussions: 
  - They will have a review of important topics and go over practice problems related to the material to supplement lecture content.
  - Thursday 4:00pm - 5:00pm (room TBD), Thursday 5:00pm - 6:00pm (room TBD), Friday 12:00noon - 1:00pm (room TBD), and Friday 4:00 - 4:00pm (room TBD).
- Assignments:
  - Homework will be released in the evening each Wednesday, starting August 28 (the first day of class). You will have until 11:59pm the following Tuesday to complete each assignment.
  - Each student is allocated 5 total days of extension, to be used on any homework assignment with no loss of points. **Note: Homework will not be accepted more than two days past the due date, barring extenuating circumstances. Also, homeworks prior to the midterm will not be allowed slip days because we want to release solutions for you to study.**
  - Please list all collaborators at the top of each submitted homework set.
  - Weekly homework parties! Each Friday 5:00pm - 7:00pm. They will be staffed by TAs to help students working through the homework.
    - Room?
  - Additionally, you will receive one homework drop if you complete **both** post-midterm surveys.
    - What is this?
  - Submission: https://www.gradescope.com/courses/568334
- Labs:
  - Thursday 11AM-2PM Cory 105
- Midterms
  - There will be two midterms covering the course material, on Thursday, October 3, and Thursday, November 21. The midterms will be held in person during class time. Students will be allowed a cheat sheet.
- Bridge Sections
  - Thursdays 6:00pm - 8:00pm, location forthcoming
  - This section is dedicated to providing a safe space for students who feel as though they are falling behind in the course. Bridge section will lag one week behind the lecture pace so students have time to formulate questions and ask them.
- Final Project
  - The final project is a major part of your grade for this course and must include sensing, planning, and actuation components on real hardware. Project deliverables include a proposal, a video, a live demo, a final report, and several intermediate check-ins.

<br>
<br>
