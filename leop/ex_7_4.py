#Дополнения для пиццы: 

#напишите цикл, который предлагает пользователю 
#вводить дополнения для пиццы до тех пор, 
#пока не будет введено значение 'quit’ . 
#При вводе каждого дополнения выведите сообщение о том, 
#что это дополнение включено в заказ.

prompt = "\nTell me please, what would you like to add to your pizza."
prompt += "\nEnter 'quit' if it's enough. "
order_is_ready = "\nThank you for your order!"
requested_topping = ""
while requested_topping != "quit":
    requested_topping = input(prompt)
    message = "We added " + requested_topping + " to your pizza!"
    if requested_topping != 'quit':
        print(message)
    else:
        print(order_is_ready)
        break
    
print("\nWait for your pizza!")