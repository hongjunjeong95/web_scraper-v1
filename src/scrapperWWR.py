import requests
from bs4 import BeautifulSoup


def extract_job(html):
    title = html.find("span", {"class": "title"}).string
    company = html.find("span", {"class": "company"}).string
    location = html.find("span", {"class": "region"})
    if location:
        location = location.string
    link = html.find("a")["href"]
    return {
        "title": title,
        "company": company,
        "location": location,
        "link": f"https://weworkremotely.com/remote-jobs{link}",
    }


def extract_jobs(url):
    jobs = []
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    results = (
        soup.find("section", {"class": "jobs"})
        .find("ul")
        .find_all("li", {"class": "feature"})
    )

    for result in results:
        job = extract_job(result)
        jobs.append(job)
    return jobs


def get_WWRJobs(word):
    url = f"https://weworkremotely.com/remote-jobs/search?term={word}"
    jobs = extract_jobs(url)
    return jobs
