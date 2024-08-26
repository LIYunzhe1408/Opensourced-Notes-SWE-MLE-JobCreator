  **The original review is written in Chinese, then translated by GPT-4o and checked by myself.**

# Introduction
- Title: From the idea to the product 从点子到产品：产品经理的价值观与方法论
- Author: Fei Liu 刘飞
- Publisher: 电子工业出版社
- Publish date: 2017.1
- ISBN: 978-7-121-30286-2

This book, from the perspective of a product manager, introduces the values and practical methodologies that a product manager needs throughout the entire cycle from idea to product. It helps better define product features, analyze requirements, foster team collaboration, and manage updates and iterations. In my view, this not only aids product managers in quickly getting started but also serves as a valuable supplement of soft skills for tech professionals, entrepreneurs, and student team leaders. It broadens their approach to considering problems, thinking through issues, and finding solutions. If you’re looking for a roadmap to turn ideas into products, this book offers a comprehensive approach from conceptualizing ideas to creating actionable plans, along with management and collaboration techniques for producing usable products.


# Summary
A successful product creates value and solves the pain points of users. Based on the analysis of user requirements, features align with what users really want. To smoothen the implementation heading for requirements, the PM should clarify how to manage files, stages, and working streams. Then the entire team works on it, and some tricks in problem-solving, communication, and personal growth boost the whole life cycle.

Key word: 方法论 methodology；价值观 values；工作流 Workflow

# Evaluation and Commentary
以互联网为例，任何产品的意义是“满足用户各式各样的需求，从而创造价值”，需要有人对用户体验需求正确分析、 协调推动产品出现，从而解决用户问题的同时，保证公司的战略目标顺利达成。

如何从核心价值出发launch一个产品？在讨论想法和点子时，先要讨论产品模型来判断在思路层面是否合理，即：需求实现的逻辑，是不是行得通。考虑产品设计的合理性（判断方法论：产品模型验证矩阵如表x所示）、盈利模式合理性、拓展合理性和实施合理性，不能只看到高楼大厦的光鲜，而不考虑背后施工队的状况。基于上述合理性的判断，显然想到什么需求就做什么是不合理的，要发现产品的核心价值，到底如何可以解决用户的问题，核心价值要清晰，帮助用户用完即走！用户的问题要分析清楚，明确到底要解决的是不是问题。解决时最好可以超出用户预期。想法和核心价值评判清晰后，可以通过Minimal Viable Product来快速、低成本验证产品模型和商业模式是否可行，通过：1.是否满足用户需求；2.是否能创造商业价值。越是早期的产品或模块，就越是要关注核心功能，而非面面俱到。因为，为了确保产品模型设计的功能得到用户认可，将其快速投入市场中进行验证是最妥当的方法；且产品的核心价值是解决用户问题，只要能解决问题，越快提供给用户，就能越快获得这些用户，产品会在不断优化中更好击中用户痛点。MVP需要产品模型的思考，它需要在理论上成立，在实践中证明。MVP务必确保其功能清晰到用一句话就能说清楚。

MVP验证成功后，需要继续根据用户进一步的需求进行完善。首先，在深挖需求时，区分Want and Needs，前者是希望在产品中看到的功能，而Needs则是确定的具体问题需要产品去解决，由此关心需求背后真正的诉求。获取这种需求的方法，可以通过用户研究，它能够协助我们理解用户，并以研究得到的结论，指导我们设计产品和优化产品的方法，一般通过定性和定量两个方面获取信息，输出结论。用户研究过程中，始终牢记：让自己成为真正的用户去设计产品，设计，永远不应该坐在办公室里做！！再进一步，确认解决用户需求后，需要考虑用户体验，用户体验关注的是让产品友好地满足用户需求，让用户通过产品，满足需求的同时足够方便、舒适和快捷。11个原则以供参考：
1. 可见原则（“哦？这里不应该有介绍吗？”东航查询失败毫无提示原因）；
2. 场景贴近原则（滴滴出行的大图标）；
3. 可控原则（Home键提升用户安全感）；
4. 一致性（粉丝-关注者等用词）；
5. 防错防呆原则（有足够的提醒，不让用户犯错和发呆）；
6. 协助用户记忆原则（支付前确认订单）；
7. 简约易读原则（切忌花哨）；
8. 容错原则（提供撤销功能和强烈提示）；
9. 帮助和提示（考虑需要进行复杂操作的情况并提示，如游戏中做任务，在卡关可能场景中出提示接口，而不是放一个完整的帮助文档）；
10. 灵活高效原则（微信点击加号弹出刚拍的照片=预判用户下一步的动作）
11. 恢复现场原则（知乎网页版编辑的自动保存；iOS返回上一界面）


开发产品过程中，对于文档、需求更新、工作流的管理对产品性能影响显著。对于产品的管理者，需要熟悉解决问题的手段（例如设计的架构、信息流动、数据结构），但不一定需要能立马上手实现（Suspect）。
- 文档：文档的作用是高效传递产品管理者对产品功能的描述并记录。好的文档应满足：没有逻辑不通的表达和逻辑不明的内容安排；没有未定义清楚的细节；直观的可读性。通常，可以先尝试以一页纸，描述清楚需求来源、开发时间线、涉及技术点和人员即可，文档体系成熟、人员熟悉后，再逐步删改文档结构。
- 需求：需求的生命周期决定了产品的设计到实现。需求的处理分为几个阶段：获取需求-讨论和分配-可行性评审-开发-复盘。需求的获取应当做判断和记录，方便回溯。判断依据是
    1. 需求本身的重要性（登录写为登陆重要，还是奖励15写成50重要）
    2. 来源（是否是目标用户）
    3. 需求背景（是否说清原因；是否说清逻辑；是否实际遇到）。
   
   采用问题+方案的形式记录（xx在用xx功能时，感觉xx，我们可以尝试xx）。讨论的通常是需求优先级。可以用四象限法则或KANO模型合理考量和说服他人。具体的讨论方法、分配、可行性评审见文末support material/文档管理/需求
- 工作流：避免：1.你做的事情应该是别人做的；2.你做的事情有避免重复劳动的方法。作为船长，你可以不去做水手的工作，但不能不理解水手的工作。协作过程中：遇到问题要让大家在情理都可以接受的范围内解决掉，而不是从逻辑上证明谁对谁错。


管理产品完整周期过程中，该书作者还提出了一些技巧和方法，我认为不仅对产品，对于管理自己的人生也有一定指导意义。任何达不到预期的事情，都要考虑是不是真实需要解决的。
- 处理问题：我们要主动发现问题：问题的提出需要有问题的背景，问题涉及的人和解决问题的预期！分析问题时，要善于抽象问题，即发现导致复杂问题发生的本质（如前述对深层需求的挖掘一样），运用逻辑分析时，要注意一些thinking trap（anchor trap, sunk-cost trap…）。发现问题和分析问题时面向的是事，而解决问题面向的，则是人。按层次、步骤、逻辑，将复杂问题拆分为一个个小问题，单独解决的效率会高很多。针对每个问题设计的解决方案，要包含
  1. 问题和背景以加深理解；
  2. 不模棱两可的方案内容；
  3. 方案的负责人；
  4. 方案的阶段性（和前述拆分子问题对应，为子问题设立目标，阶段性验证。OKR工具）

    目标和验证方法以评判达到怎么样的效果算可以。最后推动执行，确保协作者获取到所有信息并了解协作者的态度，定期关注并检验效果和复盘。
- 沟通：好的沟通能力是
    1. 快速准确理解他人表达的信息；
    2. 准确通畅地表达自己想传递的信息；
    3. 理解和表达中就事论事，也能照顾他人的情绪。
    要善于区分事实（已经发生的事实）和观点（带有主观色彩），通常接受和相信事实，吸纳为自己的信息，while对观点保持怀疑，同时，可以通过让对方重述（SRM很好用）确保对方理解。沟通的心态：发现协作方言语和举止的怪异或者让你有疑惑，最好的方式就是找他沟通一下，聊一聊，不要贸然下判断和过度解读。
- 审美：如果一个作品足够美，那大家喜欢它的角度可能不同，但如果很丑，懂的审美人就能找到同一个丑的地方。逛逛dribbble, Behance的设计师网站。

最后的最后，对于兴趣和热情，产品或团队的管理者要有责任心
- 不缺席重要场合（重要节点的配研发人员熬夜、重要比赛场合等）。任何“可能需要”他在的场合，他都应该在。
- 排除影响进度的问题（组长和管理层对设计方案吵架，主动劝和，否则影响进度）
- 主动填充缺失环节，某件事情没有人做但又需要人去做的时候，能充当临时替补（如经纬汇搬椅子、摆摊看摊位、货拉拉搬航空箱）

当每次想说没有兴趣的时候，要反思是不是只是因为遇到了困难。很重要，多次想要退队的根因。克服掉这一次的困难，再不断去尝试克服更多困难，长期以往，就发现在这件事情上足够擅长了。



