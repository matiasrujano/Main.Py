# Matias Rujano
# This program will be a fun and interactive mathematics quiz.


# This function will greet the user, explain rules and display questions
def questions():
    print("Welcome to Math Play!")
    print("Please tell me your name")
    name = input()
    print("\n""Nice to meet you", name, end="!"'\n\n')
    print(
        "Let me explain the rules of the game:""\n""In this game you will be "
        "asked mathematical questions""\n""The questions will increase in "
        "difficulty as we advance""\n""There will be 12 questions in "
        "total"'\n')
    print("LETS GO!")
    print('\n'"Question #01""\n" + name, ",what is the result for the"
                                         "fallowing operation?""\n""11+22+33+44+55+66+77+88+99")
    answer1 = 11 + 22 + 33 + 44 + 55 + 66 + 77 + 88 + 99
    while True:
        userInput1 = input()
        try:
            int(userInput1)
        except ValueError:
            print("That was not a valid answer. Please try again.")
        else:
            break
    userInput1 = int(userInput1)
    if userInput1 == answer1:
        print("Congratulations you are correct!")
    else:
        print("Your answer was incorrect! The correct answer is:", answer1,
              end="!"'\n')

    print('\n'"Question #02""\n" + name,
          ",what is the result for the following operation?""\n"
          "999-88-77-66-55-44-33-22-11")
    answer2 = 999 - 88 - 77 - 66 - 55 - 44 - 33 - 22 - 11
    while True:
        userInput2 = input()
        try:
            int(userInput2)
        except ValueError:
            print("That was not a valid answer. Please try again.")
        else:
            break
    userInput2 = int(userInput2)
    if userInput2 == answer2:
        print("Congratulations you are correct!")
    else:
        print("Your answer was incorrect! The correct answer is:", answer2,
              end="!"'\n')

    print('\n'"Question #03""\n" + name,
          ",what is the result for the following operation?""\n"
          "1*2*3*4*5*6*7*8*9*10")
    answer3 = 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10
    while True:
        userInput3 = input()
        try:
            int(userInput3)
        except ValueError:
            print("That was not a valid answer. Please try again.")
        else:
            break
    userInput3 = int(userInput3)
    if userInput3 == answer3:
        print("Congratulations you are correct!")
    else:
        print("Your answer was incorrect! The correct answer is:", answer3,
              end="!"'\n')

    print('\n'"Question #04""\n" + name,
          ",what is the result for the following operation?""\n"
          "2 to the power of 10")
    answer4 = 2 ** 10
    while True:
        userInput4 = input()
        try:
            int(userInput4)
        except ValueError:
            print("That was not a valid answer. Please try again.")
        else:
            break
    userInput4 = int(userInput4)
    if userInput4 == answer4:
        print("Congratulations you are correct!")
    else:
        print("Your answer was incorrect! The correct answer is:", answer4,
              end="!"'\n')

    print('\n'"Question #05"'\n' + name,
          ",what is the result for the following operation?""\n"
          "999 divided by 9")
    answer5 = 999 / 9
    while True:
        userInput5 = input()
        try:
            int(userInput5)
        except ValueError:
            print("That was not a valid answer. Please try again.")
        else:
            break
    userInput5 = int(userInput5)
    if userInput5 == answer5:
        print("Congratulations you are correct!")
    else:
        print("Your answer was incorrect! The correct answer is:", answer5,
              end="!"'\n')

    print('\n'"Question #06"'\n' + name,
          ",what is the result for the following operation?""\n""The remainder"
          " obtained from dividing 10 by 3")
    answer6 = 10 % 3
    while True:
        userInput6 = input()
        try:
            int(userInput6)
        except ValueError:
            print("That was not a valid answer. Please try again.")
        else:
            break
    userInput6 = int(userInput6)
    if userInput6 == answer6:
        print("Congratulations you are correct!")
    else:
        print("Your answer was incorrect! The correct answer is:", answer6,
              end="!"'\n')

    print('\n'"Question #07"'\n' + name,
          ",what is the result for the following operation?""\n""The quotient"
          " obtained from dividing 10 by 3?")
    answer7 = 10 // 3
    while True:
        userInput7 = input()
        try:
            int(userInput7)
        except ValueError:
            print("That was not a valid answer. Please try again.")
        else:
            break
    userInput7 = int(userInput7)
    if userInput7 == answer7:
        print("Congratulations you are correct!")
    else:
        print("Your answer was incorrect! The correct answer is:", answer7,
              end="!"'\n')

    print('\n'"Multiple choice BONUS!" * 3, end=" ")
    print('\n\n'"What is the square root of 49? (Choose a letter)"'\n' +
          "A)6"'\n' + "B)8"'\n' + "C)7")
    userInput8 = input()
    if (userInput8 == "C") or (userInput8 == "c"):
        print("Congratulations you are correct!")
    else:
        print("Your answer was incorrect! The correct answer is C!")

    print('\n'"Question #08"'\n' + name,
          "what is the value for X in the following equation?""\n""5X+20=25?")
    answer8 = 1
    while True:
        userInput8 = input()
        try:
            int(userInput8)
        except ValueError:
            print("That was not a valid answer. Please try again.")
        else:
            break
    userInput8 = int(userInput8)
    if userInput8 == answer8:
        print("Congratulations you are correct!")
    else:
        print("Your answer was incorrect! The correct answer is:", answer8,
              end="!"'\n')

    print('\n'"Question #09"'\n' + name,
          ",From the image below, how many squares individual and grouped can "
          "you identify?"'\n')
    for row in range(4):
        for column in range(4):
            print("[]", end="")
        print()
    answer9 = 21
    while True:
        userInput9 = input()
        try:
            int(userInput9)
        except ValueError:
            print("That was not a valid answer. Please try again.")
        else:
            break
    userInput9 = int(userInput9)
    if userInput9 == answer9:
        print("Congratulations you are correct!")
    elif (userInput9 <= 23) and (userInput9 >= 22) or (userInput9 >= 19) and (
            userInput9 <= 20):
        print("You were close, but the correct answer is", answer9,
              end="!"'\n')
    else:
        print("Your answer was incorrect! The correct answer is:", answer9,
              end="!"'\n')

    print('\n'"Question #10"'\n' + name,
          ",how many multiples of 3 appear in the sequence below?")
    x = 5
    while x <= 55:
        print(x, end=" ")
        x += 5
    answer10 = 3
    while True:
        userInput10 = input()
        try:
            int(userInput10)
        except ValueError:
            print("That was not a valid answer. Please try again.")
        else:
            break
    userInput10 = int(userInput10)
    if userInput10 == answer10:
        print("Congratulations you are correct!")
    elif (userInput10 <= 6) and (userInput10 >= 5) or (userInput10 >= 2) and (
            userInput10 <= 3):
        print("You were close, but the correct answer is", answer10,
              end="!"'\n')
    else:
        print("Your answer was incorrect! The correct answer is", answer10,
              end="!"'\n')

    print('\n'"Question #11"'\n' + name,
          ",how many multiples of 5 appear in the sequence below?")
    x = 5
    while x <= 4000:
        print(x, end=" ")
        x *= 5
    answer11 = 5
    while True:
        userInput11 = input()
        try:
            int(userInput11)
        except ValueError:
            print("That was not a valid answer. Please try again.")
        else:
            break
    userInput11 = int(userInput11)
    if userInput11 == answer11:
        print("Congratulations you are correct!")
    elif ((userInput11 <= 7) and (userInput11 >= 6)) or (
            (userInput11 <= 3) and (
            userInput11 <= 4)):
        print("You were close, but the correct answer"
              " is", answer11, end="!"'\n')
    else:
        print("Your answer was incorrect! The correct answer is", answer11,
              end="!"'\n')
    return name


# This function will calculate the diameter of a circle based on the radius input of the user
def diameter_circle(radius):
    diameter = (2 * radius)
    return diameter


def main():
    print(questions())  # call to questions
    print('\n'"Question #12"'\n'"Enter a number")
    while True:
        radius = input()
        try:
            int(radius)
        except ValueError:
            print("That was not a valid answer. Please try again.")
        else:
            break
    radius = int(radius)
    print("What is the diameter for the circle with radius", radius, "?")
    answer12 = int(diameter_circle(radius))  # call to diameter_circle
    while True:
        input12 = input()
        try:
            int(input12)
        except ValueError:
            print("That was not a valid answer. Please try again.")
        else:
            break
    input12 = int(input12)
    if input12 == answer12:
        print("Congratulations you are correct!")
    else:
        print("Your answer was incorrect! The correct answer is", answer12,
              end="!"'\n')
    print('\n'"THE END")


# call to main
main()
