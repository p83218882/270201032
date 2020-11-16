promise_book_number = int(input("plz say books  number with dsc: "))

promise_book_price = int(input("promise book price: "))

total_cost = float(input("total cost: "))

without_dsc_book_price = (total_cost - promise_book_price)

without_dsc_book_number = (without_dsc_book_price)/19.99

print("withour discount book number is :" + str(without_dsc_book_number) )
