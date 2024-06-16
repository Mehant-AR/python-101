d={}
d = {}
while True:
    try:
        book = input().split(',')
        if len(book) < 2:
            continue
        book_name = book[0].strip()
        category = book[1].strip()
        if category in d:
            d[category].append(book_name)
        else:
            d[category] = [book_name]
    except EOFError:
        break

for k, v in d.items():
    print(f"{k}: ", end='')
    print(', '.join(v))
