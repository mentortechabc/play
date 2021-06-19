# Дополнения для пиццы:

# напишите цикл, который предлагает пользователю
# вводить дополнения для пиццы до тех пор,
# пока не будет введено значение 'quit’ .
# При вводе каждого дополнения выведите сообщение о том,
# что это дополнение включено в заказ.

prompt = "\nTell me please, what would you like to add to your pizza."
prompt += "\nEnter 'quit' if it's enough. "
order_is_ready = "\nThank you for your order!"


def order_pizza(requested_topping):
    """The function asks a customer about the toppings for pizza and makes the order"""
    requested_topping = ""
    active = True
    while active == True:
        requested_topping = input(prompt)
        if requested_topping != "quit":
            message = "We added " + requested_topping + " to your pizza!"
            print(message)
        else:
            active = False
            print(order_is_ready)
            break


order_pizza("")
print("\nWait for your pizza!")
