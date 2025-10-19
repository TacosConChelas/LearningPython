def main():
    items : list[str] = []
    while True:
        try:
            items.append(str(input("").strip().upper()))
        except EOFError:
            counts: dict[str, int] = {}
            for item in items:
                counts[item] = counts.get(item, 0) + 1
            
            sorted_items = sorted(
                counts.items(),
                key=lambda kv: (-kv[1], kv[0])
            )
            for qty, name in [(v, k) for k, v in sorted_items]:
                print(f"{qty} {name}")

            break
main()