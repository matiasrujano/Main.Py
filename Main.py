# Matias Rujano
# This program will be a fun and interactive mathematics quiz.

print("Welcome to Math Play!")
print("Please tell me your name")
name=input()
print("\n""Nice to meet you",name,end="!"'\n\n')
print("Let me explain the rules of the game:""\n""In this game you will be asked mathematical questions""\n""The questions will increase in difficulty as we advance""\n""There will be X questions in total""\n""If you answer at least Y of them correctly""\n""You will win a fun prize!"'\n')
#Total number of questions pending - I will correct when quiz is finished.
print(name,",are you ready to start playing? Yes or No?",sep=" ")
confirmation=input()
if (confirmation=="no")or(confirmation=="No"):
    print("Come back when you are!")
else:
    print('\n'"Awesome!""\n""Question #01""\n"+name,",what is the result for the fallowing operation?""\n""11+22+33+44+55+66+77+88+99")
userInput1=int(input())
answer1=11+22+33+44+55+66+77+88+99
if userInput1==answer1:
    print("Congratulations you are correct!")
elif userInput1!=answer1:
    print("Your answer was incorrect! The correct answer is:",answer1,end="!"'\n')
print('\n'"Question #02""\n"+name,",what is the result for the following operation?""\n""999-88-77-66-55-44-33-22-11")
userInput2=int(input())
answer2=999-88-77-66-55-44-33-22-11
if userInput2==answer2:
    print("Congratulations you are correct!")
elif userInput2!=answer2:
    print("Your answer was incorrect! The correct answer is:",answer2,end="!"'\n')
print('\n'"Question #03""\n"+name,",what is the result for the following operation?""\n""1*2*3*4*5*6*7*8*9*10")
userInput3=int(input())
answer3=1*2*3*4*5*6*7*8*9*10
if userInput3==answer3:
    print("Congratulations you are correct!")
elif userInput3!=answer3:
    print("Your answer was incorrect! The correct answer is:",answer3,end="!"'\n')
print('\n'"Question #04""\n"+name,",what is the result for the following operation?""\n""2 to the power of 10")
userInput4=int(input())
answer4=2**10
if userInput4==answer4:
    print("Congratulations you are correct!")
else:
    print("Your answer was incorrect! The correct answer is:",answer4,end="!"'\n')
print('\n'"Question #05"'\n'+name,",what is the result for the following operation?""\n""999 divided by 9")
userInput5=int(input())
answer5=999/9
if userInput5==answer5:
    print("Congratulations you are correct!")
if userInput5!=answer5:
    print("Your answer was incorrect! The correct answer is:",answer5,end="!"'\n')
print('\n'"Question #06"'\n'+name,",what is the result for the following operation?""\n""The remainder obtained from dividing 10 by 3")
userInput6=int(input())
answer6=10%3
if userInput6==answer6:
    print("Congratulations you are correct!")
else:
    print("Your answer was incorrect! The correct answer is",answer6,end="!"'\n')
print('\n'"Question #07"'\n'+name,",what is the result for the following operation?""\n""The quotient obtained from dividing 10 by 3?")
userInput7=int(input())
answer7=10//3
if userInput7==answer7:
    print("Congratulations you are correct!")
else:
    print("Your answer was incorrect! The correct answer is",answer7,end="!"'\n')
print('\n'"Multiple choice BONUS!"*3,end=" ")
print('\n\n'"What is the square root of 49?(Choose a letter)"'\n'+"A)6"'\n'+"B)8"'\n'+"C)7")
userInput8=input()
if (userInput8=="C")or(userInput8=="c"):
    print("Congratulations you are correct!")
else:
    print("Your answer was incorrect! The correct answer is",7,end="!"'\n')
print('\n'"Question #08"'\n'+name,"what is the value for X in the following equation?""\n""5X+20=25?")
userInput8=int(input())
question8=1
if userInput8==question8:
    print("Congratulations you are correct!")
elif (userInput8<=3)and(userInput8>=2)or(userInput8>=0)and(userInput8<1):
    print("You were close, but the correct answer is",question8,end="!"'\n')
else:print("Your answer was incorrect! The correct answer is",question8,end="!"'\n')
print('\n'"Question #09"'\n'+name,",From the image below, how many squares individual and grouped can you identify?"'\n')
for row in range(4):
    for column in range(4):
      print("[]", end="")
    print()
userInput9=int(input())
question9=21
if userInput9==question9:
    print("Congratulations you are correct!")
elif (userInput9<=23)and(userInput9>=22)or(userInput9>=19)and(userInput9<=20):
    print("You were close, but the correct answer is",question9,end="!"'\n')
else:print("Your answer was incorrect! The correct answer is",question9,end="!"'\n')
print('\n'"Question #10"'\n'+name,",how many multiples of 3 appear in the sequence below?"'\n')
x = 5
while x <= 55:
    print(x, end=" ")
    x += 5
userInput10=int(input('\n'))
question10=3
if userInput10==question10:
    print("Congratulations you are correct!")
elif (userInput10<=6)and(userInput10>=5)or(userInput10>=2)and(userInput10<=3):
    print("You were close, but the correct answer is",question10,end="!"'\n')
else:print("Your answer was incorrect! The correct answer is",question10,end="!"'\n')
print('\n'"Question #11"'\n'+name,",how many multiples of 5 appear in the sequence below?"'\n')
x = 5
while x <= 4000:
    print(x, end=" ")
    x *= 5
userInput11=int(input('\n'))
question11=5
if userInput11==question11:
    print("Congratulations you are correct!")
elif (userInput11 <= 7)and(userInput11 >= 6)or(userInput11 <= 3)and(userInput11 <= 4):
    print("You were close, but the correct answer is",question11,end="!"'\n')
else:print("Your answer was incorrect! The correct answer is",question11,end="!"'\n')
#This function will calculate the diameter of a circle based on the radius input of the user
def diameter_circle(radius):
    diameter=2*radius
    return diameter
def main():
    print('\n'"Question #12"'\n'+name,"Enter a number between 1 and 10")
    radius=int(input())
    while (radius>10)or(radius<1):
        print("That was not a valid number. Please try again.")
        radius=int(input("Enter a number between 1 and 10"'\n'))
    else:
        print("What is the diameter for the circle with radius",radius,"?")
    user_input12=int(input())
    answer12=diameter_circle(radius) #call to diameter_circle(radius)
    if user_input12==answer12:
        print("Congratulations you are correct!")
    else:
        print("Your answer was incorrect! The correct answer is",answer12,end="!"'\n')
#call to main
main()







