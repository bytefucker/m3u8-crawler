import re


regex = r"(http|https):\/\/[\S]*\.m3u8"
test_str = """
http://43rfvdnfkdjkfgd43434.m3u8fsjgokfg;lf
gfhbhtgdhb
http://43rfvdnfkdjkfgd43434.m3u8
frgfrghttp://43rfvdnfkdjkfgd43434.m3u8
"""


def extract_m3u8(txt: str):
    url = []
    matches = re.finditer(regex, test_str, re.MULTILINE)
    for matchNum, match in enumerate(matches, start=1):
        print("Match {matchNum} was found at {start}-{end}: {match}"
              .format(matchNum=matchNum, start=match.start(), end=match.end(), match=match.group()))
        url.append(match.group())
    return url


if __name__ == "__main__":
    urls = extract_m3u8(test_str)
    print(urls)
