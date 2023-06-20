import mysql.connector as a
mycon = a.connect(host='localhost',user='root',password='1234')

if mycon.is_connected():
    print("connected....")
cur = mycon.cursor()
c1="create database if not exists ATM"
cur.execute(c1)

c2="use ATM"
cur.execute(c2)

c3="create table if not exists Cash_Withdrwal(Amount int, note_2000 int, note_500 int,note_200 int,note_100 int,note_50 int,note_20 int,note_10 int,note_1 int)"
cur.execute(c3)


def amount_withdraw():
  c4 = "select * from Cash_Withdrwal"
  cur.execute(c4)
  result=cur.fetchall()
  for row in result:
    print(row)

nnotes = [10,20,30,40,50,20,50,10]
notes = [2000,500,200,100,50,20,10,1]
l2=[]
def ATM1(n):
    q=n
    j=0
    for i in notes:
        if(nnotes[j]==0):
            l2.append(nnotes[j])
            j+=1
            continue
        else:
            a=n//i
            if(nnotes[j]>=a):
                l2.append(a)
                b = n % i
                n = b
                nnotes[j] = nnotes[j] - a
            else:
                b = n % i
                n = (((a - nnotes[j]) * i) + b)
                a = nnotes[j]
                l2.append(a)
                nnotes[j] = nnotes[j] - a
        j+=1

def AMT():
    n = int(input("Enter the amount:"))
    n1 = 0
    ATM1(n)
    cur = mycon.cursor()
    data = (n, l2[0], l2[1], l2[2], l2[3], l2[4], l2[5], l2[6], l2[7])
    sql1 = "insert into Cash_Withdrwal(Amount,note_2000,note_500,note_200,note_100,note_50,note_20,note_10,note_1) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cur.execute(sql1, data)
    call_function()


def call_function():
    print("1. Want to withdraw cash:")
    print("1.Yes \n2.No")
    n1 = int(input("Enter the input:"))
    if (n1 == 1):
        AMT()
    else:
        mycon.commit()
        exit()

call_function()

