
def func1(n:int):
    summarize1 = 0
    for i in range(1,n):
        if i % 2 == 0:
            summarize1 += i
    i = 1
    summarize2 = 0
    while i<n:
        if i%2 == 0:
            summarize2 += i
        i+=1
    if summarize1 == summarize2:
        print(summarize2)
def func2(arr):
    max_length = 0
    for el in arr:
        if max_length < len(el):
            max_length = len(el)
            max_el = el
    print(max_el)
    max_length = 0
    i_local = 0
    while ( i_local < len(arr)):
        #print(max_length,len(arr[i_local]), max_length < len(arr[i_local]))
        if max_length < len(arr[i_local]):
            max_length = len(arr[i_local])
            max_el = arr[i_local]
        i_local += 1
    print(max_el)


def func3(n:int): #n!
    factor = 1
    if n == 0:
        print(1)
        return 1
    for i in range(1,n+1):
        factor*=i
        print(factor)
    return factor
     
def func4(arr): #Вывести каждый 3 элемент списка вместе с его индексом, используя enumerate()
    for index,values in enumerate(arr):
        if (index+1) % 3 == 0:
            print(values)

def func5(n:int):
    print("  " + str(n))
    for i in range(1,10):
        print(f'{i} {i*n}')

def func6(n:int):
    a = str(n)
    count1 = 0
    for i in a:
        if i != '.':
            count1+=1
    print(count1)
    buf = n #need to fix for n in R
    count2 = 0
    while(buf != 0): 
        buf //= 10
        count2 += 1
    print(count2)

def func7(string_in:str):
    if (string_in == string_in[::-1]):
        print(True)
    else:
        print(False)

def func8(arr):
    s_arr = sorted(arr)
    print(len(s_arr))
    for i in range(len(s_arr)-1):
        if s_arr[i] == s_arr[i+1]:
            print("True")
            return
    print("False")

def func9(arr):
    i = 0
    while i < len(arr):
        j = i + 1
        while j < len(arr):
            if arr[i] == arr[j]:
                del arr[j]
            else:
                j += 1
        i += 1
    print(arr)

def func9_var2(arr):
    narr = []
    for el in arr:
        if el not in narr:
            narr.append(el)
    print(narr)

def func10(str1):
    for i in range(len(str1)-1,-1,-1):
        print(str1[i])

def func11():
    print("Пн Вт Ср Чт Пт Сб Вс")
    count_days = 0
    while True:
        for i in range(7):
            count_days+=1
            if count_days == 32:
                return
            print(f'{count_days:>2}',end=' ')
        print()
   





if __name__== '__main__':
    #func1(5)
    #func2(['t','task2_tested','some_garbage'])
    #func3(5)
    #func4([2,5,1,56,5,7,6,9,10])
    #func5(9)
    #func6(12)
    #func7("sdss")
    #func8([2,7,1,3,8])
    #func9([2,1,5,6,6,2,1])
    #func9_var2([2,1,5,6,6,2,1])
    #func10("Hello World!")  
    func11()