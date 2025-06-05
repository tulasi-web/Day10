import datetime
user_name=input("enter the User name :")
Quantity=int(input("How many Phones you wanted to buy : "))
cost=80000
amount=cost*Quantity
cgst=2.5/100
sgst=2.5/100
amount_cgst=amount*cgst
amount_sgst=amount*sgst
total_amount=amount+amount_cgst+amount_sgst


if Quantity==2:
    dis=(10/100)*total_amount
elif Quantity>=3 and Quantity<=5:
    dis=(15/100)*total_amount
elif Quantity>=6 and Quantity<=10:
    dis=(17/100)*total_amount
elif Quantity>=11 and Quantity<=15:
    dis=(23/100)*total_amount
elif Quantity>=15:
    dis=(25/100)*total_amount

print("\n\n")
print("\t  Tulasi pvt ltd")
print("  CF203, sector1, saltlake, Bangalore-700064")
print("\t    ph : 033-69000005")
print("\t GST IN:19AADCG7132K1ZE")
print("\t      BILL")
print("------------------------------------------------------")
print("   Memo# 17/41840\t ",datetime.datetime.now())
print("   User : {}\t\t\tPax# 1".format(user_name))
print("\t\t  Order# 1")
print("------------------------------------------------------")
print("Product\t\t\tQty\t Rate\tAmount")
print("------------------------------------------------------")
print(" Tea\t\t\t{}\t {}\t{}".format(Quantity,cost,amount))
print("------------------------------------------------------")
print("Sub Total \t\t\t\t{}".format(amount))
print("C Gst @ 2.5%\t\t\t\t",amount_cgst)
print("S Gst @ 2.5%\t\t\t\t",amount_sgst)
print("------------------------------------------------------")
print("Total\t Qty : {}\t\t\tAmt\t{} \n".format(Quantity,total_amount))
print("saved amount \t",dis)
print("After discount amount need to be pay",total_amount-dis)
print("Thank You , Please Visit again")# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.