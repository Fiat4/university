import re
import urllib.request

URL = "https://msk.spravker.ru/avtoservisy-avtotehcentry/?page={}"
MAX = 6

card_re = re.compile(r'org-widget([\w\W]*?)widgets-list__item')
title_re = re.compile(r'header__title-link">(.+)<\/a>')
meta_re = re.compile(r'header__meta">\n(.+)<\/span>')
adress_re = re.compile(r'meta--location">\s+(.+)\s+<\/span>')
work_time_re = re.compile(r'[А-я-,]+ \d{1,2}:\d{1,2}.\d{1,2}:\d{1,2}')
phone_re = re.compile(r'(\+7 .\d{3}. \d{3}.\d{2}.\d{2})')

def parse_page(page: int):
    raw = urllib.request.urlopen(URL.format(page)).read().decode()
    cards = re.finditer(card_re, raw)
    for card in cards:
        title = re.findall(title_re, card.group(0))
        meta = re.findall(meta_re, card.group(0))
        adress = re.findall(adress_re, card.group(0))
        work_time = re.findall(work_time_re, card.group(0))
        phone = re.findall(phone_re, card.group(0))
        
        print(
            (
                title[0] if title else "Неизвестный сервис",
                meta[0].strip() if meta else "Сервис",
                adress[0] if adress else "Адрес неизвестен",
                work_time[0] if work_time else "Часы работы неизвестны",
                ", ".join(phone) if phone else "Номер неизвестен",            
            )
        )
        
        
    

if __name__ == "__main__":
    for page in range(1, MAX):
        parse_page(page)