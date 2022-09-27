import random
from re import I
i=1
print("*** WELCOME TO BANK OF INDIA ***")
print("What Can I help You With ")
while True:
    wt_todo=input("(1)Open a new account\n(2)Use existing account\n")
    if wt_todo=="1":
        new_acc=open("/home/suvansh/Documents/py projects/X--BANK--X/bank_data","a")
        acc_num=i
        usr_name=input("Enter Name - ")
        usr_num=input("Enter Mobile Number - ")
        usr_ID=input("Enter Unique ID - ")
        usr_bal=input("Enter Amount to deposit - ")
        new_acc.write("\n Account number - "+str(i) )
        new_acc.write("     User Name - "+usr_name)
        new_acc.write("     User Mobile Number - "+usr_num)
        new_acc.write("     User Unique ID - "+usr_ID)
        new_acc.write("     User Balance - "+usr_bal)
        print("\n\n\n*** SUCCESS ***")
        print("User Account Number is - ",i)
        print("User Name is - ",usr_name)
        print("User Mobile Number is - ",usr_num)
        print("User Unique ID is - ",usr_ID)
        print("")
        print("________________________")
        print("Balance = ",usr_bal)
        print("________________________")
        input()
        new_acc.close()
        i=i+1
    if wt_todo=="2":
        acc_det=open("/home/suvansh/Documents/py projects/X--BANK--X/bank_data","r")
        acc_num=input("Enter Account Number - ")
        lines=acc_det.readlines()
        print("\n\n",lines[int(acc_num)])
        
