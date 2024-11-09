import requests
import json
from typing import Dict, Any

M_TOKENS = 1e6


class Model:
    def __init__(self, name, input_cost, output_cost):
        self._name = name
        self._input_cost = input_cost
        self._output_cost = output_cost

    @property
    def name(self):
        return self._name

    @property
    def input_cost(self):
        return self._input_cost

    @property
    def output_cost(self):
        return self._output_cost


# From routers used in RouterBench paper:
# could not find "WizardLM/WizardLM-13B-V1.2",
# 404: "anthropic/claude-instant-1.0", # "claude-instant-v1",
# 404: "anthropic/claude-1", # "claude-v1",
# included: "anthropic/claude-2",  # "claude-v2",
# included: "openai/gpt-3.5-turbo-1106",  # "gpt-3.5-turbo-1106",
# included: "openai/gpt-4-1106-preview",  # "gpt-4-1106-preview",
# 404: "meta-llama/codellama-34b-instruct", # meta/code-llama-instruct-34b-chat
# 404: "meta-llama/llama-2-70b-chat", # meta/llama-2-70b-chat
# included: "mistralai/mistral-7b-instruct",  # "mistralai/mistral-7b-chat"
# included: "mistralai/mixtral-8x7b-instruct",  # "mistralai/mixtral-8x7b-chat"
# 404: "01-ai/yi-34b-chat" # "zero-one-ai/Yi-34B-Chat"

MODELS = [
    Model(
        name="anthropic/claude-2",
        input_cost=8.0 / M_TOKENS,
        output_cost=24.0 / M_TOKENS,
    ),
    Model(
        name="openai/gpt-3.5-turbo-1106",
        input_cost=1.0 / M_TOKENS,
        output_cost=2.0 / M_TOKENS,
    ),
    Model(
        name="openai/gpt-4-1106-preview",
        input_cost=10.0 / M_TOKENS,
        output_cost=30.0 / M_TOKENS,
    ),
    Model(
        name="mistralai/mistral-7b-instruct",
        input_cost=0.055 / M_TOKENS,
        output_cost=0.055 / M_TOKENS,
    ),
    Model(
        name="mistralai/mixtral-8x7b-instruct",
        input_cost=0.24 / M_TOKENS,
        output_cost=0.24 / M_TOKENS,
    ),
]


def get_model_response(model: Model, prompt: str) -> requests.Response:
    """
    Sends a prompt to the OpenRouter API and retrieves the response from the specified model.

    Returns:
        requests.Response: The response object returned by the OpenRouter API, which contains the generated
            HTTP response. Check result of this function with .json() or .status_code
    """

    return requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": "Bearer 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"
        },
        data=json.dumps(
            {
                "model": model["name"],
                "messages": [{"role": "user", "content": prompt}],
            }
        ),
    )


def get_win_rate(model: Model, model_output: str, prompt: str):
    """
    TODO
    """
    pass
