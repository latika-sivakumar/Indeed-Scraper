from apify_client import ApifyClient
import csv

client = ApifyClient("apify_api_c9dp39YHxSXvemMNlm7XbEiM1ews8w27av7s")

run_input = {
    "position": "Data Analyst",
    "country": "IN",
    "maxItems": 50,
    "parseCompanyDetails": True,
    "saveOnlyUniqueItems": True,
    "followApplyRedirects": False,
}

run = client.actor("hMvNSpz3JnHgl5jkh").call(run_input=run_input)

items = list(client.dataset(run["defaultDatasetId"]).iterate_items())

csv_file_name = r"C:\Users\latik\OneDrive\Documents\Project\indeed_jobs.csv"

with open(csv_file_name, mode='w', newline='', encoding='utf-8') as csv_file:
    fieldnames = ["job_title", "company_name", "location", "salary", "job_description", "date_posted"]
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

    for item in items:
        row = {
            "job_title": item.get("positionName") or "",
            "company_name": item.get("company") or "",
            "location": item.get("location") or "",
            "salary": item.get("salary") or "",
            "job_description": item.get("description") or "",
            "date_posted": item.get("postedAt") or ""
        } 
        csv_writer.writerow(row)
print(f"Data successfully written to {csv_file_name}")