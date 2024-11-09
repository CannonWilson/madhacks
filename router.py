import time
import json
import pandas as pd
from utils import MODELS, get_model_response, compare_model_to_reference, get_output_from_response

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

        # Compare model to reference model
        compare_model_to_reference(
            model=model,
            model_output=get_output_from_response(response),
            prompt=task["prompt"],
        )

    # new_row[f"{model}:latency"] = end-start
    # new_row[f"{model}:price"] =
    # res_json = response.json()
    # df.loc[len(df)] =
    # latencies[task["uid"]][model] = end - start
# outputs[task["uid"]][model] = res_json["choices"][0]["message"]["content"]
# tokens[task["uid"]][model] = res_json["usage"]["total_tokens"]
