import json
import time
from datetime import datetime

import requests
import multiprocessing

from app.constants import (
    SIGNNOW_DOCUMENT_CONNECTION_DICT,
    SIGNNOW_DOCUMENT_CONNECTION_LIST,
    DOWELLCONNECTION_URL,
)

dd = datetime.now()
time = dd.strftime("%d:%m:%Y,%H:%M:%S")
headers = {"Content-Type": "application/json"}


def get_event_id():
    url = "https://uxlivinglab.pythonanywhere.com/create_event"
    data = {
        "platformcode": "FB",
        "citycode": "101",
        "daycode": "0",
        "dbcode": "pfm",
        "ip_address": "192.168.0.41",  # get from dowell track my ip function
        "login_id": "lav",  # get from login function
        "session_id": "new",  # get from login function
        "processcode": "1",
        "location": "22446576",  # get from dowell track my ip function
        "objectcode": "1",
        "instancecode": "100051",
        "context": "afdafa ",
        "document_id": "3004",
        "rules": "some rules",
        "status": "work",
        "data_type": "learn",
        "purpose_of_usage": "add",
        "colour": "color value",
        "hashtags": "hash tag alue",
        "mentions": "mentions value",
        "emojis": "emojis",
        "bookmarks": "a book marks",
    }

    r = requests.post(url, json=data)
    if r.status_code == 201:
        return json.loads(r.text)
    else:
        return json.loads(r.text)["error"]

def save_to_signnow_document_collection(options):
    options["eventId"] = get_event_id()["event_id"]
    options["created_on"] = time
    payload = json.dumps(
        {
            **SIGNNOW_DOCUMENT_CONNECTION_DICT,
            "command": "insert",
            "field": options,
            "update_field": {"order_nos": 21},
            "platform": "bangalore",
        }
    )
    return post_to_data_service(payload)


def post_to_data_service(data):
    response = requests.post(url=DOWELLCONNECTION_URL, data=data, headers=headers)
    return json.loads(response.text)

def get_data_from_data_service(
    cluster: str,
    platform: str,
    database: str,
    collection: str,
    document: str,
    team_member_ID: str,
    function_ID: str,
    command: str,
    field: dict,
):
    """Pass In DB info + look fields + DB query to get data"""
    payload = json.dumps(
        {
            "cluster": cluster,
            "platform": platform,
            "database": database,
            "collection": collection,
            "document": document,
            "team_member_ID": team_member_ID,
            "function_ID": function_ID,
            "command": command,
            "field": field,
            "update_field": "nil",
        }
    )
    response = post_to_data_service(payload)
    res = json.loads(response)
    if res["data"] is not None:
        if len(res["data"]):
            return res["data"]
    return

