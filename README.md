# Intelligent Routing System for Language Models

## Project Overview

This project develops an intelligent router designed to direct user prompts to the most suitable Large Language Model (LLM) based on performance, latency, and cost. The router analyzes the prompt, generates a task description using a language model, and subsequently selects the optimal model using a sophisticated ranking system.

### How It Works

1. **Prompt Reception:** Upon receiving a user prompt, it's passed to a designated language model that succinctly describes the task in natural language.
2. **Task Embedding:** This description is converted into an embedding using an efficient variant of BERT (e.g., DistilBERT, AlBERT).
3. **Clustering:** Task embeddings are clustered using algorithms like DBSCAN or k-means to identify the cluster with the closest center.
4. **Model Ranking:** Each cluster center has associated model rankings based on three dimensions (performance, latency, cost). User preferences are used to select the best model from these rankings.
5. **Update Mechanism:** When updating clusters, new task embeddings are used for clustering. Each model is then re-ranked using a judge model in comparison to a reference model, with associated costs and latencies recorded.

## Major Tasks

### Dataset

- **Task/Prompt Collection:** Creation of a dataset consisting of various tasks/prompts.
- **Model Interaction:** Integration with openrouter.ai to call all 11 models mentioned in the routerbench paper.
- **Ranking Development:** Establishment of human rankings for all models across each task.

### Model Rankings

- **Task Description Model Selection:** Decide on the task description model, options include LLAMA, fast claude, etc.
- **Embedding Model Decision:** Choose an appropriate embedding model such as DistilBERT or AlBERT.
- **Clustering Implementation:** Evaluate and possibly adapt clustering methods like k-means and DBSCAN.
- **Prompt Recording:** Document prompts for cluster centers.
- **Judging System:** Develop a system to assess prompt suitability using a judge model while also recording cost and latency.
- **Model Selection:** Implement a model selection system that incorporates task/prompt rankings and user preferences.

### Deployment

- **Containerization:** Package the system into a container for deployment.
- **Cloud Deployment:** Deploy the system on Google Cloud, equipped with a cron job for regular updates.

## Installation

```bash
git clone https://github.com/yourgithubrepo/intelligent-routing-system.git
cd intelligent-routing-system
# Follow setup instructions here
