# num1.int = 40
# num2.int = 20
# num3.int = 10

# num4:int = num1*num2*num3
 
# print(num4)

# num = 100
# CONST = 10 

# s = num/CONST

# if s == 50:
#   print("ok")
# else:
#   print("not ok")

# def PrintSqure():
#   a = int(input("введите значение стороны а пямоугольника"))
#   b = int(input("введите значение стороны b пямоугольника"))
#   print("Площадь прямоугольника =", a * b) #- вывод двух аргументов

# PrintSqure()






# def Calc(a:int, b:int) -> int:
#   rez = a * b
#   return rez
  
# print(Calc(10, 14))





# def Recursize():
#   def Greeting(st:str):
#     print(st)
#     if len(st) == 0:
#       return
#     else:
#       Greeting(st[:-1])
#   Greeting("Hello, word!")


# Recursize()


# array = [34, 56, 78, 90, 34, 23, 23, 67]

# print

def Das() -> bool:
  playerChoise = input("орел или решка ?").scrip().lower()
  return playerChoise == "орел"
  
  
def isWin(coin:int, playerChoise:bool):
  if coin == playerChoise:
    print("попеда")
  else:
    print("поражение")
  
def Main():
  import random
  coin = random.randint(0, 1)
  playerChoise = Das()
  IsWin(coin, playerChoise)
  
  
Main()






























