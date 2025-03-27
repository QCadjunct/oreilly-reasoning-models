Improved Approach for DeepSeek-R1

Started with cold-start data: Unlike R1-Zero, they collected thousands of high-quality chain-of-thought examples to fine-tune the base model before applying RL.

Applied reasoning-oriented RL: After fine-tuning, they applied large-scale reinforcement learning focused on enhancing reasoning capabilities.

Added language consistency reward: To prevent language mixing, they introduced a reward for maintaining consistent language throughout responses.
Performed rejection sampling and SFT: When RL training converged, they:

Generated samples using the trained model
Kept only the correct responses
Combined them with non-reasoning data from DeepSeek-V3


Conducted a second round of fine-tuning: They fine-tuned the base model again using the curated dataset of about 800,000 samples.
Applied a second round of RL: They implemented another RL stage to further align the model with human preferences, balancing helpfulness, harmlessness, and reasoning capabilities.