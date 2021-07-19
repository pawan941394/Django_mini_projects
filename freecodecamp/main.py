# string concantentation
# youtube = "pawan kumar"
# print("subscribe to " + youtube)
# print("subscribe to {}".format(youtube))
# print(f"subscribe to  {youtube}")



# secret number
# import random
# def guess(x):
#     random_number = numbers.randint(1,x)
#     while(expression):
# 


# print(random.randint(0,2))




# ock paper scissor game



import random

def tied(user ,computer):
    print("This match is tied because you choose " + user +" and computer choose " + computer)
def paperwin(user ,computer):
    print("paper win because you choose " + user +" and computer choose " + computer)
def rockwin(user ,computer):
    print("rock win because you choose " + user +" and computer choose " + computer)
def scissorwin(user ,computer):
    print("scissor win because you choose " + user +" and computer choose " + computer)

def play ():
    user = input("'r' for rock , 'p' for paper ,'s' for scissor = ")
    computer = random.choice(['r','p','s'])

    if user == computer:
        return tied(user ,computer)

    elif user == 'r' or computer == 'p' :
        return paperwin(user ,computer)

    elif user == 'r' or computer == 's' :
        return rockwin(user ,computer)

    elif user == 'p' or computer == 's' :
        return scissorwin(user ,computer)
    else:
        print("you enter wrong key soo ab nikl yaha se")



print("Welcome to rock paper scissor game ")
a = input("if you wan to play game then enter 1 otherwise enter 0 = ")

if a == '1':
    play ()
else:
      print("you exit the game byy ")

