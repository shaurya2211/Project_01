import pickle
import datechecker

def acc1plus():
    with open('accounts.dat','rb') as f:
        l=pickle.load(f)
    a=l.pop()
    z=a[0]+1
    return z

def createaccount():
    with open('accounts.dat', 'rb') as g:
        l = pickle.load(g)
        print('Please enter the following details to create a new account:')
        print()
        name = input('Enter A/c holder name: ')
        while True:
            dob=input('Enter Date of Birth (DD-MM-YYYY): ')
            c=datechecker.datechecker(dob)
            if c is True:
                break
            else:
                print('Enter valid date')
        while True:
            phno = int(input('Enter your phone number: '))
            string=str(phno)
            if len(string)<10 or len(string)>10:
                print('Enter valid phone number')
            else:
                break
        while True:
            email = input('Enter your Email ID: ')
            if email.count('@') == 0 or email.count('@') > 1:
                print('Enter a valid Email ID')
            else:
                break
        add = input('Enter your Address: ')
        print()
        print('Thank You for creating an account with us!!')
        print()
        b=acc1plus()
        s='ASR'+str(b)
        print('Your A/c No. is',s)
        k = [b, name, dob, phno, email, add, 0.0, 0.0]
        l.append(k)
    with open('accounts.dat', 'wb') as s:
        pickle.dump(l,s)
    features()


def closeaccount():
    with open('accounts.dat', 'rb') as g:
        l = pickle.load(g)
    while True:
        acc=int(input('Enter the remaining digits of the account number you want to close(ASR...): '))
        for i in l:
            if i[0]==acc:
                print('Account details are:')
                print()
                print('Name: ',i[1],'\nD.O.B: ',i[2],'\nPh.No: ',i[3])
                print('Email: ',i[4],'\nAddress: ',i[5],'\nRemaining Loan Amt: ',i[6])
                print('Balance: ',i[7])
                while True:
                    ch = input('Do you really want to close account?(Y/N): ')
                    if ch == 'y' or ch == 'Y':
                        l.remove(i)
                        print()
                        print('Account closed successfully')
                        print()
                        with open('accounts.dat', 'wb') as s:
                            pickle.dump(l, s)
                        features()
                        break
                    elif ch=='n' or ch=='N':
                        print()
                        features()
                        break
                    else:
                        print('Enter valid option')
                        continue
        else:
            print('Enter a valid Account number')
            print()
            
def applyloan():
    with open('accounts.dat', 'rb') as g:
        li = pickle.load(g)
    print('Welcome to the Loan Portal!!')
    print('Press: \n 1. To Apply for Home Loan \n 2. To Apply for Car Loan')
    print('3. To Apply for Business Loan \n 4. To Apply for Education Loan')
    print('5. To Apply for Other Loan')
    ch=int(input('Enter your choice: '))
    l=['Home loan','Car Loan','Business Loan','Education Loan','Other Loan']
    print('Please enter the following details to apply for a',l[ch-1],':')
    while True:
        acc=int(input('Enter the remaining digits of the account number you want to take loan on(ASR...): '))
        for i in li:
            if i[0]==acc:
                sal=float(input('Enter your current salary in Rs: '))
                amo=float(input('Enter the amount of loan required in Rs: '))
                year=int(input('Enter number of years: '))
                print('You are eligible for a loan of Rs',amo,'at an interest of 12.35% for',year,'years')
                ch = input('Do you want to take loan?(Y/N): ')
                if ch == 'y' or ch == 'Y':
                    i[6]+=amo+(0.1235*amo)
                    print()
                    print('You have been granted the loan successfully')
                    print()
                    with open('accounts.dat', 'wb') as s:
                        pickle.dump(li, s)
                    features()
                    break
                elif ch=='n' or ch=='N':
                    print()
                    features()
                    break
                else:
                    print('Enter valid option')
                    continue    
        else:
            print('Enter a valid Account number')
            print()
            continue
    
def addmoney():
    with open('accounts.dat', 'rb') as g:
        li = pickle.load(g)
    while True:
        acc=int(input('Enter the remaining digits of your account number to continue(ASR...): '))
        for i in li:
            if i[0]==acc:
                amo=float(input('Enter the amount to be added in Rs: '))
                ch = input('Do you want to add amount?(Y/N): ')
                if ch == 'y' or ch == 'Y':
                    i[7]+=amo
                    print()
                    print('Your balance has been updated successfully')
                    print()
                    with open('accounts.dat', 'wb') as s:
                        pickle.dump(li, s)
                    features()
                    break
                elif ch=='n' or ch=='N':
                    print()
                    features()
                    break
                else:
                    print('Enter valid option')
                    continue    
        else:
            print('Enter a valid Account number')
            print()
            

def sendmoney():
    with open('accounts.dat', 'rb') as g:
        li = pickle.load(g)
    while True:
        accfrom=int(input('Enter the remaining digits of account number from which money is to be debited(ASR...): '))
        for i in li:
            if i[0]==accfrom:
                amo=float(input('Enter the amount to be debited in Rs: '))
                while True:
                    accto=int(input('Enter the remaining digits of account number to which money is to be credited(ASR...): '))
                    for j in li:
                        if j[0]==accto:
                            while True:
                                ch= input('Do you want to proceed with the transaction?(Y/N): ')
                                if ch == 'y' or ch == 'Y':
                                    if i[7]>amo:
                                        i[7]-=amo
                                        j[7]+=amo
                                        print()
                                        print('Transaction successful')
                                        print()
                                        with open('accounts.dat', 'wb') as s:
                                            pickle.dump(li, s)
                                        features()
                                        break
                                    else:
                                        print('Insufficient Balance. Top up balance')
                                        features()
                                        break
                                elif ch=='n' or ch=='N':
                                    print()
                                    features()
                                    break
                                else:
                                    print('Enter valid option')
                           
                    else:
                        print('Enter a valid Account number')
        else:
            print('Enter valid account number')

def viewaccount():
    with open('accounts.dat', 'rb') as g:
        l = pickle.load(g)
    while True:
        acc = int(input('Enter the remaining digits of the account number you want to view details of(ASR...): '))
        for i in l:
            if i[0]==acc:
                print('Account details are:')
                print()
                print('Name: ',i[1],'\nD.O.B: ',i[2],'\nPh.No: ',i[3])
                print('Email: ',i[4],'\nAddress: ',i[5],'\nRemaining Loan Amt: ',i[6])
                print('Balance: ',i[7])
                print()
                features()
                break
        else:
            print('Enter valid Account Number')

def payloan():
    with open('accounts.dat', 'rb') as g:
        l = pickle.load(g)
    while True:
        acc=int(input('Enter the remaining digits of account number you want to pay loan of(ASR...): '))
        for i in l:
            if i[0]==acc:
                amo=float(input('Enter amount to pay: '))
                if i[7]>amo and i[6]!=0:
                    i[6]-=amo
                    i[7]-=amo
                    with open('accounts.dat','wb') as f:
                        pickle.dump(l,f)
                    print('Loan Amount payed successfully')
                    print()
                    features()
                else:
                    print('Insufficient Balance or No Loan Pending')
                    print()
                    features()
        else:
            print('Enter valid account number')
            
                        
               

def features():
    while True:
        print('Press: \n 1 To Create a new Account \n 2 To Close an existing Account \n 3 To Apply for a Loan \n 4 To Repay an existing Loan \n 5 To view account details \n 6 Send Money \n 7 To Add Money \n 8 To Logout')
        ch = int(input('Enter your choice:'))
        print()
        if ch == 1:
            createaccount()
            break
        elif ch == 2:
            closeaccount()
            break
        elif ch == 3:
            applyloan()
            break
        elif ch == 4:
            payloan()
            break
        elif ch == 5:
            viewaccount()
            break
        elif ch == 6:
            sendmoney()
            break
        elif ch == 7:
            addmoney()
            break
        elif ch == 8:
            print('Logout successful')
            break
        else:
            print('Enter a valid input')
