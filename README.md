~ Apify Integration: You use ApifyClient with your API token to authenticate and access Apify's services.

~ Running an Apify Actor: You call an Apify actor (hMvNSpz3JnHgl5jkh) designed for Indeed scraping, setting parameters such as job position ("Data Analyst"), country ("IN" for India), and other configurations like maximum items to retrieve (50) and whether to parse company details.

~ Fetching the Scraped Data: The script retrieves the scraped job listings from the actor's dataset, which is automatically stored in Apify's cloud storage.

~ Data Handling: The scraped results are written to a local CSV file, including fields like job title, company name, location, salary, job description, and date posted.

The integration aims to facilitate automated and scalable job scraping while managing IPs to avoid anti-scraping measures by using Apify's proxy and actor infrastructure.
