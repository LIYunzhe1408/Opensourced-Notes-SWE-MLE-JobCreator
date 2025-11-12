## Introduce myself
Hi, my name is Jonas. I’m currently a Machine Learning Engineer at WeRide, which is a robotaxi company similar to Waymo. My current work focuses on developing real-time detection models for production-level AiDrive System and leveraging vision language models for offline large-scale data mining.

Before that, I interned at Momenta, another self-driving company that focuses more on assisted-driving systems, similar to Tesla’s Autopilot. During the internship, I helped deliver the first version of the reversing feature for GM Cadillac vehicles, and i engaged in the entire lifecycle of this feature.

I received my master’s degree in Computer Science from UC Berkeley, and my bachelor’s degree from Shanghai University. Over the past seven to eight years, I’ve been deeply involved in robotics and computer vision, starting from building real-time perception pipelines for mobile robots in competitions like FIRST Tech Challenge in high school and DJI RoboMaster in undergrad.

Those team experiences taught me how exciting it is to build something meaningful with others and see it actually work in the real world. That’s also why I’m really excited about Google — to contribute to large-scale, impactful products that can reach millions of users.


## Why leave and Why google
“That’s a great question.”

I’ve really appreciated my time at WeRide, where I have opportunities to develop production-level autonomous driving systems and work in fast-paced engineering teams. These experiences have taught me how to build machine learning systems that handle complex, real-world data under real-time constraints.

But over time, I’ve realized I want to work on problems with even broader impact, especially where ML models can directly shape products used by millions of people. That’s what draws me to Google.

I’m particularly inspired by how Google applies large-scale machine learning to everyday products like Maps, Search, and Gemini. Acutally, using Gemini in Colab has been eye-opening for me, i think it's not only a powerful debugging tool for engineers, but it also serves as a great learning resource for coding beginners. Like, my younger brother, who’s just starting to learn programming in high school, can simply ask Gemini questions in the Colab notebook itself instead of googling across websites like we used to. I’d love to contribute to that kind of meaningful product.

What also excites me is Google’s engineering excellence and its diverse engineer community. I believe that when people from different backgrounds come together, innovative ideas emerge more naturally. With my background in autonomous driving and real-time perception, I hope to bring a unique perspective to the team and contribute meaningfully to Google’s mission.


## Leadership principles
Reference: https://docs.google.com/document/d/112HBiMNvu6TYbDUOfVRe_MS4A-fKaWYrpMlmnsiMNiA/edit?usp=sharing


* Customer Obsession
  * Customer interaction: When you are working with a large number of customers(requirements), it's tricky to deliver excellent service to them all. So how do you go about prioritizing your customers' needs?
    * 问的是明白用户想要什么并且prioritize你的我work来满足用户需求
  * Go beyond: Tell me a time when you went above and beyond for a client.
* Are Right, A Lot
  * Work with incomplete data
  * Disagree with a colleague and you are wrong/right
  * Make a wrong decision and what you learnt
* Ownership
  * Go beyond
  * Conflict, push back
  * Help peers
* Bias for action
  * Take risk
  * Incomplete information
  * Moving fast for a deadline/without consulting manager
* Think big
  * Go beyond, see opportunity do smth much bigger than initial focus
* Invent & Simplify
  * Solve in an innovative way
  * simple solution to complex problem
* Learn and be curious
  * Learn smth by yourself and end up solving problems at work
* Dive deep
  * Make decisions with data
  * Go through a big problem and in-depth analysis
* Insist on highest standards
  * miss expectations
  * improve an already good system
* Earn trust
  * Do you collaborate well
* Deliver results
  * What's the project you are most proud of. challenges and resolve.

## Stories
### Story one
The situation was that I was a software engineering intern at Momenta, working on the reversing feature for GM Cadillac vehicles. I collaborated closely with the product manager on daily simulation testing and reporting.

The task was that she asked me to export raw reversing simulation logs every day so they postprocess them and prepare reports for daily stand-ups with the General Motor team.

My action was, initially, I followed the request and sent her the raw logs, but I started thinking about the downstream effort. I asked her how the data was used and realized that what they truly needed wasn't just the raw logs, but aggregated metrics of maneuvers for different scenarios and the differences with previous benchmarks. Their current solution was manually separate scenarios and calculate numbers one by one, and then fill them into a Microsoft Word doc. As we have several scenarios, this process took them over 2 hours a day. So she often assigned this to her interns.

But I know that the data structure was consistent and the output format was fixed, I proposed to build a python-based reporting pipeline that parsed the simulation logs, and aggregated key metrics, calculate numbers, and exported everything into a Word document using python-docx libraries. TBH, it didn't take a long time to develop.

The result was exciting that, this one-click reporting tool reduced their work from 2 hours to seconds. She and her interns were thrilled and shared it with other PMs across 4 vehicle projects. Eventually, the tool was integrated into our internal platform. So instead of just delivering what was asked, I jumped out of scope and dive deeper into this problem and delivered what was actually needed. Enabling  faster, insight-driven decision-making.

1.  Tell me a time when you went above and beyond for a client.[Customer Obsession]
2.  Tell me about a time when you took on something significant outside your area of responsibility.[Ownership]

### Story two
The situation was at my current role at WeRide, where I supported two key projects: an onboard traffic sign detection model for vehicle deployment, and an offboard road marker auto-labeling model used by the data team to generate pseudo labels.

Approaching the end of last quarter, the onboard team requested that we fully prioritize a new traffic sign model since it was blocking the production release. At the same time, the data team urgently needed updates to our uncertainty filtering module to improve label quality. So, both requests need development effort and GPU resources.

My task was to prioritize these competing requests.

So I scheduled a sync with both teams, came prepared with performance benchmarks, GPU usage projections, and a trade-off analysis. I proposed a compromise: prioritize the traffic sign model upgrade for that week to meet the mass production deadline, while rolling out a lightweight threshold-based uncertainty filter in parallel, then allocate full attention to the data team’s requirements the following week.

The result was successful: the traffic sign model launched on time, and the improved uncertainty filter was released the following week. While both teams had urgent needs, by being transparent and data-driven, we reached alignment and avoided resource conflicts.

1. When you are working with a large number of customers(requirements), it's tricky to deliver excellent service to them all. So how do you go about prioritizing your customers' needs? [Customer]
2. Tell me a time you had to leave a task unfinished [Ownership]
3. Did you have to push back a request [Ownership]
4. If you have conflict goals, how do you make trade-offs?[Ownership]
5. Multitask, prioritize, time management

   
### Story three
**Incomplete Data**
The situation was during my master's at UC Berkeley, I'm a member of the capstone project that developed an ai-driven system that can automatically choose the best modular pieces to build the most efficient robotic arm for specific tasks where a single rigid design is insufficient.

My task was to assemble different robot joints with linkages in simulation and make it an assembled robotic arm for further optimization. The simulation library i used was called timor-python, which provided limited tutorial for importing customized mesh file.

So my first action was to try some simple assemblies that only include two joints. But the assembled result made no sense that the linkage directly penetrated the entire motor. Then i looked into the mesh file the hardware team provided us and realized the key information is to edit the parameters correctly but these parameters are out of my knowledge. So i reached out to 2 members in hardware team, Chris and Cheney, and organized a quick in-person meeting with them. I asked them to show me how each joint work and how they were assembled in their 3D design. 

As a result, I quickly get the point and refine the code to get it assembled in just one day after the meeting.

**Incomplete data & Bad decision**
* Neuralmap model improvement: improve metric -> intuition is enlarge model size -> latency requirement -> experiment focuses on parameter increasing while latency not increasing much -> determine some ways. -> latency and safety should always be the priority

1. Tell me a time when you had to work with incomplete data or information
2. Tell me a time you made a bad decision and learning from the experience enabled you to make a good decision later.(Model perf & latency -> first version release with perf improve but latency ++ -> Find myself when testing the new model on vehicle -> Can not even detect obstacle)



### Story four
The situation was during my current work at WeRide, where I was leading a project on traffic sign detection. We had a large amount of unlabeled driving video, and sending all of it to human annotators would have been prohibitively expensive.

My task was to develop an auto-labeling model to detect traffic signs and generate bounding boxes as pseudo ground truth.

**For unexpected problem, trade-off for long&short** \
My first action was to research potential model candidates, including YOLO variants, transformer-based models, and internal detection modules. I drafted a proposal outlining two options: One was a quick, open-source model that could deliver results fast but lacked long-term maintainability. The other was a more systematic solution that adapted our internal traffic light model and training infrastructure for traffic sign detection. It would take more effort, requiring changes to proto definitions, dataloaders, and model heads, but offered better integration and long term gains.

After reviewing the trade-offs with my manager, I chose the long-term approach, even though there was a risk of missing the deadline. I mitigated this by breaking down the work into clearly scoped tasks, proto buffers, dataloader updates, model architecture, and evaluation scripts, and implemented them one by one with continuous testing.

As a result, I completed the model before the deadline and achieved strong performance. The modular approach not only reduced development time but also made it easier to maintain and scale in future iterations.


**For conflict** \
I initially proposed reusing our existing internal traffic light detection model as a base. However, a teammate suggested an alternative model architecture, claiming it could offer better performance. Rather than dismissing his idea or insisting on my approach, I suggested that, since we still had a few weeks of buffer, we both implement our respective ideas and evaluate them side by side, with a shared deadline to present preliminary results.

By the review point, we compared the performance, his model showed better precision, but as it's open-sourced and purely external, it required non-trivial effort to integrate with our current infra. After further discussion, I proposed refining my model based his architecture to align better with our infra, allowing us to preserve performance gains while reusing existing components.

The result was a collaborative win: we improved detection accuracy, maintained compatibility with our platform, and strengthened team alignment through open, data-driven decision-making.


1. Tell me a time when you disagreed with a colleague.
2. Tell me a time when you had to work on a project with unclear responsibility[Ownership]

### Story five
road marker auto labeling -> as offboard, codebase was left behind the master 2 months -> some dependencies have been updated and currently using hacky way to make it work

Task was trying to rebase it to master -> after rebasing, many dependencies can be completely removed, and the codebase will be easier to maintain

report to manager further improve codebase, see more opportunities than risks. but coupling several modules, require one week to decoupling, the worse case is, after 1 week, the rebase doesn;t work, but nothing will affect the auto label production -> I then break down task to decouple input from different sensors and only keep the necessary input, from dataloader to model dataflow

one week, Made it. As come back to master, many performance improvement on master also can be reused on auto labeling, make it maintainable.

1. Take risk
2. Improve an already good system