#1 Restaurant Menu print
number_of_items=4
items_name=['','','','','','','']
items_price=['','','','','','','']
for i in range(0,number_of_items):
    items_name[i]=input(f'enter item {i+1} name: ')
    items_price[i]=input(f'enter item {i+1} price: ')


max_len=0
for i in range(number_of_items):
    if(len(items_name[i])>=max_len):
        max_len=len(items_name[i])

menu=['','','','','','','']
for i in range(number_of_items):
    menu[i]=items_name[i].ljust(max_len+10)+items_price[i]
    print(menu[i])