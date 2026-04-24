# ATM log-in 
print("ATM")
print("plz insert your card")
pin=int(input("enter pin!!"))
balance=10000
num=8793
if pin==num:
    while True:
        print("1=withdraw money")
        print("2=deposit money")
        print("3=check balance")
        print("4=reset pin")
        print("5=exit")
        try:
            option=int(input("plz choose option: "))
        except:
            print("plz enter valid input!!")
        finally:
            p=int(input("enter pin!!"))
        if p==pin:
            if option==1:
                withdraw =int(input("enter amount:"))
                if withdraw < balance:
                    balance = balance - withdraw 
                    print("------------------------------------------")
                    print(f'{withdraw } is debited from your account')
                    print("------------------------------------------")
                else:
                    print("------------------------------------------")
                    print("account m konya intne paise!!")
                    print("------------------------------------------")
            elif option==2:
                deposit = int(input("enter amount"))
                balance = balance + deposit 
                print("------------------------------------------")
                print(f'{deposit} is credited to your account')
                print("------------------------------------------")
            elif option==3:
                print("------------------------------------------")
                print(f'your balance {balance}')
                print("------------------------------------------")
            elif option==4:
                old_pin=int(input("enter old pin"))
                if old_pin==pin:
                    new_pin=int(input("enter new pin"))
                    confirm_pin=int(input("enter pin again"))
                    if new_pin==confirm_pin:
                        num=new_pin
                        pin=new_pin
                    else:
                        print("------------------------------------------")
                        print("pin doesn't match")
                        print("------------------------------------------")
                else:
                    print("------------------------------------------")
                    print("plz enter valid pin")
                    print("------------------------------------------")
            elif option==5:
                print("Thank you")
                break 
        else:
            print("------------------------------------------")
            print("plz enter valid pin")
            print("------------------------------------------")
else:
    print("plz enter valid pin")