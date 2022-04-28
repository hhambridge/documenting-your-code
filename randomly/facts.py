import requests
from requests.exceptions import RequestException
from typing import Union


def generate_random_fact(output_format: str, language: str) -> Union[str, dict]:
    """
    Generates a random fact based on the user specified inputs

    Parameters
    ----------
    output_format : str
        format to return; "html", "json", "txt", or "md"
    language : str
        language to return; "en" or "de"

    Returns
    -------
    fact : dict if output_format = "json", str otherwise
        a random fact pulled from uselessfacts.jsph.pl

    """
    # Verify inputs are valid
    if language not in {"en", "de"}:
        raise ValueError(f"{language} is not supported.")

    if output_format not in {"html", "json", "txt", "md"}:
        raise ValueError(f"{output_format} is not supported.")

    # Query to get fact
    response = requests.get(
        f"https://uselessfacts.jsph.pl/random.{output_format}?language={language}"
    )

    # Status code 200 indicates successful request
    if response.status_code == 200:
        if output_format == "json":
            fact = response.json()
        else:
            fact = response.text
    else:
        raise RequestException(
            f"Something went wrong. Request returned status {response.status_code}."
        )

    return fact
