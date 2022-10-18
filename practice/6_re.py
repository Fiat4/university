import re

SEARCH = re.compile(
    r"^Рейс (\d+) (?:прибыл|отправился) (из|в) (\S+) в (\d{2}:\d{2}:\d{2}$)"
)

with open("data/journal.txt", "r", encoding="utf-8") as s:
    with open("data/cleanjournal.txt", "w", encoding="utf-8") as d:
        for line in s:
            results = re.search(SEARCH, line)
            if results:
                d.write(
                    f"[{results.groups()[3]}] Поезд № {results.groups()[0]} {results.groups()[1]} {results.groups()[2]}\n"
                )
