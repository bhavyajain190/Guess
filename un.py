import random

print('Hey what is your name?')
name = input() 

print('Welcome ' + name + ' I am thinking of a number between 1 and 10')
Num = random.randint(1,10)

for guessesTaken in range(1,3):
  print('Take a guess')
  guess = int(input())

  if guess < Num:
    print('Your guess is a lttle low')
  elif guess > Num:
    print('Your guess is too high')
 
if guess == Num:
  print('congratulations ' + name + ' you have guessed my number in ' + str(guessesTaken) + ' guesses!!')
else:
  print('I am sorry number was ' + str(Num))