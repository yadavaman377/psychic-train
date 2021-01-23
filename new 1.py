def addition(lst):
    count=0
    for i in range(0, len(lst)):
        count = count + lst[i]
    print(count)


n= int(input("enter the numbers="))
lst=[]
for i in range(n):
    lst.append(int(input()))
    
addition(lst)
