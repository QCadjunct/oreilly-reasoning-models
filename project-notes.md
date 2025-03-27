Course link: https://www.oreilly.com/live-events/working-with-o1-deepseek-and-gemini-20-reasoning-capabilities/0642572015593/

# Tasks
|                   |                           |                                                         |
| ----------------- | ------------------------- | ------------------------------------------------------- |
| Stage             | Traditional LLM           | Thinking Model (DeepSeek-R1)                            |
| Pretrain          | Internet-scale corpus     | Same                                                    |
| SFT               | Human-annotated QA        | Chain-of-Thought (CoT) data                             |
| RL                | Helpfulness/safety reward | Reasoning reward + Format reward + Language consistency |
| Emergent Behavior | Few CoTs                  | Self-verification, long CoTs, reflection                |
- [x] <span style="color: red">What defines/constitutes a reasoning/thinking model?</span> 
- [x] <span style="color: red">How do they differ from a traditional LLM like gpt-4o?</span> 
	- [x] [[how reasoning models effectively differ from traditional llms]]
- [x] <span style="color: red">Why use reasoning models why are they relevant?</span> 
	- First because the performance gap between OSS and proprietary models has decreased significantly
		- [[AI Review Highlights 2024.pdf#page=5&selection=0,1,50,62|AI Review Highlights 2024, page 5]]
- [x] <span style="color: red">What matters when choosing an LLM? </span> 
	 - reasoning quality, embedded knowledge, and context window [[AI Review Highlights 2024.pdf#page=10&selection=60,0,61,1|AI Review Highlights 2024, page 10]]  [[AI Review Highlights 2024.pdf#page=8&selection=0,0,4,55|AI Review Highlights 2024, page 8]]
- [x] <span style="color: red">What are they being used for?</span> 
	- People use them for information retrieval, text generation, summarization, chatbots, text structuring and classification [[AI Review Highlights 2024.pdf#page=11&selection=0,0,57,14|AI Review Highlights 2024, page 11]]
- [x] <span style="color: red">How to prompt Thinking Models?</span>
	- [Read this first to set stage for arguments](https://www.latent.space/p/o1-skill-issue)
	- [[How to prompt Large Thinking & Reasoning models?]]
		- [Prompting O1](https://www.latent.space/p/o1-skill-issue)
	- [[Gregory Brockman tweet about LLMs]]
		- [[how to prompt reasoning models - o1]]
- [x] [Summarize instructively this entire video and extract articles mentioned](https://www.youtube.com/watch?v=f0RbwrBcFmc)
- [x] <span style="color: red">What are the concrete limitations of thinking models and how should we think about them when building with these models?</span> 
	- [x] Read - [[LLMs limitations on thinking and reasoning]]
- [x] <span style="color: red"> What is the role of distilled models when planning an implementation?</span> 
	- [x] **Distilled Models**
	  * DeepSeek-R1-Distill-Qwen-32B outperforms OpenAI-o1-mini across various benchmarks [8]
	  * Smaller models can retain impressive reasoning capabilities through knowledge distillation [9]
	  * The Llama-70B distilled model achieves 94.5% accuracy on MATH-500 and 86.7% on AIME 2024 [10] 
* [ ] <span style="color: red">How to integrate them into workflows?</span> 
* [ ] <span style="color: red">Read through all the bites</span>
* [ ] Feedback loop
	* [x] <span style="color: red">what is the best way to normalize the factors when deciding between a model?</span> 
	* [ ] <span style="color: red">add a better more descriptive intro to the trainine/architecture behind the different reasoning llm options</span> 
	* [ ] <span style="color: red">Turn that decision making matrix into a jupyter notebook</span> 
	* [ ] [from this paper what is exactly the way in which they prove llms were not really reasoning?](https://arxiv.org/pdf/2305.18654)
	* [ ] and the counter factual paper? what was the main argument and point?
	* [ ] Read and delete the complement info in the whiteboard and integrate if necessary (same with notes, process and compile them in the notes folder adding structure and organization)
	* [ ] Redo that part about structured outputs justify it better is it traceable reasoning tece stuff?

# Bites
- [[how reasoning models effectively differ from traditional llms]]
- [[How to choose between regular models and 'reasoning' models]]
- [Grok3 model](https://x.com/mckaywrigley/status/1892347064673038457)
- https://www.latent.space/p/o1-skill-issue?utm_campaign=post&utm_medium=web
- [[LLMs limitations on thinking and reasoning]]
- [[prompting reasoning models]]
- [for writing code](https://x.com/mattshumer_/status/1891531012674302331?s=46&t=CSmFBRRX097Mpa7XSLa7uw)
  * [Quick tips for getting better performance from o1-series models](https://www.tiktok.com/@answer.hq/video/7460595621313908011)
[[mini report reasoning models]]
- [[special performance of reasoning models]]
- [[specialized training of reasoning models like o1 or deep seek r1]]
- Relevant models for reasoning & Knowledge (MMLU)
	1. [Specialized example](https://huggingface.co/papers/2412.18925)
	2. [[AI Review Highlights 2024.pdf#page=4&selection=75,0,77,6|AI Review Highlights 2024, page 4]]
  * Uses chain-of-thought prompting where models reason iteratively through problems [4]
  * Establishes benchmarks for reasoning capabilities in math, science, and coding tasks [5]
  * DeepSeek-R1 demonstrates that reinforcement learning without supervised fine-tuning can achieve strong reasoning capabilities [2]
  * [[Reasoning models leaderboard from artificial analysis]]
  * Uses a rule-based reward system that helps models improve reasoning over time [6]
- **Hugging Face Open-R1 Project** Aims to build missing pieces of the R1 pipeline for open reproduction [11]
	  * Includes scripts to train, evaluate, and generate synthetic data [11]
	  * First step: Replicate R1-Distill models by distilling high-quality reasoning datasets from DeepSeek-R1 [12]
- [[deep seek r1 vs o1]]
- **Model Evaluation Standards**
  * OpenAI's o3 model has set new benchmarks for evaluating human-level intelligence in AI systems [18]
  * Testing methodologies for reasoning capabilities continue to evolve [18]
  * Open-source models are rapidly approaching proprietary model performance [19]
# References
- 
![[Pasted image 20250112222502.png]]
# References
[1] https://unfoldai.com/deepseek-r1/
[2] https://huggingface.co/deepseek-ai/DeepSeek-R1
[3] https://newsletter.languagemodels.co/p/the-illustrated-deepseek-r1
[4] https://www.techtarget.com/whatis/feature/OpenAI-o1-explained-Everything-you-need-to-know
[5] https://platform.openai.com/docs/guides/reasoning-best-practices
[6] https://www.datacamp.com/blog/deepseek-r1-vs-v3
[7] https://textcortex.com/post/deepseek-r1-vs-o1
[8] https://github.com/deepseek-ai/DeepSeek-R1
[9] https://github.com/huggingface/open-r1
[10] https://www.datacamp.com/blog/deepseek-r1
[11] https://github.com/huggingface/open-r1/blob/main/README.md
[12] https://github.com/huggingface/blog/blob/main/open-r1.md
[13] https://techcrunch.com/2025/01/27/deepseek-claims-its-reasoning-model-beats-openais-o1-on-certain-benchmarks/
[14] https://blog.promptlayer.com/openai-o3-vs-deepseek-r1-an-analysis-of-reasoning-models/
[15] https://indianexpress.com/article/technology/artificial-intelligence/deepseek-r1-a-reasoning-model-that-beats-openai-o1-9791318/
[16] https://sebastian-petrus.medium.com/developing-rag-systems-with-deepseek-r1-ollama-f2f561cfda97
[17] https://ollama.com/library/deepseek-r1
[18] https://www.nature.com/articles/d41586-025-00110-6
[19] Referenced in multiple sources including LinkedIn posts from tech leaders
[20] - [Building a Research Assistant with O3-mini](https://www.youtube.com/watch?v=8-rEFXgMSTk&t=216s)