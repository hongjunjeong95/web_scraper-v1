from scrapperSO import get_SOjobs
from scrapperWWR import get_WWRJobs
from scrapperRemote import get_RemoteJobs


def get_jobs(word):
    SOJobs = get_SOjobs(word)
    WWRJobs = get_WWRJobs(word)
    RemoteJobs = get_RemoteJobs(word)
    jobs = SOJobs + WWRJobs + RemoteJobs
    return jobs
