import random
print()
kp='y'
while(kp=='y' or kp=='Y'):
    comp_guess='n'
    b=0
    print(" Game Starts!")
    min=int(input(" enter the min_value of the range: "))
    max=int(input(" enter the max_value of the range: "))
    while(comp_guess!=b):
       comp_guess=random.randint(min,max)
       b=int(input(" enter your guess: "))
       if(b==comp_guess):
          print(" Right guess!")
       elif(comp_guess!=b):
         print(" wrong guess!")
       else:
         print(" invalid input")
    kp=str(input(" Want to continue (y/n)? :"))
    print()
print('Game Ends!')
print()