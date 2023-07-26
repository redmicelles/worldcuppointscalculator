import requests
from constants import CONFIG
from tenacity import retry, wait_exponential, retry_if_exception_type
from constants import REQUEST_TIMEOUT
from model.request_models import FixturesModel, FixturesModelItem
from typing import List
from pydantic import parse_obj_as, TypeAdapter
import json


@retry(
    wait=wait_exponential(multiplier=1, min=1, max=6),
    retry=retry_if_exception_type(
        (requests.ConnectionError, requests.ConnectTimeout, requests.HTTPError)
    ),
    reraise=True,
)
def fetchdata() -> dict:
    try:
        return requests.get(url=CONFIG.get("DATA_SOURCE_URL"), timeout=REQUEST_TIMEOUT).json()
    except Exception as e:
        return e
    
# x = [i for i in FixturesModel.validate_python(fetchdata()) if i]
# with open("./fixtures.json", "w", encoding="utf-8") as fp:
#     json.dump(x, fp, indent=4)


