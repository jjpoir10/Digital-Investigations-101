import requests
from bs4 import BeautifulSoup

# .jobs .cats

base_url = "https://newyork.craigslist.org/"
response = requests.get(base_url)

html = response.text
soup = BeautifulSoup(html, "html.parser")

jobs = soup.select(".jobs .cats a")

lines = ["category, url\n"]
for job_url in jobs:
    job_cat = job_url.text
    job_url = job_url.get("href")
    new_line = job_cat + "," + job_url + "\n"
    lines.append(new_line)

with open("cl_jobs.csv", "w") as outfile:
    outfile.writelines(lines)
