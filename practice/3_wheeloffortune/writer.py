from pathlib import Path

package_path = Path(__file__).parent.resolve()


def get_words(filename: str | Path = package_path / "words.txt") -> list[str]:
    words: list[str] = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            [words.append(word.strip()) for word in line.split(",")]
    return words


def get_record(filename: str | Path = package_path / "record.txt") -> int:
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return int(f.readline())
    except (FileNotFoundError, ValueError):
        return 0


def write_record(
    record: int, filename: str | Path = package_path / "record.txt"
) -> None:
    with open(filename, "w", encoding="utf-8") as f:
        f.write(str(record))


def check_and_write_record(
    record: int, filename: str | Path = package_path / "record.txt"
) -> int:
    current_record = get_record(filename)
    if record > current_record:
        write_record(record, filename)
        return record
    return current_record
