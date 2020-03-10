import requests
import os
import spacy

from fastapi import APIRouter

from core.constants import SOURCE_URL
from core.config import MODEL

nlp = spacy.load(os.environ.get('MODEL', MODEL))

router = APIRouter()


@router.get("/")
def get_redacted_message_from_source():
    source_url = os.environ.get('SOURCE_URL', SOURCE_URL)
    res = requests.get(source_url)
    data = res.json()
    handled_data = handle_data(data)
    return {"redacted": True, "data": handled_data}


@router.post("/")
def get_redacted_message_from_body(data: dict):
    handled_data = handle_data(data)
    return {"redacted": True, "data": handled_data}


def handle_data(data):
    result = {}

    if not isinstance(data, list) and not isinstance(data, dict) and not isinstance(data, str):
        return data

    if isinstance(data, str):
        return replace_name(data)

    if isinstance(data, list):
        tmp = []
        for value in data:
            tmp.append(handle_data(value))
        return tmp

    if isinstance(data, dict):
        for k, v in data.items():
            if isinstance(v, dict):
                result[k] = handle_data(v)
            elif isinstance(v, list):
                tmp = []
                for value in v:
                    tmp.append(handle_data(value))
                result[k] = tmp
            elif isinstance(v, str):
                result[k] = replace_name(v)
            else:
                result[k] = v
    return result


def replace_name(value: str) -> str:
    doc = nlp(value)
    names = [ent.text for ent in doc.ents if ent.label_ == "PERSON"]
    for name in names:
        short_name = ".".join([text[0] for text in name.split()])
        value = value.replace(name, short_name)
    return value
