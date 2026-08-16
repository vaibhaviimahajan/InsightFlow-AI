from agents.llm import get_llm


def generate_ai_insights(df):

    llm = get_llm()

    summary = df.describe(
        include="all"
    ).to_string()

    prompt = f"""
You are a senior business analyst.

Analyze this dataset:

{summary}

Provide:

1. Five important business insights
2. Three potential business risks
3. Three opportunities
4. A short executive summary

Focus on actionable business meaning.

Avoid generic statements.
"""

    response = llm.invoke(prompt)

    return response.content


def generate_executive_summary(df):

    llm = get_llm()

    summary = df.describe(
        include="all"
    ).to_string()

    prompt = f"""
Create a professional one-paragraph
executive summary for a business report.

Dataset:

{summary}

The summary should explain:

- overall performance
- important trends
- strongest areas
- weakest areas
- business opportunities

Use concise business language.
"""

    response = llm.invoke(prompt)

    return response.content