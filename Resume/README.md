#### Tell me about yourself
**I**: I’m Jonas, a Master’s student in EECS at UC Berkeley with a strong background in robotics and computer vision. \
**E**: Over the past 7 years, I have developed real-time perception pipelines and object detection/tracking systems for mobile robots with omnidirectional chassis. \
**R**: My experience spans both research and industry, during undergrad, I worked on explainable AI for image classification and data mining in materials science, supported by the National Natural Science Foundation of China.
**W**: Before graduating, I interned at Momenta as a Software Engineer, helping to deliver the first version of the autonomous reversing feature in 6 months. 
**C**: I feel like I think it's dope to build something with a team, but it's even more dope to bring it to the real world. I really enjoy working in fast-paced environments, where things move quickly and ideas turn into real impact. After talking with Zhengtao at the career fair, I feel like MaxInsight is exactly the kind of place where I can make a real contribution and grow.

## Momenta
#### Can you walk me through your experience at Momenta and your role in improving the reversing feature for GM Cadillac Lyriq?
**S:** At Momenta, I worked as a Software Engineer Intern, contributing to the development of an autonomous reversing feature for GM’s Cadillac Lyriq. \
**T:** My task was to enhance the vehicle’s ability to detect and recover from stuck states during autonomous parking. \
**A:** I developed a clustering algorithm to detect when a vehicle was stuck, reducing false positives in the system. I also designed a checker that identified prolonged braking stops, improving the accuracy of stuck-state detection. \
**R:** These optimizations boosted recovery performance by 3% in real-world parking scenarios, improving reliability across 800+ test cases in 30+ garages. Additionally, I automated data processing, reducing the product manager’s workload by 87.5%.

#### How did you design the stuck-state detection system using clustering and SVM?
S (Situation):
At Momenta, we faced a critical issue in autonomous parking: vehicles occasionally got stuck due to obstacles, inaccurate localization, or environmental constraints (e.g., uneven surfaces, sensor noise). The existing system relied on rule-based policy, which resulted in false positives (misclassifying slow maneuvers as stuck states).

T (Task):
My goal was to develop a robust stuck-state detection algorithm that could differentiate between normal slow movements and genuine stuck scenarios.

A (Action):

1. Feature Engineering: I analyzed vehicle data, extracting relevant features such as:
    * Velocity and acceleration trends
    * Steering angle variation
    * Longitudinal and lateral displacement over time
    * Reversal patterns (oscillatory movements)
2. Clustering Analysis:
    * Applied DBSCAN (Density-Based Spatial Clustering) to segment driving trajectories into clusters of movement behavior.
    * Identified clusters representing stuck states based on low displacement, repetitive maneuvers, and steering oscillations.
3. SVM Classifier for Refinement:
    * I trained an SVM (Support Vector Machine) on labeled data to distinguish stuck states from normal low-speed maneuvers.
    * Used time-series windowing to extract temporal patterns, improving classification robustness.
4. Validation & Testing:
    * Evaluated the model on a test set of 15,000+ parking events, ensuring high generalization performance.
    * Fine-tuned hyperparameters to reduce false positives by 15% and improve recovery performance by 3%.

R (Result):
* Evaluated in real-world driving tests across 800+ parking cases in 30+ garages.
* Successfully deployed the stuck-state detection system, leading to more reliable recovery behavior in autonomous parking scenarios.
* The system enhanced simulation reliability across 15,000+ events, improving the real-world adaptability of the autonomous parking feature.

#### What was the role of the checker for prolonged braking stops? How did it improve system reliability?
S (Situation):
During testing, the system occasionally misclassified temporary halts as stuck states. For example, if the vehicle paused to re-evaluate its path, it could trigger an unnecessary stuck-state recovery maneuver, disrupting smooth parking.

T (Task):
* To increase classification accuracy, I designed a "prolonged braking checker" that verifies whether a detected stuck state truly represents an irrecoverable situation.

A (Action):

Analyzing Braking Patterns:
* Examined thousands of test cases to identify braking behavior during valid stops vs. genuine stuck scenarios.
* Extracted key features: brake pressure duration, wheel speed trends, and engine torque changes.

Implementing the Checker:
* Developed a lightweight rule-based module that:
* Tracks braking duration (eliminating false positives from momentary pauses).
* Monitors wheel-speed variations to detect continuous resistance (true stuck state) vs. intentional stops.
* Incorporates heuristics based on obstacle proximity and vehicle positioning.

Testing & Refinement:
* Integrated the checker into the simulation pipeline, validating it across 15,000+ events.

R (Result):
* 98% accuracy in identifying prolonged braking stops.
* Reduced false positive stuck detections by 15%, leading to smoother and more reliable parking maneuvers.
* Improved real-world simulation reliability, ensuring the system behaves more naturally in real urban scenarios.


stremhtj: engage people
weekness
the person i wanna work with: passion not sleep
tech trend
