from agents.llm import get_mistral_client


MODEL = "mistral-small-latest"


def ask_dataset_question(df, question):

    client = get_mistral_client()

    dataset_info = df.describe(
        include="all"
    ).to_string()

    columns = ", ".join(
        df.columns.astype(str)
    )

    prompt = f"""
You are a data analyst assistant.

The user uploaded a dataset.

Columns:
{columns}

Dataset summary:
{dataset_info}

User question:
{question}

Answer the user's question using
only information supported by the dataset.

If the information cannot be determined
from the dataset, clearly say so.

Explain the answer in simple
business language.
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