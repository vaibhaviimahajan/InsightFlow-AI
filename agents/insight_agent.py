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

def generate_executive_summary(df):

    client = get_mistral_client()

    summary = df.describe(
        include="all"
    ).to_string()

    prompt = f"""
You are preparing an executive report
for a business manager.

Dataset summary:

{summary}

Write a concise executive summary.

Cover:

- overall performance
- strongest areas
- weakest areas
- important trends
- business opportunities

Use professional business language.

Do not invent facts.
Only use information supported
by the dataset.
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