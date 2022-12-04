import re
import urllib.request

URL = "https://msk.spravker.ru/avtoservisy-avtotehcentry/?page={}"
MAX = 6

card_re = re.compile(r"org-widget__in[\w\W]*?widgets-list__item")
info_re = re.compile(
    r'__in">[\W\w]*?title-link">([\W\w]*?)<[\W\w]*?location">\s*([А-я,\-  .0-9]*)[\W\w]*?(?:spec__value">([0-9 + (),-]*)<\/dd>[\W\w]*?)?spec__value">([\W\w]*?)<'
)


def parse_page(page: int):
    raw = urllib.request.urlopen(URL.format(page)).read().decode()
    cards = card_re.finditer(raw)
    for card in cards:
        info = info_re.search(card.group(0))
        if info:
            print(info.groups())


if __name__ == "__main__":
    for page in range(1, MAX):
        parse_page(page)
