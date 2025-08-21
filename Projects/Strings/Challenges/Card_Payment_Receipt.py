#take credit card number as input, payment amount and then display a message of the transaction
Card_No=input('enter credit card number: ') #0123 4 5678 9 10111213 14
pay_amount=input('enter your payment amount: ')
Displayed_no=''
counter=0
for i in Card_No:
    if(counter>=15):
        Displayed_no+=Card_No[counter]
    counter += 1
s='XXXX XXXX XXXX '
Displayed_no=s+Displayed_no
print(f"\t\t Transaction Alert\n Amount {pay_amount}$ has been debited from your card {Displayed_no}")


#easier way
# a good programmer makes the task with algorithm that takes less time, less processing
Displayed_no=Card_No[15:]
S=('X'*4)+' '
Displayed_no=(S*3)+Displayed_no
print(f"\t\t Transaction Alert\n Amount {pay_amount}$ has been debited from your card {Displayed_no}")