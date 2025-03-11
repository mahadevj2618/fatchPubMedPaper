# fatchPubMedPaper
## Overview
This Python project fetches research papers from PubMed, identifies authors affiliated with pharmaceutical or biotech
companies, and saves the results in a CSV file.
## Features
- Fetches PubMed research papers using a flexible search query
- Extracts authors with company affiliations (pharma, biotech, etc.)
- Outputs results as CSV or prints to the console
- Command-line interface with debugging and file output options
## Installation
### 1. Clone the Repository
```
git clone https://github.com/yourusername/pubmed_paper_fetcher.git
cd pubmed_paper_fetcher
```
### 2. Install Dependencies
Using pip:
```
pip install -r requirements.txt
```
Using Poetry (optional):
```
poetry install
```
## Usage
### Run the script with a search query
```
python script.py "biotechnology"
```
This will print results to the console.
### Save results to a CSV file
```
python script.py "biotechnology" -f results.csv
```
The extracted paper details will be saved in results.csv.
### Enable debug mode
```
python script.py "biotechnology" -d
```
Debug mode prints additional details like fetched PubMed IDs.
## Command-line Options
| Option | Description |
|--------------|--------------------------------|
| query | (Required) Search query for PubMed papers |
| -f, --file | Specify a filename to save results as a CSV |
| -d, --debug | Enable debug mode for extra output |
| -h, --help | Show help message |
## Project Structure
```
/pubmed_paper_fetcher
 fetch_pubmed_ids.py # Fetch PubMed IDs for a given query
 fetch_paper_detail.py # Fetch detailed paper information
 extract_company_authors.py # Identify authors affiliated with companies
 save_to_csv.py # Save the results to a CSV file
 script.py # Main CLI script
 requirements.txt # Dependencies
 README.md # Documentation
```
## Example Output
Running:
```
python script.py "cancer immunotherapy"
```
May produce:
```
{
 "PubmedID": "12345678",
 "Title": "New Advances in Cancer Immunotherapy",
 "Publication Date": "2024-03-10",
 "Non-academic Authors": "Dr. John Doe",
 "Company Affiliations": "XYZ Biotech Inc."
}
