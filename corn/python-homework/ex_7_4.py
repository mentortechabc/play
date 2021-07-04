
def added_topping():
    while True:
        topping = input("Input topping for pizza ")
        if topping == "quit":
            break

        else:
            print("You", topping, "added for order")


added_topping()
