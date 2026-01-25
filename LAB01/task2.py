#q.2

def evenfunc(num):
  checkeven=1
  count = 0
  while (checkeven <= num) :
    if(checkeven % 2 == 0):
      print (checkeven)
      count+=1
    checkeven=checkeven +1
  print("total even numbers:" ,count)
     
takenum=int(input("enter a number"))
evenfunc(takenum)
