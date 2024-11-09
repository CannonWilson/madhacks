import time
import json
import pandas as pd
from utils import MODELS, get_model_response, get_win_rate

# Load the tasks dataset
with open("tasks.json", "r") as file:
    dataset = json.load(file)

# Create empty dataframe to record experiment data
columns = []
for model in MODELS:
    for metric_name in ["price", "latency", "win_rate"]:
        columns.append(f"{model}:{metric_name}")
df = pd.DataFrame(columns=columns)

# Run experiment
for task in dataset:
    new_row = {}
    for model in MODELS:

        # Time how long it takes this model to answer the task prompt
        start = time.time()
        response = get_model_response(model, task["prompt"])
        end = time.time()

        # Get info about model response for task
        res_json = response.json()
        model_cost = (
            model.input_cost * res_json["usage"]["prompt_tokens"]
            + model.output_cost * res_json["usage"]["completion_tokens"]
        )
        model_latency = end - start

        # Get win rate compared to reference model
        win_rate = get_win_rate(
            model=model,
            model_output=res_json["choices"][0]["message"]["content"],
            prompt=task["prompt"],
        )

    # new_row[f"{model}:latency"] = end-start
    # new_row[f"{model}:price"] =
    # res_json = response.json()
    # df.loc[len(df)] =
    # latencies[task["uid"]][model] = end - start
# outputs[task["uid"]][model] = res_json["choices"][0]["message"]["content"]
# tokens[task["uid"]][model] = res_json["usage"]["total_tokens"]
