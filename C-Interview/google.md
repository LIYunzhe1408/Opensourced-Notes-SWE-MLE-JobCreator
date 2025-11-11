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
The situation was that I was a software engineering intern at Momenta, working on the reversing feature for GM Cadillac vehicles. I collaborated closely with the product manager on daily simulation testing and reporting.

The task was that she asked me to export raw reversing simulation logs every day so they could manually review stuck cases and prepare reports for daily stand-ups with the GM team.

Initially, I followed the request and sent her the raw logs, but I started thinking about the downstream effort. I asked her how the data was used and realized that what they truly needed wasn't just the raw logs, but a summary of pass/fail statistics in different scenarios and the gap with previous benchmarks, formatted into a Word report. She mentioned it took over 2 hours a day, often delegated to her interns, just to aggregate metrics and fill out the same template.

Since the data structure was consistent and the output format was fixed, I proposed and built an automated reporting pipeline that parsed the simulation logs, calculated key metrics like success rate and metric differences, and exported everything directly into a Word document using python libraries. It didn't take a long time for development.

The result was a one-click reporting tool that reduced her work from 2 hours to seconds. She was thrilled and shared it with other PMs across 4 vehicle projects. Eventually, the tool was integrated into our internal platform. So instead of just delivering what was asked, I delivered what was actually needed and enable faster, insight-driven decision-making.

1.  Tell me a time when you went above and beyond for a client.[Customer Obsession]
2.  Tell me about a time when you took on something significant outside your area of responsibility.[Ownership]


Sure. At WeRide, I supported multiple internal teams that all depended on our auto-labeling system, including perception, QA, and data management. One time, the perception team requested that we fully prioritize a new traffic light model because it was blocking their L3 release.

But at the same time, the QA team urgently needed updates on uncertainty filtering to handle an annotation backlog. The two requests conflicted—running both would exceed GPU limits and delay processing for everyone.

So I scheduled a short sync with both teams. I prepared performance estimates, system bottlenecks, and trade-off charts in advance. We walked through the impact of each request, and I proposed a compromise: we’d prioritize traffic light model upgrades this week while rolling out a lightweight uncertainty filter that wouldn’t slow down throughput.

It wasn’t easy—both teams felt their needs were urgent—but by showing transparency and backing up trade-offs with data, we reached alignment. The model launched on time, and the QA backlog dropped the following week.

1. When you are working with a large number of customers(requirements), it's tricky to deliver excellent service to them all. So how do you go about prioritizing your customers' needs? [Customer]
2. Tell me a time you had to leave a task unfinished [Ownership]
3. Did you have to push back a request [Ownership]
4. If you have conflict goals, how do you make trade-offs?[Ownership]

   
* Optibot: mesh file -> assembly no sense -> key info is param in mesh file -> meet with 2 memebers in HW Team
* Neuralmap model improvement: improve metric -> intuition is enlarge model size -> latency requirement -> experiment focuses on parameter increasing while latency not increasing much -> determine some ways. -> latency and safety should always be the priority

1. Tell me a time when you had to work with incomplete data or information
2. Tell me a time you made a bad decision and learning from the experience enabled you to make a good decision later.(Model perf & latency -> first version release with perf improve but latency ++ -> Find myself when testing the new model on vehicle -> Can not even detect obstacle)

    
* Optibot: I propose one solution -> one proposed and let me use his -> no data evidance -> not pushing back but impelment within a hard ddl -> discuss and choose one.
* **Same logic but in traffic sign autolabeling. One is quick and dirty(short term gain), another is systematic(long-term gain) but may miss deadline. break down tasks and reduce dev time result is prioritize work and make it before deadline**

1. Tell me a time when you disagreed with a colleague.
2. Tell me a time when you had to work on a project with unclear responsibility[Ownership]