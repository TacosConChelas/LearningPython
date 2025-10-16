def main():
    price = 50
    while price > 0 :
        print(f"Amount Due: {price}")
        coin = int(input("Insert Coin: "))
        match(coin):
            case 5:
                price -= coin
            case 10:
                price -= coin
            case 25:
                price -= coin
    if price <= 0:
        print(f"Change Owed: {- price}")
        
main()