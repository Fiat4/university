PERMISSIONS = {"read": "R", "write": "W", "execute": "X"}

files: dict[str, str] = dict(
    [input().split(maxsplit=1) for _ in range(int(input("Кол-во файлов: ")))]
)

for _ in range(int(input("Кол-во операций: "))):

    operation, filename = input().split()

    if PERMISSIONS[operation] in files.get(filename, ""):
        print("OK")
    else:
        print("Denied")
