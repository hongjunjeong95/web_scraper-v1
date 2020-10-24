# https://remoteok.io/remote-dev+python-jobs
import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"
}


def extract_job(html):
    tds = html.find_all("td")
    link = tds[0].find("a")["href"]
    if not link:
        link = ""

    title = tds[1].find("h2").string
    if not title:
        title = ""

    company = tds[1].find("a").find("h3").string
    if not company:
        company = ""

    location = tds[1].find("div", {"class": "location"})
    if not location:
        location = ""
    else:
        location = location.string

    return {
        "title": title,
        "company": company,
        "location": location,
        "link": f"https://remoteok.io/{link}",
    }


def extract_jobs(url):
    jobs = []
    result = requests.get(url, headers=headers)
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find("table", {"id": "jobsboard"}).find_all("tr", {"class": "job"})

    for result in results:
        job = extract_job(result)
        jobs.append(job)
    return jobs


def get_RemoteJobs(word):
    url = f"https://remoteok.io/remote-dev+{word}-jobs"
    jobs = extract_jobs(url)
    return jobs


# https://remoteok.io/remote-dev+python-jobs