def addnums(a,b):
    answer=a+b
    print("sum is:",answer)
    return answer

def subnums(a,b):
    answer=a-b
    print("the difference is:",answer)
    return answer

choice=int(input("enter your choice (1-add, 2-sub, 3-exit):"))

while (choice != 3):
    if choice == 1:
        num1=int(input("enter the first number"))
        num2=int(input("enter the second number"))
        addnums(num1,num2)
         
    elif choice == 2:
        num1=int(input("enter the first number"))
        num2=int(input("enter the second number"))
        subnums(num1,num2)
    else : print("wrong number entered")
    
    choice=int(input("enter your choice (1-add, 2-sub, 3-exit):"))
