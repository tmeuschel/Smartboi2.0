from random import randint


class Store:
  def __init__(self, items, cash):
    self.items = items
    self.cash = cash

def main():
    s1 = Store(5, 80)
    s2 = Store(70, 80)
    s3 = Store(80, 500)
    s4 = Store(7000, 7000)
    s5 = Store(5000, 200)

    User = Store(0, 500)

    while(1):
        tmp = randint(1, 6)
        store = Store(0, 0)
        if (tmp == 1):
            store.items = s1.items
            store.cash = s1.cash 
        elif (tmp == 2):
            store.items = s2.items
            store.cash = s2.cash 
        elif (tmp == 3):
            store.items = s3.items
            store.cash = s3.cash 
        elif (tmp == 4):
            store.items = s4.items
            store.cash = s4.cash 
        elif (tmp == 5):
            store.items = s5.items
            store.cash = s5.cash 

        print(f"Your cash amount {User.cash}")
        storeitem = randint(1, store.items)
        print(f"The seller is willing to barder {storeitem}")
        inp = str(input("Enter cash amount for trade: "))
        thebarderamount = randint(0, store.cash)

        try:
            inp = int(inp)

            if (inp >= thebarderamount):
                print("Good Trade")
                User.items += storeitem
                print(f"You have {User.items} items")
                inp = -1 * inp
                User.cash += inp
            else:
                print("Bad Deal")

            if (tmp == 1):
                s1.items -= storeitem
                s1.cash -= inp
            elif (tmp == 2):
                s2.items -= storeitem
                s2.cash -= inp
            elif (tmp == 3):
                s3.items -= storeitem
                s3.cash -= inp
            elif (tmp == 4):
                s4.items -= storeitem
                s4.cash -= inp
            elif (tmp == 5):
                s5.items -= storeitem
                s5.cash -= inp

        except:
            print("Why")

main()