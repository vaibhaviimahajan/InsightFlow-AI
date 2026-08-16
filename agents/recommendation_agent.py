from agents.llm import get_mistral_client


MODEL = "mistral-small-latest"


def generate_recommendations(df):

    client = get_mistral_client()

    summary = df.describe(
        include="all"
    ).to_string()

    prompt = f"""
You are a senior business strategy analyst.

Analyze this dataset:

{summary}

Generate 5 specific,
data-driven business recommendations.

For every recommendation provide:

1. Recommendation
2. Evidence from the dataset
3. Expected business impact

Avoid generic advice.

Do not invent information.
"""

    response = client.chat.complete(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content