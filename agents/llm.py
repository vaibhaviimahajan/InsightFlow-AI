import os
from mistralai import Mistral


def get_mistral_client():

    api_key = os.getenv("MISTRAL_API_KEY")

    if not api_key:
        raise ValueError(
            "MISTRAL_API_KEY is not configured."
        )

    return Mistral(api_key=api_key)