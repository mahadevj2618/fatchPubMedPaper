import requests
from typing import List

PUBMED_SEARCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"


def fetch_pubmed_ids(query: str, max_results: int = 10) -> List[str]:
    """
    Fetch PubMed IDs based on a search query.

    Args:
        query (str): The PubMed search query.
        max_results (int): The maximum number of results to fetch.

    Returns:
        List[str]: List of PubMed IDs.
    """
    params = {
        "db": "pubmed",
        "term": query,
        "retmax": max_results,
        "retmode": "json"
    }

    response = requests.get(PUBMED_SEARCH_URL, params=params)
    response.raise_for_status()

    data = response.json()
    return data.get("esearchresult", {}).get("idlist", [])


if __name__ == "__main__":
    print(fetch_pubmed_ids("biotechnology"))
