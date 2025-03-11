import requests
from typing import Dict, Any

PUBMED_SUMMARY_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"

def fetch_paper_detail(pubmed_id: str) -> Dict[str, Any]:
    """
    Fetch details of a PubMed research paper.

    Args:
        pubmed_id (str): Unique PubMed identifier.

    Returns:
        Dict[str, Any]: Dictionary containing paper details.
    """
    params = {
        "db": "pubmed",
        "id": pubmed_id,
        "retmode": "json"
    }

    response = requests.get(PUBMED_SUMMARY_URL, params=params)
    response.raise_for_status()

    data = response.json()
    result = data.get("result", {}).get(pubmed_id, {})

    return {
        "PubmedID": pubmed_id,
        "Title": result.get("title", "N/A"),
        "Publication Date": result.get("pubdate", "N/A"),
        "Authors": result.get("authors", [])
    }

if __name__ == "__main__":
    print(fetch_paper_detail("12345678"))
