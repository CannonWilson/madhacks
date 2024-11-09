import requests
import json

response = requests.post(
  url="https://openrouter.ai/api/v1/chat/completions",
  headers={
    "Authorization": f"Bearer {'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'}",
    # "HTTP-Referer": f"{YOUR_SITE_URL}", # Optional, for including your app on openrouter.ai rankings.
    # "X-Title": f"{YOUR_APP_NAME}", # Optional. Shows in rankings on openrouter.ai.
  },
  data=json.dumps({
    "model": "nousresearch/hermes-3-llama-3.1-405b:free", # Optional
    "messages": [
      {
        "role": "user",
        "content": "Please aggregate the following data from sales reports and summarize the total sales per region:\n'Region, Sales\nNorth, 1000\nSouth, 1500\nNorth, 1200\nEast, 800\nSouth, 1300\nWest, 950'"
      }
    ]
  })
)

print(response.json())
