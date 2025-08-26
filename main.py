import pickle
def dash(name):
    print('Welcome,',name)
    print('How can we help you today?')
    import Features
    Features.features()
def register():
    f=open('users.dat', 'rb+')
    L = pickle.load(f)
    print('Please enter the following details to Register with us \n')
    name=input('Enter your name: ')
    user = input('Create a new Username: ')
    pas = input('Create a new Password: ')
    while True:
        email= input('Enter your Email ID: ')
        if email.count('@')==0 or email.count('@')>1:
            print('Enter a valid Email ID')
        else:
            break
    k = [name,user,pas,email]
    L.append(k)
    with open('users.dat', 'wb') as f:
        pickle.dump(L, f)
    print()
    print('Your Registration is successful!! \n')
    ch=input('Press any key to continue to login: \n')
    if ch!='  ':
        login()

def login():
    with open('users.dat', 'rb') as f:
        L = pickle.load(f)
    us = input('Enter your Username: ')
    pa = input('Enter your Password: \n')
    for i in L:
        if i[1] == us and i[2] == pa:
            dash(i[0])
            break
    else:
        print('You have not registered. Please register first. \n')
        main()

def main():
    while True:
        print('Welcome to Unity Bank \n')
        print('Press: \n 1.To Login \t 2.To Register \t 3.To Exit \n')
        ch = int(input('Enter your choice:\n'))
        if ch == 1:
            login()
            break
        elif ch == 2:
            register()
        elif ch == 3:
            print('Goodbye!')
            break
        else:
            print('Enter valid input')

main()
