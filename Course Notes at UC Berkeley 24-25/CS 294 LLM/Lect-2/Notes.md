Level
1. text agent
2. LLM agent: use LLM to act
3. reasoning agent: uses LLM to reason to act


Before LLM, RL in specific domain. One domain, one trained model.

LLM:
- Reasoning: zero-shot CoT
- Acting: Game, robotics (LLM agent but not reasoning agent)

ReAct: integrating together -> reasoning agent


# QA task
- computational way: generting program -> answer
- Retrival: retrivaor + corpora -> search (what if the qustion is not included in the corpora)
- Tool use: special token for invoking tool calls

Simple and unifying solution?
- Reasoning through LLM and observation from actions
- Motivation: thought + action -> observation -> thought + action -> observation -> ... More info, think more.


Everything can be turned into text games.
- If just have acting without reasoning, stuck in one tough situations or border case.

 - Traditional agents:action is defined by the env
- ReAct: action space is the union set augmented by reasoning(infinte space of language).

# Long-term Memory
- short-term memory: limited context; do not persist over new tasks. (Golden Fish, solve critical math, but forget quickly. What a shame)
- long-term memory: read and write; store experience, skills; persist over new experience
  - Reflexion: reflect on coding and failure. RL with agent
    - Traditional RL: reward + updates on weight
    - Relfexion: learn via text feedback; learning by updating language
  - LLM is a form of long-term memory. Agent can learn and retieve from it.
  - Then Reason from short-term memory


# Beyond questions and games?
- Digital automation: file reports(SAP), code experiments(VS Code), explore papers(arxiv)
- Benchmark is needed. should be scalable and practical in real-world challenges.
  - WebShop: 
    - large-scale complex env based on1.16M Amazon producs
    - Automatic reward based on instuction
  - Web arena
  - SWE Bench
    - input: a repo and file
    - output: a file diff to run
    - Evaluation: unit tests from pull request
- Code, Software, internet is practical and scalable, compared to robots(expensive, practical but not scalable) and game(sim to real is hard, scalable but not practical)

# Takeaways
- Think in abstration.
- Familiarity with tasks (not task-specific methods!), supporting abstraction.
- Learning history and other subjectss

# Future
* Training
  * LLM is not trained for agents. Not train but prompting. 
  * Prompt for agents to generating data, then fine-tune the model.
* Interface: env for agent
  * Optimize the env instead of optimizing agent self. (writing code)
  * summarized search(give 10 possible answers) for agents instead of "cd, ls" or iterative search which is intuitive for human.
* Robustness: real life
  * [Expected solve 1000 in 1000 times]"Would I fail one time of 1000 times"(lose customer)
  * [Not Expected Anymore]"Can I solve one time of 1000 times"
  * GM test cases. PF or TF
* Human: with human
* Benchmark: how to build


# Question
1. Ambiguous questions
   - can you evaluate, hard
   - can you immprve, hrad
2. To educate human and to be more interpretable.