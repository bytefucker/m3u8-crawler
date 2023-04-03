import re
import requests
import os
import json


title_regex = r"<title>([\S\s]*)</title>"
m3u8_regex = r"(http|https):\/\/[\S]*\.m3u8"


def extract_m3u8(txt: str):
    title = ''
    urls = []
    title_match = re.finditer(title_regex, txt, re.MULTILINE)
    for _, match in enumerate(title_match, start=0):
        title = match.group().replace('<title>', '').replace('</title>', "")

    m3u8_matches = re.finditer(m3u8_regex, txt, re.MULTILINE)
    for _, match in enumerate(m3u8_matches, start=1):
        urls.append(match.group())
    return title, urls


def web_page(url: str):
    resp = requests.get(url=url)
    if resp.status_code != 200:
        pass
    title, urls = extract_m3u8(resp.text)
    dir = f'data/{title}'
    if os.path.exists(dir) is False:
        os.mkdir(dir)
    with open(f'{dir}/meta.json', 'w', encoding='utf-8') as f:
        data = json.dumps({"title": title, "urls": urls}, ensure_ascii=False)
        f.writelines(data)
    return title


def download(url):
    pass


if __name__ == "__main__":
    for i in range(0, 2000):
        url = f"https://demo.com/videos/play/{25399-i}"
        title = web_page(url)
        print(f'{i}:{title}')
