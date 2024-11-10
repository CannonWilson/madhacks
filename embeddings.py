"""
Decide on task description model (i.e. LLAMA, fast claude, etc.)
Decide on embedding model (i.e. DistilBERT, AlBERT, etc.)
Perform clustering, compare k-means and DBSCAN (adaptive clustering?)
Record prompts for cluster centers
"""

import time
from transformers import DistilBertTokenizer, DistilBertModel, AutoTokenizer, AutoModelForCausalLM, AutoModelForSeq2SeqLM
from utils import Model, M_TOKENS, get_model_response, get_output_from_response

example_prompt = "Please summarize the following article into 3-5 key bullet points:\n\n'The global economy is showing signs of recovery as markets rebound and consumer confidence increases. Experts attribute this to successful vaccination programs and government stimulus packages. However, concerns remain over potential inflation and supply chain disruptions."

_TASK_FROM_INPUT_PROMPT =  """
Given a prompt, describe the main task it is trying to achieve.
Be concise.

Prompt: 

{user_input}

Task Description:
"""

# mistral tiny does not do well, takes a long time
# google/gemini-flash-1.5-8b is 0.5-0.6 seconds
# meta-llama/llama-3.2-1b-instruct is 0.4-0.6 seconds
# _TASK_FROM_INPUT_MODEL = Model(
#     name="meta-llama/llama-3.2-1b-instruct", # fast, lightweight model
#     input_cost=1.0 / M_TOKENS,
#     output_cost=2.0 / M_TOKENS,
# )
# start = time.time()
# example_task_from_prompt_response = get_model_response(_TASK_FROM_INPUT_MODEL, _TASK_FROM_INPUT_PROMPT.format(user_input=example_prompt))
# end = time.time()
# print(f"example_task_from_prompt_response took {end-start} seconds.")
# example_task_from_prompt = get_output_from_response(example_task_from_prompt_response)

model_name = "google/flan-t5-small" # can't get access: "meta-llama/Llama-2-7b-chat-hf"  # Example for 7B chat model

# Load tokenizer and model
# tokenizer = AutoTokenizer.from_pretrained(model_name)
# model = AutoModelForCausalLM.from_pretrained(model_name, token="")
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
user_input = _TASK_FROM_INPUT_PROMPT.format(user_input=example_prompt)
start = time.time()
inputs = tokenizer(user_input, return_tensors="pt")
outputs = model.generate(**inputs, max_new_tokens=50)
response = tokenizer.decode(outputs[0], skip_special_tokens=True)
end = time.time()
print(f"response from prompt->task model: {response}, took {end-start} seconds")

# Load embedding model
tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-uncased")
model = DistilBertModel.from_pretrained("distilbert-base-uncased")

# Generate embedding for task
start = time.time()
inputs = tokenizer(user_input, return_tensors="pt")
outputs = model(**inputs)
embeddings = outputs.last_hidden_state
end = time.time()
print(f"Getting embeddings took {end-start} seconds")
print(embeddings.shape)