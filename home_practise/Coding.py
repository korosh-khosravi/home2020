import sqlite3
from sqlite3 import Error

connect = sqlite3.connect('Employee')
c = connect.cursor()


def input_table_name():
    print('enter ur table name: ')
    table_name = str(input())
    print('enter ur row(s)[Beware If U Enter a 0, Ur Table Is Create!]:')
    rows = list('')
    while True:
        row = input()
        if row == "":
            print("U Enter a Blank! Try Again.")
            continue
        if row == '0' and rows == list(''):
            print("Ur List Still Empty! Try Again.")
            continue
        elif row == '0':
            print("End.")
            break
        else:
            rows += row
    print("Ur colomn is: ")
    for x in rows:
        print(x)
    type(row)
    return table_name, rows

a,b = input_table_name()
CREATE_TABLE(a, b)

def CREATE_TABLE(self,self1):
    #a.execute('''create table {a} ()''')
    return 0