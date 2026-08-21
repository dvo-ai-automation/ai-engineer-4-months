def main():
    amount_due = 50
    print("Amount Due:", amount_due)

    while amount_due > 0:
        coin = int(input("Insert coin: "))
        if coin in [25, 10, 5]:
            amount_due = amount_due - coin
        if amount_due > 0:
            print("Amount Due:", amount_due)

    change = abs(amount_due)
    print("Change Owed:", change)

main()
