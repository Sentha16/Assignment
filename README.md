Assignment 8 - AI Research engineer (agentic reasoning & tool use)

I. Non-Coding Component
A. Conceptual map:
1.	Reasoning and Acting (ReAct):
o	Reasoning: Chain-of-thought prompting, reasoning traces.
o	Acting: Interfacing with external sources.
o	Workflow: Act -> Observe -> Reason -> Act 
2.	Toolformer: This is a LLM with tooling module with self-taught tool use
o	Tool Use: Deciding which APIs to call, when to call them, and how to incorporate results.
o	Workflow: Using Self-supervised learning, zero-shot performance improvement.
3.	ReST meets ReAct: Emphasize the interleaving of reasoning with explicit action calls, using chain-of-thought augmented by tool invocations.
o	Reasoning and Acting: Multi-step reasoning, integrating external knowledge.
o	Workflow: Iterative training on previous trajectories, reinforcement learning with AI feedback.
4.	Chain of Tools: 
o	Tool Use: Automatic multi-tool learner.
o	Workflow: Learning to use multiple tools, integrating tool outputs.
5.	Language Agent Tree Search:
o	Reasoning, Acting, and Planning: Unifying these components in LLMs.
o	Workflow: Tree search for optimal reasoning and action sequences.






B. Analysis

Paper	Agent Design	Reasoning steps	Tool Use	Real world application

ReAct	Interleaved reasoning and action steps	Chain-of-thought prompting	Wikipedia API	Improved performance on question answering and decision-making tasks

Toolformer	Self-supervised learning to use tools	Deciding which APIs to call	Calculator, Q&A system, search engines, translation system	Improved zero-shot performance across various tasks
ReST meets ReAct	Iterative training with reinforcement learning	Multi-step reasoning with external knowledge	External knowledge sources	Comparable performance with fewer parameters
Chain of Tools	Automatic learning of multiple tools	Integrating tool outputs	Multiple tools	Versatile tool integration for multi-step operations, such as complex data processing or task automation.
Language Agent Tree Search	Unifying reasoning, acting, and planning	Tree search for optimal sequences	Multiple tools	Comprehensive approach to task-solving


