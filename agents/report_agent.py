from agents.llm import get_mistral_client


MODEL = "mistral-small-latest"


def generate_business_report(df):

    client = get_mistral_client()

    summary = df.describe(
        include="all"
    ).to_string()

    prompt = f"""
You are a senior business analyst.

Create a professional business report
based on this dataset.

DATASET SUMMARY:

{summary}

Report structure:

# Executive Summary

Write a concise overview.

# Key Findings

List the 5 most important findings.

# Business Risks

List important potential risks.

# Opportunities

List potential business opportunities.

# Recommendations

Provide 5 specific recommendations.

Rules:

- Do not invent facts.
- Base conclusions on the dataset.
- Use professional business language.
- Make recommendations actionable.
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