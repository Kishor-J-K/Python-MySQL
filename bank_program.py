import mysql.connector
import random
conn=mysql.connector.connect(
    host='localhost',
    username='root',
    password='18271827NKnk@',
    database='bank'
    )

mycursor = conn.cursor()

def account_no():
    while True:
        x=random.randint(1000,9999)
        mycursor.execute(f"SELECT * FROM accounts WHERE AccountNumber={x}")
        result=mycursor.fetchone()
        if result is None:
            break
    return x

def create_acc():
    while True:
        acc_name=input("Enter your name (without space): ")
        acc_age=int(input("Enter your age: "))
        while True:
            acc_gender=input("Enter your gender (M/F/T): ")
            acc_gender=acc_gender.upper()
            if acc_gender== 'M' or acc_gender=='F' or acc_gender== 'T':
                break
            print("We accept only male,female and trans. We request you to chose from the option: ")
        acc_no=account_no()
        print(f"Your account number will be: {acc_no}")
        acc_pass=input("Set a strong passward: ")
        a=input("Enter password for confirmation: ")
        if acc_pass!=a:
            while True:
                print("Password din't match 😖")
                acc_pass=input("Set a strong passward: ")
                if acc_pass==input("Enter password for confirmation: "):
                    break
        a=0
        data=(acc_no,acc_pass,acc_name,acc_gender,a,acc_age)
        entry="INSERT INTO accounts value (%s,%s,%s,%s,%s,%s)"
        mycursor.execute(entry,data)
        conn.commit()
        mycursor.execute(f"SELECT * FROM accounts WHERE AccountNumber={acc_no} and passward={acc_pass}")
        result=mycursor.fetchone()
        if result is not None:
            break
        print("something went wrong 😖")
        print("please try again ")
    print(f'''
            ------------------- ACCOUNT CREATION SUCCESSFUL -------------------
            Account Number : {acc_no}
            Name           : {acc_name}
            Age            : {acc_age}
            gender         : {acc_gender}
            Account Balance: 0
            ''')
    
def acc_info():
    while True:
        acc_no=int(input("enter your account no: "))
        acc_pass=input("enter the password: ")
        mycursor.execute(f"select name,balence from accounts where AccountNumber={acc_no} and passward={acc_pass}")
        result=mycursor.fetchone()
        if result is not None:
            break
        else:
            print("Account_no/Password is correct")
            ch=input("enter E to exit and any other key to try again: ")
            if ch==ch.upper():
                return
    a=0
    print()
    for i in result :
        if a==0:
            print(f"name: {i} 😁")
            a=a+1
        elif a==1:
            print(f"balence: {i} 💵")
            
def depo_am():
    while True:
        acc_no=int(input("enter your account no: "))
        acc_pass=input("enter the password: ")
        mycursor.execute(f"select balence from accounts where AccountNumber={acc_no} and passward={acc_pass}")
        result=mycursor.fetchone()
        if result is not None:
            break
        else:
            print("Account_no/Password is correct")
            ch=input("enter E to exit and any other key to try again: ")
            if ch==ch.upper():
                return
    am=int(input("enter amount to deposit: "))
    for i in result:
        am=am+int(i)
    mycursor.execute(f"update accounts set balence={am} where AccountNumber={acc_no} and passward={acc_pass}")
    conn.commit()
    print("----------------TRANSACTION SUCCESSFULL-----------------")
    print()
    mycursor.execute(f"select name,balence from accounts where AccountNumber={acc_no} and passward={acc_pass}")
    result=mycursor.fetchone()
    a=0
    for i in result :
        if a==0:
            print(f"name: {i} 😁")
            a=a+1
        elif a==1:
            print(f"balence: {i} 💵")

def with_am():
    while True:
        acc_no=int(input("enter your account no: "))
        acc_pass=input("enter the password: ")
        mycursor.execute(f"select name,balence from accounts where AccountNumber={acc_no} and passward={acc_pass}")
        result=mycursor.fetchone()
        if result is not None:
            break
        else:
            print("Account_no/Password is correct")
            ch=input("enter E to exit and any other key to try again: ")
            if ch==ch.upper():
                return
    a=0
    print()
    for i in result :
        if a==0:
            print(f"name: {i} 😁")
            a=a+1
        elif a==1:
            bal=int(i)
            print(f"balence: {i} 💵")
    print()
    while True:
        am=int(input("Enter amount to dithdraw: "))
        if am>bal:
            print("Insufficient balence.😖")
            am=input("ente E to exit or any other key to try again: ")
            if am.upper()=='E':
                return
        else:
            break
    bal=bal-am
    mycursor.execute(f"update accounts set balence={bal} where AccountNumber={acc_no} and passward={acc_pass}")
    conn.commit()
    print("-----------------------TRANSACTION SUCCESSFUL-------------------------")
            
while True:
    print('''
          ----------------  WELCOME 🙏 TO KHAN BANK 🏦  -----------------
          1. OPEN ACCOUNT 📂
          2. CHECK ACCOUNT INFO 📖
          3. DEPOSIT MONEY 💱💵
          4. WITHDRAW MONEY 💱💵
          5. EXIT 🔴
          ''')
    ch=int(input("Enter choice in withrespect to no: "))
    
    if ch==1:
        create_acc()
    elif ch==2:
        acc_info()
    elif ch==3:
        depo_am()
    elif ch==4:
        with_am()
    elif ch==5:
        break
    else:
        print("pleas there correct option ")

print("Thankyou for your time 🙋‍♂️")