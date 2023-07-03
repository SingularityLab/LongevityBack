```python
import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def generate_advice(user_info, test_results):
    prompt = f"This person's information is as follows: {user_info}. Their test results are: {test_results}. What advice can you give to improve their quality of life and longevity?"

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.5,
        max_tokens=200
    )

    advice = response.choices[0].text.strip()
    return advice
```