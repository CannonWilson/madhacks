# Intelligent Routing System for Language Models

## Project Overview

This project develops an intelligent router designed to direct user prompts to the most suitable Large Language Model (LLM) based on performance, latency, and cost. The router analyzes the prompt, generates a task description using a language model, and subsequently selects the optimal model using a sophisticated ranking system.

### How It Works

1. **Prompt Reception:** Upon receiving a user prompt, it's passed to a designated language model that succinctly describes the task in natural language.
2. **Task Embedding:** This description is converted into an embedding using an efficient variant of BERT (e.g., DistilBERT, AlBERT).
3. **Clustering:** Task embeddings are clustered using algorithms like DBSCAN or k-means to identify the cluster with the closest center.
4. **Model Ranking:** Each cluster center has associated model rankings based on three dimensions (performance, latency, cost). User preferences are used to select the best model from these rankings.
5. **Update Mechanism:** When updating clusters, new task embeddings are used for clustering. Each model is then re-ranked using a judge model in comparison to a reference model, with associated costs and latencies recorded.

### LLM Ranks

1. **Task/Prompt Collection:** Creation of a dataset consisting of prompts from 25 tasks.
2. **Model Interaction:** Integration with openrouter.ai to call all 5 models, including Claude-2, ChatGPT-3.5-turbo, ChatGPT-4, Meta-Llama34b and Meta-Llama-2-70b.
3. **Ranking Development:** Establishment of human rankings and LLM judges for all models across each task. We avoid position bias by letting the judge model judge the performances of two LLMs 6 times. Ties will be skipped.


