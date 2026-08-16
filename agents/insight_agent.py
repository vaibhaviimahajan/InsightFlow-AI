from agents.llm import get_mistral_client


MODEL = "mistral-small-latest"


def generate_ai_insights(df):

    client = get_mistral_client()

    summary = df.describe(
        include="all"
    ).to_string()

    prompt = f"""
You are a senior data analyst.

Analyze this dataset summary:

{summary}

Generate 5 important business insights.

Focus on:
- unusual patterns
- strong performance
- weak performance
- possible business problems
- opportunities

Do not simply repeat statistics.

Explain what the numbers mean
from a business perspective.

Return a numbered list.

Do not invent facts that are not
supported by the dataset.
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