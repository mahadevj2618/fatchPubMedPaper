import csv
from typing import List, Dict

def save_to_csv(filename: str, data: List[Dict[str, str]]) -> None:
    """
    Saves research paper details to a CSV file.

    Args:
        filename (str): The name of the CSV file to save.
        data (List[Dict[str, str]]): A list of dictionaries containing paper details.

    Returns:
        None
    """
    if not data:
        print("No data to save.")
        return

    fieldnames = data[0].keys()

    try:
        with open(filename, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        print(f"Results successfully saved to {filename}")
    except Exception as e:
        print(f"Error saving to CSV: {e}")

if __name__ == "__main__":
    sample_data = [
        {
            "PubmedID": "12345678",
            "Title": "A New Study on Biotechnology",
            "Publication Date": "2024-03-10",
            "Non-academic Authors": "Dr. John Doe",
            "Company Affiliations": "XYZ Biotech Inc.",
            "Corresponding Author Email": "johndoe@xyzbiotech.com"
        }
    ]
    save_to_csv("sample_results.csv", sample_data)
