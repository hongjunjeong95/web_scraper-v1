import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"
}


def get_post(post):
    url = post.find("a", {"class", "SQnoC3ObvgnGjWt90zD9Z"})
    if url:
        article = post.find("h3").text
        votes = post.find("div", {"class", "_1rZYMD_4xY3gRcSS3p8ODO"}).text
        url = url.attrs["href"]
        return {
            "article": article,
            "votes": votes,
            "url": f"https://www.reddit.com/{url}",
        }


def get_subreddit(aggregated_subreddit):
    subreddit = dict(language="", posts=[])
    subreddit["language"] = aggregated_subreddit

    url = f"https://www.reddit.com/r/{aggregated_subreddit}/top/?t=month"
    result = requests.get(url, headers=headers)
    soup = BeautifulSoup(result.text, "html.parser")

    posts_container = soup.find("div", {"class", "rpBJOHq2PR60pnwJlUyP0"})
    posts_list = posts_container.find_all("div", {"class": None}, recursive=False)

    for aPost in posts_list:
        extracted_post = get_post(aPost)
        if extracted_post:
            subreddit["posts"].append(extracted_post)
    return subreddit


def get_subreddits(aggregated_subreddits_dict):
    subreddits = []
    for aggregated_subreddit in aggregated_subreddits_dict:
        subreddit = get_subreddit(aggregated_subreddit)
        subreddits.append(subreddit)
    return subreddits
