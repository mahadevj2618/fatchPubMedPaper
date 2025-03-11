import argparse
from fetch_pubmed_ids import fetch_pubmed_ids
from fetch_paper_detail import fetch_paper_detail
from extract_company_authors import extract_company_authors
from save_to_csv import save_to_csv

def main():
    parser = argparse.ArgumentParser(description="Fetch PubMed research papers with company-affiliated authors.")
    parser.add_argument("query", type=str, help="Search query for PubMed")
    parser.add_argument("-f", "--file", type=str, help="Output CSV file")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode")

    args = parser.parse_args()

    pubmed_ids = fetch_pubmed_ids(args.query, max_results=10)

    if args.debug:
        print(f"PubMed IDs: {pubmed_ids}")

    results = []

    for pubmed_id in pubmed_ids:
        details = fetch_paper_detail(pubmed_id)
        author_data = extract_company_authors(details.get("Authors", []))

        result = {
            "PubmedID": details["PubmedID"],
            "Title": details["Title"],
            "Publication Date": details["Publication Date"],
            "Non-academic Authors": ", ".join(author_data["Non-academic Authors"]),
            "Company Affiliations": ", ".join(author_data["Company Affiliations"]),
        }
        results.append(result)

    if args.file:
        save_to_csv(args.file, results)
    else:
        for result in results:
            print(result)

if __name__ == "__main__":
    main()
