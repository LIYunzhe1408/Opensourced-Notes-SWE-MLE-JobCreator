AI prototype is easy to make  but hard to be made reliable


controllable and improve modularly
Use dspy to make a verdict: `dspy.chainofThought`

### Multi-hop generation
```python
# define the strategy for expressing a signature
dspy.ChainOfThought("context, question -> query")
dspy.ChainOfThought("context, question -> answer")

for i in range(hops):
    query = generate_query(context, question)
    context +=dspy.retrieve(query)
answer = generate_answer(context, question)
```