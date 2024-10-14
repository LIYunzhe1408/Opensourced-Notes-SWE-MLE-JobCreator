# Prompt Hacking
Prompt hacking relies on **carefully crafting prompts** to deceive the LLM into performing unintended actions

Three types of hacking:

* prompt injection
* prompt leaking
* jailbreaking

Overall, prompt hacking is a growing concern for the security of LLMs, and it is essential to remain vigilant and take proactive steps to protect against these types of attacks.

## Prompt injection
Prompt Injection is the process of overriding original instructions in the prompt with special user input
![](./Figures/prompt_injection.png)

### A Real world Example of Tweets reply
A remote work company (remoteli.io) created a Twitter bot that would respond positively to Tweets about remote work. This bot was powered by an LLM and users quickly found ways to trick it into saying whatever they wanted.

In the image, the user Evelyn created an adversarial input, the last line of which instructed the bot to make a threat against the president.

Upon reading this Tweet, the bot included Evelyn's input into its LLM prompt and was prompt injection into making a threat against the president!
![img.png](Figures/tweetsReply.png)

### Conclusion
Prompt Injection arises from the fact the current transformer architectures are not able to distinguish between original developer instructions and user input instructions. It is conceivable that future models will be able to distinguish between these two types of instructions, but even this would not be guaranteed to stop prompt injection. As it is, prompt injection is very difficult to stop, and it will likely continue to be a problem for the foreseeable future.

### Further Q&A
1. Can prompt injection be entirely prevented?

    Due to the nature of current transformer architectures, prompt injection cannot be completely prevented. The AI models we have today are unable to distinguish between user input instructions and developer instructions. While research is being done to mitigate this problem, there is no foolproof solution yet.
   

## Prompt Leaking
Prompt leaking is a form of prompt injection in which the model is asked to spit out its own prompt.

* In Goal Hijacking, the attacker changes `user_input` to print malicious instructions.
* In Prompt Leaking, the attacker changes `user_input` to attempt to return the prompt
![img.png](Figures/PromptLeaking.png)
  
Well, so what? Why should anyone care about prompt leaking?

Sometimes people want to keep their prompts secret. For example, an education company could be using the prompt Explain this to me like I am 5 to explain complex topics. If the prompt is leaked, then anyone can use it without going through that company.

## Jailbreaking
Jailbreaking is the process of getting a GenAI model to perform or produce unintended outputs through specific prompts