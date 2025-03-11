from typing import List, Dict

COMPANY_KEYWORDS = ["pharma", "biotech", "laboratories", "inc.", "corp", "gmbh", "ltd"]


def extract_company_authors(authors: List[Dict[str, str]]) -> Dict[str, List[str]]:
    """
    Identifies authors affiliated with pharmaceutical/biotech companies.

    Args:
        authors (List[Dict[str, str]]): List of authors with their affiliations.

    Returns:
        Dict[str, List[str]]: Dictionary with author names and company affiliations.
    """
    non_academic_authors = []
    company_affiliations = []

    for author in authors:
        name = author.get("name", "Unknown")
        affiliation = author.get("affiliation", "")

        if any(keyword in affiliation.lower() for keyword in COMPANY_KEYWORDS):
            non_academic_authors.append(name)
            company_affiliations.append(affiliation)

    return {
        "Non-academic Authors": non_academic_authors,
        "Company Affiliations": company_affiliations
    }


if __name__ == "__main__":
    sample_authors = [
        {"name": "Dr. John Smith", "affiliation": "XYZ Biotech Inc."},
        {"name": "Dr. Alice Johnson", "affiliation": "Harvard University"},
    ]
    print(extract_company_authors(sample_authors))
