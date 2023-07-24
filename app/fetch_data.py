import requests
from constants import CONFIG
from tenacity import retry, wait_exponential, retry_if_exception_type


@retry(
    wait=wait_exponential(multiplier=1, min=1, max=6),
    retry=retry_if_exception_type(
        (requests.ConnectionError, requests.ConnectTimeout, requests.HTTPError)
    ),
    reraise=True,
)
def fetchdata() -> dict:
    return requests.get(url=CONFIG.get("DATA_SOURCE_URL"))
