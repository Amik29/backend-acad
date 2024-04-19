def f1():
    str1 = str(input("Введите строку:\n"))
    print(str1[::-1])
def f2():
    str1 = str(input("Введите строку c h:\n"))
    str1 = str1[0] + str1[1:-1].replace('h','H') + str1[-1]
    print(str1)
def f3():
    str1 = str(input("Введите строку\n"))
    arr = str1.split(' ')  # Есть проблема со спамом пробела, TODO: Fix 
    print(len(arr))
def f4():
    str1 = str(input("Введите строку\n"))
    print(str1.count(' ') + 1)
def f5():
    str1 = str(input("Введите строку:\n"))
    arr = str1.split(' ')
    strOut =  arr[1] + " " + arr[0]
    print(strOut)
def f6():
    str1 = str(input("Введите ФИО:\n"))
    arr = str1.split(' ')
    stringOut = arr[0] + ' ' +arr[1][0] + '.' + arr[2][0] + '.'
    print(stringOut)
def f7():
    s = [1,[2.1,[2+1j,[[],2,"Иголка"]]]]
    print(s[1][1][1][2])

def f8():
    s1 = [2,3,4]

    s2 = [4,1,6]

    s3 = [2,5,7]
    s3.extend(s2)
    print(s3)
    print(s1+s2)

def f9():
    s1 = [2,3,4,5]

    s2 = [4,1,6,5,3]
    s3 = s1+s2
    s3.sort()
    s3 = list(set(s3))
    print(s3)

def f10():
    s1 = [2,3,4,5]
    s2 = [2,2,4,5,1]
    s3 = list(set(s1))
    s4 = list(set(s2))
    print(len(s1) == len(s3))
    print(len(s2)==len(s4))

def f11():
    date_dict = {'year': 2024, 'month': 4, 'day': 14}
    print(str(date_dict['year']) + '-' + str(date_dict['month']) +'-'+ str(date_dict['day']))

def f12():
    string = str(input())
    arr = string.split(',')
    kort  = tuple(arr)
    print(arr)
    print(kort)

def f13():
    students = {'Schultz', 'Django', 'Brunhilde', 'Fritz'}
    employees = {'Schultz', 'Django', 'Calvin', 'Butch', 'Fritz'}
    print(students | employees)
    print(students.union(employees))
    
    print(students & employees)
    print(students.intersection(employees))

    print(employees - students)
    print(employees.difference(students))

    print(students ^ employees)
    print(students.symmetric_difference(employees))

def f14():
    import numpy as np
    array = [
        [11, 12, 13, 14, 15],
        [21, 22, 23, 24, 25],
        [31, 32, 33, 34, 35],
        [41, 42, 43, 44, 45],
        [51, 52, 53, 54, 55]
    ]
    print(np.transpose(array))
def f15():
    print("X" + 0*'x' + "X")
    print("X" + 2*'x' + "X")
    print("X" + 4*'x' + "X")
    print("X" + 6*'x' + "X")
    print("X" + 8*'x' + "X")

if __name__== '__main__':
    f15()