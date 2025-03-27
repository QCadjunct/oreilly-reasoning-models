# Understanding Reasoning Models (O1 & O3)

## Core Differences Between Chat Models vs. Reasoning Models

### Training Paradigms
- **Chat Models**: Trained using next token prediction (system 1 thinking - fast, intuitive)
- **Reasoning Models**: Trained using reinforcement learning over Chain of Thought (system 2 thinking - slow, effortful)

### Prompting Approach
- **Chat Models**: Tell the model HOW to think ("Think step by step," "Act as an engineer")
- **Reasoning Models**: Tell the model WHAT you want (focus on goals and desired output format)

### Interaction Style
- **Chat Models**: Interactive, conversational, pulling context from user over time
- **Reasoning Models**: Non-conversational, best for "wormholing" on a detailed task without interaction

## How Reasoning Models Work
- Use reinforcement learning on Chain of Thought
- Training process:
  1. Start with data containing verifiably correct answers (coding, math problems)
  2. Model generates multiple solution trajectories
  3. A grader verifies correct answers
  4. Model weights are nudged to favor correct Chain of Thought paths
  5. Over time, model learns to produce better reasoning paths

## Using Reasoning Models
- Don't prompt like chat models
- Use "anatomy of an O1 prompt":
  - Explicit goal
  - Return format
  - Context (dump all your data)
- API parameters:
  - Reasoning effort: low/medium/high (tunes reasoning depth vs. speed)
  - O1 Mini doesn't support system messages

## Key Use Cases for Reasoning Models
- **Coding**: One-shotting entire files or sets of files
- **Planning & Agency**: Upfront planning for agentic workflows
- **Deep Reflection**: Analysis of meeting notes, documents, papers
- **Data Analysis**: Medical diagnostics, data interpretation
- **Research & Report Generation**: Deep research on complex topics
- **LLM as Judge**: Evaluation steps in workflows
- **Cognitive Layer for News Feeds**: Monitoring trends, summarizing information

## When to Use Reasoning Models
- Background tasks where latency isn't critical
- Complex problems requiring deeper thinking
- Tasks benefiting from extensive reasoning
- Research and planning-heavy workflows
