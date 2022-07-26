import re
import urllib.request
import json
import pykakasi


def convert_to_hepburn(name: str):
    hiragana = re.compile('[\u3041-\u309F]+')
    match = hiragana.fullmatch(name)
    if match:
        print(match)
        item = pykakasi.kakasi().convert(match.group())[0]
        return item["hepburn"]
    else:
        return None


def get_gender(name: str):
    if not name:
        return None
    hepburn_name = convert_to_hepburn(name)
    if not hepburn_name:
        return None
    url = f"https://api.genderize.io/?name={hepburn_name}"
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as res:
        json_data = json.loads(res.read())
        return json_data
