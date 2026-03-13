
#q.1:
import random
def func(x):
  return -x**2 + 6*x

def hill_climbing( ):
  x = random.randint(0,6)
  print("starting value of x =",x)
  print("f(x)=",func(x))

  while True :
    neighbours= []

    if x+1 <= 6:
      neighbours.append(x+1)
    if x-1 >= 0:
      neighbours.append(x-1)

    best = max(neighbours,key = func)

    if func(best) <= func(x):
      break
    x=best
    print("Move to x:",x,"f(x):",func(x))
  
  print("Final optimal x:", x)
  print("Maximum value:", func(x))
      
hill_climbing()
