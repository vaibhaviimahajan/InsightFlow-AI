from agents.llm import get_llm


def generate_ai_insights(df):

    llm = get_llm()

    summary = df.describe(
        include="all"
    ).to_string()

    prompt = f"""
You are a senior data analyst.

Analyze the following dataset summary.

DATASET SUMMARY:
{summary}

Generate 5 useful business insights.

Focus on:
- important patterns
- unusually high or low values
- business opportunities
- potential problems
- relationships between variables

Do not simply repeat statistics.

Explain what the numbers mean from a
business perspective.

Return the insights as a numbered list.
"""

    response = llm.invoke(prompt)

    return response.content