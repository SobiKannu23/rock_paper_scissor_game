import random
number_guess=random.randint(1,100)

while True:
 try:
  guess = int(input("enter number between 1 to 100:"))
  if guess<number_guess:
    print("too low")

    print("too high")
  else: 
    print('congrats you guessed the number')
    break
 except ValueError:
  print("please enter a valid number")



